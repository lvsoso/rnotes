package main

import (
	"fmt"

)


type MaxHeap struct {
	data []any
}


func newMaxHeap(nums []any) *MaxHeap {
	h := &MaxHeap{data: nums}
	for i := h.parent(len(h.data ) - 1); i >= 0; i -- {
		h.siftDown(i)
	}
	return h
}

func (h *MaxHeap) left(i int)int{
	return 2* i + 1
}

func (h *MaxHeap)right(i int)int{
	return 2*i + 2
}

func (h *MaxHeap)parent(i int)int{
	return (i - 1) / 2
}

func(h *MaxHeap)peek() any {
	return h.data[0]
}

func (h *MaxHeap)push(val any) {
	h.data = append(h.data, val)
	h.siftUp(len(h.data) - 1)
}

func (h *MaxHeap)siftUp(i int){
	for true {
		p := h.parent(i)
		if p < 0 || h.data[i].(int) <= h.data[p].(int){
			break
		}
		h.swap(i, p)
		i = p
	}
}

func (h *MaxHeap)swap(i, p int){
	h.data[i], h.data[p] = h.data[p], h.data[i]
}

func (h *MaxHeap)pop() any {
	if h.isEmpty() {
		fmt.Println("error")
		return nil
	}

	h.swap(0, h.size() - 1)

	val := h.data[len(h.data) - 1]
	h.data = h.data[:len(h.data) - 1]
	h.siftDown(0)
	return val
}

func (h *MaxHeap) siftDown(i int){
	for true {
		l, r, max := h.left(i), h.right(i), i
		if l < h.size() && h.data[l].(int) > h.data[max].(int) {
			max = l
		}
		if r < h.size() && h.data[r].(int) > h.data[max].(int) {
			max = r
		}
		if max == i {
			break
		}
		h.swap(i, max)
		i = max
	}
}

func (h *MaxHeap)size() int {
	return len(h.data)
}
func (h *MaxHeap)isEmpty() bool {
	return h.size() == 0
}

func main(){}