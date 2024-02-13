package main

import (
	"container/list"
	"fmt"
)


type linkedListDeque struct {
	data *list.List
}

func newLinkedListDeque() *linkedListDeque {
	return &linkedListDeque{
		data: list.New(),
	}
}

func (s *linkedListDeque) pushFirst(value any) {
	s.data.PushFront(value)
}

func (s *linkedListDeque)pushLast(value any){
	s.data.PushBack(value)
}

func (s *linkedListDeque)popFirst() any {
	if s.isEmpty() {
		return nil
	}
	e := s.data.Front()
	s.data.Remove(e)
	return e.Value
}

func (s *linkedListDeque)popLast() any {
	if s.isEmpty(){
		return nil
	}
	e := s.data.Back()
	s.data.Remove(e)
	return e.Value
}

func (s *linkedListDeque)peekFirst() any{
	if s.isEmpty(){
		return nil
	}
	return s.data.Front().Value
}
func (s *linkedListDeque)peekLast() any{
	if s.isEmpty() {
		return nil
	}
	return s.data.Back().Value
}

func (s *linkedListDeque)size()int{
	return s.data.Len()
}

func (s *linkedListDeque)isEmpty() bool{
	return s.data.Len() == 0
}

func (s *linkedListDeque) toList() *list.List{
	return s.data
}

type arrayDeque struct {
	nums []int
	front int
	queSize int
	queCapacity int
}

func newArrayDeque(queCapacity int)*arrayDeque {
	return &arrayDeque{
		nums: make([]int, queCapacity),
		queCapacity: queCapacity,
		front: 0,
		queSize: 0,
	}
}

func (q *arrayDeque)size() int{
	return q.queSize
}

func (q *arrayDeque)isEmpty() bool {
	return q.queSize == 0
}

func (q *arrayDeque)index(i int) int{
	return (i + q.queCapacity) % q.queCapacity
}

func (q *arrayDeque)pushFirst(num int) {
	if q.queSize == q.queCapacity {
		fmt.Println("queue is fulled")
		return
	}

	q.front = q.index(q.front - 1)
	q.nums[q.front] = num
	q.queSize ++
}

func (q *arrayDeque)pushLast(num int) {
	if q.queSize == q.queCapacity {
		fmt.Println("queue is fulled")
		return
	}
	rear := q.index(q.front + q.queSize)
	q.nums[rear] = num
	q.queSize ++
}

func (q *arrayDeque) popFirst() any {
    num := q.peekFirst()
    q.front = q.index(q.front + 1)
    q.queSize--
    return num
}

func (q *arrayDeque) popLast() any {
    num := q.peekLast()
    q.queSize--
    return num
}

func (q *arrayDeque) peekFirst() any {
    if q.isEmpty() {
        return nil
    }
    return q.nums[q.front]
}

func (q *arrayDeque) peekLast() any {
    if q.isEmpty() {
        return nil
    }
    last := q.index(q.front + q.queSize - 1)
    return q.nums[last]
}

func (q *arrayDeque) toSlice() []int {
    res := make([]int, q.queSize)
    for i, j := 0, q.front; i < q.queSize; i++ {
        res[i] = q.nums[q.index(j)]
        j++
    }
    return res
}

func main() {

}
