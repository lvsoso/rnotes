package main

import (
	"log"

	"queue/tasks"

	"github.com/hibiken/asynq"
)

const redisAddr = "127.0.0.1:7617"

func main() {
	srv := asynq.NewServer(
		// asynq.RedisClusterClientOpt{
		// 	Addrs:    []string{redisAddr},
		// 	Password: "123456",
		// },
		asynq.RedisClientOpt{
			Addr:     redisAddr,
			Password: "123456",
		},
		asynq.Config{
			// Specify how many concurrent workers to use
			Concurrency: 10,
			// Optionally specify multiple queues with different priority.
			Queues: map[string]int{
				"critical": 6,
				"default":  3,
				"low":      1,
			},
			// See the godoc for other configuration options
		},
	)

	// mux maps a type to a handler
	mux := asynq.NewServeMux()
	mux.HandleFunc(tasks.TypeEmailDelivery, tasks.HandleEmailDeliveryTask)
	mux.Handle(tasks.TypeImageResize, tasks.NewImageProcessor())
	// ...register other handlers...

	if err := srv.Run(mux); err != nil {
		log.Fatalf("could not run server: %v", err)
	}
}
