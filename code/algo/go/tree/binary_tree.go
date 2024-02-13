package main

import (
	"container/list"

)

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}


func NewTreeNode(v int) *TreeNode {
	return &TreeNode{
		Left: nil,
		Right: nil,
		Val: v,
	}
}



func levelOrder(root *TreeNode) []any{
	queue := list.New()
	queue.PushBack(root)
	nums := make([]any, 0)
	for queue.Len() > 0 {
		node := queue.Remove(queue.Front()).(*TreeNode)
		nums = append(nums, node.Val)
		if node.Left != nil {
			queue.PushBack(node.Left)
		}
		if node.Right != nil {
			queue.PushBack(node.Right)
		}
	}
	return nums
}

type binarySearchTree struct{
	root *TreeNode
}

func (bst *binarySearchTree) search(num int) *TreeNode {
    node := bst.root
    for node != nil {
        if node.Val < num {
            node = node.Right
        } else if node.Val > num {
            node = node.Left
        } else {
            break
        }
    }
    return node
}

func (bst *binarySearchTree) insert(num int) {
	cur := bst.root
	if cur == nil {
		bst.root = NewTreeNode(num)
		return
	}

	var pre *TreeNode = nil
	for cur != nil {
		if cur.Val == num {
			return
		}
		pre = cur
		if cur.Val < num {
			cur = cur.Right
		}else{
			cur = cur.Left
		}
	}

	node := NewTreeNode(num)
	if pre.Val < num {
		pre.Right = node
	}else{
		pre.Left = node
	}
}


func (bst *binarySearchTree)remove(num int){
	cur := bst.root
	if cur == nil {
		return
	}

	var pre *TreeNode = nil
	for cur != nil {
		if cur.Val == num {
			break
		}
		pre = cur
		if cur.Val < num {
			cur = cur.Right
		}else{
			cur = cur.Left
		}
	}
	if cur == nil {
		return
	}

	if cur.Left == nil || cur.Right == nil {
		var child *TreeNode = nil
		if cur.Left != nil {
			child = cur.Left
		}else {
			child = cur.Right
		}

		if cur != bst.root {
			if pre.Left == cur {
				pre.Left = child
			}else{
				pre.Right = child
			}
		}else {
			bst.root = child
		}
	}else {
		tmp := cur.Right
		for tmp.Left != nil {
			tmp = tmp.Left
		}
		bst.remove(tmp.Val)
		cur.Val = tmp.Val
	}
}

type arrayBinaryTree struct {
	tree []any
}

func newArrayBinaryTree(arr []any) *arrayBinaryTree {
	return &arrayBinaryTree{
		tree: arr,
	}
}

func (abt *arrayBinaryTree) size() int {
	return len(abt.tree)
}


func (abt *arrayBinaryTree)val(i int)any{
	if i < 0 || i >= abt.size() {
		return nil
	}
	return abt.tree[i]
}

func (abt *arrayBinaryTree)left(i int) int {
	return  2*i + 1
}

func (abt *arrayBinaryTree)right(i int)int{
	return 2*i + 2
}

func (abt *arrayBinaryTree)parent(i int) int {
	return (i - 1) / 2
}

func (abt *arrayBinaryTree)levelOrder()[]any{
	var res []any
	for i := 0; i < abt.size(); i ++ {
		if abt.val(i) != nil {
			res = append(res, abt.val(i))
		}
	}
	return res
}

func (abt *arrayBinaryTree)dfs(i int, order string, res *[]any){
	if abt.val(i) == nil {
		return
	}

	if order == "pre" {
		*res = append(*res, abt.val(i))
	}
	abt.dfs(abt.left(i), order, res)
	if order == "in" {
		*res = append(*res, abt.val(i))
	}
	abt.dfs(abt.right(i), order, res)
	if order == "post" {
		*res = append(*res, abt.val(i))
	}
}

func (abt *arrayBinaryTree)preOrder()[]any{
	var res []any
	abt.dfs(0, "pre", &res)
	return res
}
func (abt *arrayBinaryTree)inOrder() [] any{
	var res []any
	abt.dfs(0, "in", &res)
	return res
}
func (abt *arrayBinaryTree)postOrder() [] any{
	var res []any
	abt.dfs(0, "post", &res)
	return res
}

func (abt *arrayBinaryTree)search(num int) int {
	idx := 0
	node := abt.val(idx)
	for node != nil {
		if node.(int) < num {
			idx = abt.right(idx)
		}else if node.(int) > num {
			idx = abt.left(idx)	
		}else{
			break
		}
		node = abt.val(idx)
	}
	return idx
}


func main(){
	n1 := NewTreeNode(1)
	n2 := NewTreeNode(2)
	n3 := NewTreeNode(3)
	n4 := NewTreeNode(4)
	n5 := NewTreeNode(5)

	n1.Left = n2
	n1.Right = n3
	n2.Left = n4
	n2.Right = n5
}