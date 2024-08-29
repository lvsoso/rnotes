package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os/exec"
	"sync"
	"time"

	"github.com/gorilla/mux"
	"github.com/gorilla/websocket"
	"gopkg.in/natefinch/lumberjack.v2"
)

// Task struct
type Task struct {
	ID           string    `json:"id"`
	Command      string    `json:"command"`
	Args         []string  `json:"args"`
	Status       string    `json:"status"`
	StartTime    time.Time `json:"start_time"`
	StopTime     time.Time `json:"stop_time,omitempty"`
	Error        string    `json:"error,omitempty"`
	AutoRestart  bool      `json:"auto_restart"`
	MaxRestarts  int       `json:"max_restarts"`
	RestartCount int       `json:"restart_count"`
	cmd          *exec.Cmd `json:"-"`
	stopChan     chan struct{}
	stoppedChan  chan struct{}
	logger       *log.Logger
}

type TaskManager struct {
	tasks  map[string]*Task
	mutex  sync.RWMutex
	logger *log.Logger
}

// NewTaskManager function
func NewTaskManager(logger *log.Logger) *TaskManager {
	return &TaskManager{
		tasks:  make(map[string]*Task),
		logger: logger,
	}
}

func (tm *TaskManager) StartTask(id, command string, autoRestart bool, maxRestarts int, args ...string) error {
	tm.mutex.Lock()
	defer tm.mutex.Unlock()

	if _, exists := tm.tasks[id]; exists {
		return fmt.Errorf("task with ID %s already exists", id)
	}

	task := &Task{
		ID:           id,
		Command:      command,
		Args:         args,
		Status:       "Starting",
		StartTime:    time.Now(),
		AutoRestart:  autoRestart,
		MaxRestarts:  maxRestarts,
		RestartCount: 0,
		stopChan:     make(chan struct{}),
		stoppedChan:  make(chan struct{}),
	}

	tm.tasks[id] = task

	go tm.runTask(task)

	return nil
}

func (tm *TaskManager) StopTask(id string) error {
	tm.mutex.RLock()
	task, exists := tm.tasks[id]
	tm.mutex.RUnlock()

	if !exists {
		return fmt.Errorf("task with ID %s not found", id)
	}

	if task.Status != "Running" && task.Status != "Restarting" {
		return fmt.Errorf("task with ID %s is not running or restarting", id)
	}

	close(task.stopChan)
	<-task.stoppedChan
	return nil
}

func (tm *TaskManager) GetTaskStatus(id string) (string, error) {
	tm.mutex.RLock()
	defer tm.mutex.RUnlock()

	task, exists := tm.tasks[id]
	if !exists {
		return "", fmt.Errorf("task with ID %s not found", id)
	}

	return task.Status, nil
}

func (tm *TaskManager) ListTasks() []Task {
	tm.mutex.RLock()
	defer tm.mutex.RUnlock()

	tasks := make([]Task, 0, len(tm.tasks))
	for _, task := range tm.tasks {
		tasks = append(tasks, *task)
	}
	return tasks
}

// runTask method
func (tm *TaskManager) runTask(task *Task) {
	defer close(task.stoppedChan)

	for {
		task.cmd = exec.Command(task.Command, task.Args...)
		task.Status = "Running"
		tm.logger.Printf("Task %s started: %s %v", task.ID, task.Command, task.Args)

		err := task.cmd.Start()
		if err != nil {
			task.Status = "Error"
			task.Error = err.Error()
			tm.logger.Printf("Task %s failed to start: %v", task.ID, err)
			break
		}

		done := make(chan error)
		go func() {
			done <- task.cmd.Wait()
		}()

		select {
		case err := <-done:
			if err != nil {
				task.Status = "Error"
				task.Error = err.Error()
				tm.logger.Printf("Task %s failed: %v", task.ID, err)
				if task.AutoRestart && (task.MaxRestarts == 0 || task.RestartCount < task.MaxRestarts) {
					task.RestartCount++
					task.Status = "Restarting"
					tm.logger.Printf("Task %s restarting (attempt %d)", task.ID, task.RestartCount)
					time.Sleep(5 * time.Second) // Wait before restarting
					continue
				}
			} else {
				task.Status = "Completed"
				tm.logger.Printf("Task %s completed successfully", task.ID)
			}
		case <-task.stopChan:
			if err := task.cmd.Process.Kill(); err != nil {
				task.Status = "Error"
				task.Error = err.Error()
				tm.logger.Printf("Task %s failed to stop: %v", task.ID, err)
			} else {
				task.Status = "Stopped"
				tm.logger.Printf("Task %s stopped", task.ID)
			}
			<-done
		}

		break
	}

	task.StopTime = time.Now()
}

