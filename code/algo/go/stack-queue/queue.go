package main

import (
	"container/list"

)

type linkdListQueue struct {
	data *list.List
}

func newLinkedListQueue() *linkdListQueue {
	return &linkdListQueue{
		data: list.New(),
	}
}


func (s *linkdListQueue) push(value any) {
	s.data.PushBack(value)
}

func (s *linkdListQueue) pop()any{
	if s.isEmpty(){
		return nil
	}

	e := s.data.Front()
	s.data.Remove(e)
	return e.Value
}

func (s *linkdListQueue)peek() any {
	if s.isEmpty() {
		return nil
	}
	return s.data.Front().Value
}

func (s *linkdListQueue) size() int {
	return s.data.Len()
}

func (s *linkdListQueue) isEmpty() bool {
	return s.data.Len() == 0
}

func (s *linkdListQueue) toList() *list.List {
	return s.data
}

type arrayQueue struct {
	nums []int
	front int
	queSize int
	queCapacity int
}

func newArrayQueue(queCapacity int) *arrayQueue {
	return &arrayQueue{
		nums: make([]int, queCapacity),
		front: 0,
		queSize: 0,
		queCapacity: queCapacity,
	}
}

func (q *arrayQueue) size() int{
	return q.queSize
}

func (q *arrayQueue) isEmpty() bool {
	return q.queSize == 0
}

func (q *arrayQueue) push(num int) {
	if q.queSize == q.queCapacity {
		return
	}

	rear := (q.front + q.queSize) % q.queCapacity
	q.nums[rear] = num
	q.queSize++
}

func (q *arrayQueue) peek() any {
	if q.isEmpty(){
		return nil
	}
	return q.nums[q.front]
}

func (q *arrayQueue) pop() any{
	num := q.peek()
	q.front = (q.front + 1) % q.queCapacity
	q.queSize --
	return num
}

func (q *arrayQueue) toSlice() []int{
	rear := (q.front + q.queSize)
	if rear >= q.queCapacity {
		rear %= q.queCapacity
		return append(q.nums[q.front:], q.nums[:rear]...)
	}
	return q.nums[q.front:rear]
}
//func (q *arrayQueue) () {}

func main(){

}