package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

var taskManager *TaskManager

// Command
// ffmpeg -i input.mp4 -threads 4 -an -s "394x?" -aspect 16:9 -c:v libx264 -f flv rtmp://127.0.0.1:1935/live/test110
func Command(pullURL, pushURL string) []string {
	return []string{
		"-i",
		pullURL,
		"-threads",
		"4",
		"-an",
		"-s",
		"394x?",
		" -aspect",
		" 16:9",
		" -c:v",
		" libx264",
		" -f",
		" flv",
		pushURL,
	}
}

func taskHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != "POST" {
		http.Error(w, "Method Not Allowed", http.StatusMethodNotAllowed)
		return
	}

	var task Task
	err := json.NewDecoder(r.Body).Decode(&task)
	if err != nil {
		log.Printf("Error decoding JSON: %v\n", err)
		http.Error(w, "Invalid JSON", http.StatusBadRequest)
		return
	}

	taskManager.StartTask(task.ID, task.Command, task.Args...)

	w.WriteHeader(http.StatusCreated)
	fmt.Fprintf(w, "Task published successfully")
}

func main() {
	taskManager = NewTaskManager()

	http.HandleFunc("/publish-task", taskHandler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
