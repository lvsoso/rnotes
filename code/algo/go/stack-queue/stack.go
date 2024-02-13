package main

import "container/list"


type linkedListStack struct {
	data *list.List
}


func newLinkedListStack() *linkedListStack {
	return &linkedListStack{
		data: list.New(),
	}
}

func (s *linkedListStack) push(value int){
	s.data.PushBack(value)
}

func(s *linkedListStack)pop() any {
	if s.isEmpty() {
		return nil
	}

	e := s.data.Back()
	s.data.Remove(e)
	return e.Value
}

func (s *linkedListStack) peek() any {
	if s.isEmpty() {
		return nil
	}

	e := s.data.Back()
	return e.Value
}

func (s *linkedListStack) size() int {
	return  s.data.Len()
}

func (s *linkedListStack) isEmpty() bool {
	return s.data.Len() == 0
}

func (s *linkedListStack) toList() *list.List {
	return s.data
}

func (s *linkedListStack)show(){
	start := s.data.Front()
	for start != nil {
		print(start.Value.(int))
		print(" ")
		start = start.Next()
	}
	println()
}


type arrayStack struct {
	data []int 
}

func newArrayStack() *arrayStack {
	return &arrayStack{
		data: make([]int, 0, 16),
	}
}

func (s *arrayStack) size() int {
	return len(s.data)
}

func (s *arrayStack) isEmpty() bool {
	return s.size() == 0
}

func (s *arrayStack) push(v int) {
	s.data = append(s.data, v)
}

func (s *arrayStack) pop() any {
	val := s.peek()
	s.data = s.data[:len(s.data) - 1]
	return val
}

func (s *arrayStack)peek() any {
	if s.isEmpty(){
		return nil
	}
	val := s.data[len(s.data) - 1]
	return val
}

func (s *arrayStack) toSlice()  []int {
	return s.data
}

func main(){
	stack := newLinkedListStack()

	stack.push(1)
	stack.push(2)
	stack.push(3)
	stack.push(4)
	stack.push(5)
	stack.push(6)

	stack.show()

	stack.pop()
	stack.show()
}