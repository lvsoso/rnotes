package main

import (
	"fmt"
	"testing"
	"time"
)

func TestXxx(t *testing.T) {
	tm := NewTaskManager()

	err := tm.StartTask("task1", "ping", "baidu.com")
	if err != nil {
		fmt.Println("Error starting task:", err)
		return
	}

	time.Sleep(5 * time.Second)

	status, err := tm.GetTaskStatus("task1")
	if err != nil {
		fmt.Println("Error getting task status:", err)
	} else {
		fmt.Println("Task status:", status)
	}

	err = tm.StopTask("task1")
	if err != nil {
		fmt.Println("Error stopping task:", err)
	}

	tasks := tm.ListTasks()
	for _, task := range tasks {
		fmt.Printf("Task ID: %s, Status: %s, Command: %s\n", task.ID, task.Status, task.Command)
	}
}
