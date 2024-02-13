package main

import (
	"math/rand"
)

func randomAccess(nums []int)(randomNum int){
	randomIndex := rand.Intn(len(nums))
	randomNum = nums[randomIndex]
	return
}

func insert(nums []int, num int, index int){
	l := len(nums)
    //	if index >= l {
    //		
    //	}
   for i := l-1; i > index ; i-- {
		nums[i] = nums[i-1]
	}
	nums[index] = num
}

func remove(nums []int, index int){
	for i := index; i < len(nums)  - 1; i ++ {
		nums[i] =  nums[i + 1]
	}
}

func find(nums []int, target int)(index int){
	index = -1
	for i := 0; i < len(nums); i ++ {
		if nums[i] == target {
			index = i
			return
		}
	}
	return
}


func extend(nums []int, enlarge int)[]int {
	res := make([]int, len(nums) + enlarge)
	for i, num := range nums {
		res[i] = num
	}
	return res
}

func show(arr []int){
	for i := range arr {
		print(arr[i])
	}
	println()
}

func main(){
	var arr = []int{1, 2, 3, 4, 5}
	println(randomAccess(arr))

	show(arr)
	insert(arr, 9, 2)
	show(arr)

	remove(arr, 2)
	show(arr)

	println(find(arr, 3))
	
	arr = extend(arr, 10)
	println(len(arr))
	println(cap(arr))

}
