package main

import (
	"container/heap"
	"fmt"
)


type initHeap []any

func (h *initHeap) Push(x any) {
	*h = append(*h, x.(int))
}

func (h *initHeap) Pop() any {
	last := (*h)[len(*h) - 1]
	*h = (*h)[:len(*h) - 1]
	return last
}

func (h *initHeap) Len() int {
	return len(*h)
}

func (h *initHeap) Less(i, j int) bool {
	return (*h)[i].(int) > (*h)[j].(int)
}

func (h *initHeap) Swap(i, j int) {
	(*h)[i], (*h)[j] = (*h)[j], (*h)[i]
}

func (h *initHeap)Top() any {
	return (*h)[0]
}


func testHeap(){
	maxHeap := &initHeap{}
	heap.Init(maxHeap)

	heap.Push(maxHeap, 1)
	heap.Push(maxHeap, 3)
	heap.Push(maxHeap, 2)
	heap.Push(maxHeap, 4)
	heap.Push(maxHeap, 5)

	top := maxHeap.Top()
	fmt.Printf("Top : %d\n", top)

	println(heap.Pop(maxHeap).(int))
	println(heap.Pop(maxHeap).(int))
	println(heap.Pop(maxHeap).(int))
	println(heap.Pop(maxHeap).(int))
	println(heap.Pop(maxHeap).(int))

	size := len(*maxHeap)
	fmt.Printf("Len %d\n", size)

	isEmpty := len(*maxHeap) == 0
	fmt.Printf("IsEmpty %t\n", isEmpty)
}

func main(){
	testHeap()
}