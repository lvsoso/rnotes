package main

import (
	"fmt"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func NewListNode(val int) *ListNode {
	return &ListNode{
		Val:  val,
		Next: nil,
	}
}

func show(head *ListNode) {
	node := head
	for {
		if node == nil {
			break
		}
		print(node.Val)
		print("    ")
		node = node.Next
	}
	println()
}


func insertNode(n0 *ListNode, p *ListNode) {
	n1 := n0.Next
	p.Next = n1
	n0.Next = p
}


func removeItem(n0 *ListNode){
	if n0.Next == nil {
		return
	}

	p := n0.Next
	n1 := p.Next
	n0.Next = n1
}


func access(head *ListNode, index int) *ListNode {
	for i :=  0; i < index; i ++ {
		if head == nil {
			return nil
		}
		head = head.Next
	}
	return head
}

func findNode(head *ListNode, target int) int {
	index := 0
	for head != nil {
		if head.Val ==  target {
			return index
		}
		head = head.Next
		index ++
	}
	return -1
}

func main() {
	n0 := NewListNode(1)
	n1 := NewListNode(2)
	n2 := NewListNode(3)
	n3 := NewListNode(4)
	n4 := NewListNode(5)
	n0.Next = n1
	n1.Next = n2
	n2.Next = n3
	n3.Next = n4
	show(n0)

	n000 := NewListNode(1223)
	insertNode(n3, n000)
	show(n0)
	
	removeItem(n3)
	show(n0)

	node := access(n0, 4)
	fmt.Printf("%+v\n",node)

	idx := findNode(n0, 2)
	fmt.Println(idx)
}