func (tm *TaskManager) startTaskHandler(w http.ResponseWriter, r *http.Request) {
	var taskRequest struct {
		ID          string   `json:"id"`
		Command     string   `json:"command"`
		Args        []string `json:"args"`
		AutoRestart bool     `json:"auto_restart"`
		MaxRestarts int      `json:"max_restarts"`
	}

	if err := json.NewDecoder(r.Body).Decode(&taskRequest); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	tm.mutex.Lock()
	defer tm.mutex.Unlock()

	if _, exists := tm.tasks[taskRequest.ID]; exists {
		http.Error(w, fmt.Sprintf("Task with ID %s already exists", taskRequest.ID), http.StatusConflict)
		return
	}

	task := &Task{
		ID:           taskRequest.ID,
		Command:      taskRequest.Command,
		Args:         taskRequest.Args,
		Status:       "Starting",
		StartTime:    time.Now(),
		AutoRestart:  taskRequest.AutoRestart,
		MaxRestarts:  taskRequest.MaxRestarts,
		RestartCount: 0,
		stopChan:     make(chan struct{}),
		stoppedChan:  make(chan struct{}),
	}

	tm.tasks[task.ID] = task
	go tm.runTask(task)

	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(task)
}

func (tm *TaskManager) stopTaskHandler(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]

	tm.mutex.RLock()
	task, exists := tm.tasks[id]
	tm.mutex.RUnlock()

	if !exists {
		http.Error(w, fmt.Sprintf("Task with ID %s not found", id), http.StatusNotFound)
		return
	}

	if task.Status != "Running" && task.Status != "Restarting" {
		http.Error(w, fmt.Sprintf("Task with ID %s is not running or restarting", id), http.StatusBadRequest)
		return
	}

	close(task.stopChan)
	<-task.stoppedChan

	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(task)
}

func (tm *TaskManager) getTaskStatusHandler(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]

	tm.mutex.RLock()
	task, exists := tm.tasks[id]
	tm.mutex.RUnlock()

	if !exists {
		http.Error(w, fmt.Sprintf("Task with ID %s not found", id), http.StatusNotFound)
		return
	}

	json.NewEncoder(w).Encode(task)
}

func (tm *TaskManager) listTasksHandler(w http.ResponseWriter, r *http.Request) {
	tm.mutex.RLock()
	tasks := make([]*Task, 0, len(tm.tasks))
	for _, task := range tm.tasks {
		tasks = append(tasks, task)
	}
	tm.mutex.RUnlock()

	json.NewEncoder(w).Encode(tasks)
}

// WebSocket upgrader
var upgrader = websocket.Upgrader{
	CheckOrigin: func(r *http.Request) bool {
		return true // Allow all origins for this example
	},
}

