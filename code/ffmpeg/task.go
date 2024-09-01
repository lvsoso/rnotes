package main

import (
	"fmt"
	"os/exec"
	"sync"
	"time"
)

type Task struct {
	ID          string
	Command     string
	Args        []string
	cmd         *exec.Cmd
	Status      string
	StartTime   time.Time
	StopTime    time.Time
	Error       error
	stopChan    chan struct{}
	stoppedChan chan struct{}
}

type TaskManager struct {
	tasks map[string]*Task
	mutex sync.RWMutex
}

func NewTaskManager() *TaskManager {
	return &TaskManager{
		tasks: make(map[string]*Task),
	}
}

func (tm *TaskManager) StartTask(id, command string, args ...string) error {
	tm.mutex.Lock()
	defer tm.mutex.Unlock()

	if _, exists := tm.tasks[id]; exists {
		return fmt.Errorf("task with ID %s already exists", id)
	}

	task := &Task{
		ID:          id,
		Command:     command,
		Args:        args,
		Status:      "Starting",
		StartTime:   time.Now(),
		stopChan:    make(chan struct{}),
		stoppedChan: make(chan struct{}),
	}

	tm.tasks[id] = task

	go func() {
		defer close(task.stoppedChan)
		task.cmd = exec.Command(task.Command, task.Args...)
		task.Status = "Running"

		err := task.cmd.Start()
		if err != nil {
			task.Status = "Error"
			task.Error = err
			return
		}

		done := make(chan error)
		go func() {
			done <- task.cmd.Wait()
		}()

		select {
		case err := <-done:
			if err != nil {
				task.Status = "Error"
				task.Error = err
			} else {
				task.Status = "Completed"
			}
		case <-task.stopChan:
			if err := task.cmd.Process.Kill(); err != nil {
				task.Status = "Error"
				task.Error = err
			} else {
				task.Status = "Stopped"
			}
			<-done
		}

		task.StopTime = time.Now()
	}()

	return nil
}

func (tm *TaskManager) StopTask(id string) error {
	tm.mutex.RLock()
	task, exists := tm.tasks[id]
	tm.mutex.RUnlock()

	if !exists {
		return fmt.Errorf("task with ID %s not found", id)
	}

	if task.Status != "Running" {
		return fmt.Errorf("task with ID %s is not running", id)
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