// WebSocket handler for FLV streaming and task management
func (tm *TaskManager) handleWebSocket(w http.ResponseWriter, r *http.Request) {
	conn, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		tm.logger.Println("WebSocket upgrade error:", err)
		return
	}
	defer conn.Close()

	for {
		messageType, p, err := conn.ReadMessage()
		if err != nil {
			tm.logger.Println("WebSocket read error:", err)
			return
		}

		var message struct {
			Type    string          `json:"type"`
			Payload json.RawMessage `json:"payload"`
		}

		if err := json.Unmarshal(p, &message); err != nil {
			tm.logger.Println("JSON unmarshal error:", err)
			continue
		}

		switch message.Type {
		case "start_stream":
			var streamInfo struct {
				URL string `json:"url"`
			}
			json.Unmarshal(message.Payload, &streamInfo)
			go tm.forwardFLVStream(conn, streamInfo.URL)
			tm.logger.Printf("Started FLV stream from %s", streamInfo.URL)

		case "start_task":
			var taskInfo Task
			json.Unmarshal(message.Payload, &taskInfo)
			taskInfo.logger = tm.logger
			tm.mutex.Lock()
			tm.tasks[taskInfo.ID] = &taskInfo
			tm.mutex.Unlock()
			go tm.runTask(&taskInfo)

			response, _ := json.Marshal(map[string]string{"status": "Task started"})
			conn.WriteMessage(messageType, response)
			tm.logger.Printf("Task %s started", taskInfo.ID)

		case "stop_task":
			var stopInfo struct {
				ID string `json:"id"`
			}
			json.Unmarshal(message.Payload, &stopInfo)
			tm.mutex.RLock()
			task, exists := tm.tasks[stopInfo.ID]
			tm.mutex.RUnlock()
			if exists {
				close(task.stopChan)
				<-task.stoppedChan
				response, _ := json.Marshal(map[string]string{"status": "Task stopped"})
				conn.WriteMessage(messageType, response)
				tm.logger.Printf("Task %s stopped", stopInfo.ID)
			} else {
				response, _ := json.Marshal(map[string]string{"status": "Task not found"})
				conn.WriteMessage(messageType, response)
				tm.logger.Printf("Attempted to stop non-existent task %s", stopInfo.ID)
			}

		default:
			response, _ := json.Marshal(map[string]string{"status": "Unknown command"})
			conn.WriteMessage(messageType, response)
			tm.logger.Printf("Received unknown command: %s", message.Type)
		}
	}
}

// Function to forward FLV stream from HTTP to WebSocket
func (tm *TaskManager) forwardFLVStream(conn *websocket.Conn, url string) {
	resp, err := http.Get(url)
	if err != nil {
		tm.logger.Printf("Error fetching FLV stream from %s: %v", url, err)
		return
	}
	defer resp.Body.Close()

	// Send FLV header
	header := make([]byte, 13)
	_, err = io.ReadFull(resp.Body, header)
	if err != nil {
		tm.logger.Printf("Error reading FLV header from %s: %v", url, err)
		return
	}
	conn.WriteMessage(websocket.BinaryMessage, header)

	// Forward FLV tags
	buffer := make([]byte, 4096)
	for {
		n, err := resp.Body.Read(buffer)
		if err != nil {
			if err != io.EOF {
				tm.logger.Printf("Error reading FLV stream from %s: %v", url, err)
			}
			break
		}
		err = conn.WriteMessage(websocket.BinaryMessage, buffer[:n])
		if err != nil {
			tm.logger.Printf("Error writing FLV stream to WebSocket: %v", err)
			break
		}
	}
	tm.logger.Printf("Finished forwarding FLV stream from %s", url)
}

// Authentication middleware
func authMiddleware(next http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		token := r.Header.Get("Authorization")
		if token == "" {
			http.Error(w, "Unauthorized: No token provided", http.StatusUnauthorized)
			return
		}

		// In a real-world scenario, you would validate the token here
		// For this example, we'll use a simple static token
		if token != "your-secret-token" {
			http.Error(w, "Unauthorized: Invalid token", http.StatusUnauthorized)
			return
		}

		next.ServeHTTP(w, r)
	}
}

func main() {
	// Set up rotating log file
	logFile := &lumberjack.Logger{
		Filename:   "/var/log/taskmanager/taskmanager.log",
		MaxSize:    10, // megabytes
		MaxBackups: 3,
		MaxAge:     28, // days
		Compress:   true,
	}

	// Create a new logger
	logger := log.New(logFile, "", log.LstdFlags)

	tm := NewTaskManager(logger)
	router := mux.NewRouter()

	router.HandleFunc("/tasks", tm.startTaskHandler).Methods("POST")
	router.HandleFunc("/tasks/{id}", tm.stopTaskHandler).Methods("DELETE")
	router.HandleFunc("/tasks/{id}", tm.getTaskStatusHandler).Methods("GET")
	router.HandleFunc("/tasks", tm.listTasksHandler).Methods("GET")

	// Apply auth middleware to WebSocket endpoint
	router.HandleFunc("/ws", authMiddleware(tm.handleWebSocket))

	// Start the server
	fmt.Println("Server is running on :8080")
	logger.Println("Server started on :8080")
	log.Fatal(http.ListenAndServe(":8080", router))
}
