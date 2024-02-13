package main

import (
	"fmt"
	"sort"
)

func selectionSort(nums []int){
	n := len(nums)

	for i :=0; i < n - 1; i ++ {
		k := i
		for j := i + 1; j < n; j ++ {
			if nums[j] < nums[k] {
				k = j
			}
		}

		nums[i], nums[k] = nums[k], nums[i]
	}
}

func bubbleSort(nums []int){
	for i := len(nums) - 1 ; i > 0; i -- {
		flag := false
		for j := 0; j < i; j ++ {
			if nums[j] > nums[j + 1] {
				nums[j], nums[j+1] = nums[j+1], nums[j]
				flag = true
			}
		}

		if !flag {
			break
		}
	}
}

func insertionSort(nums []int) {
	for i := 1; i < len(nums); i ++ {
		base := nums[i]
		j := i - 1
		for j > 0 && nums[j] > base {
			nums[j+1] = nums[j]
			j--
		}
		nums[j+1] = base
	}
}

type quickSort struct{}

func (q *quickSort)partition(nums []int, left, right int) int {
	med := q.medianThree(nums, left, (left+right)/2, right)
	nums[left], nums[med] = nums[med], nums[left]

	i, j := left, right
	for i < j {
		for i < j && nums[j] >= nums[left] {
			j --
		}
		for i < j && nums[i] <= nums[left] {
			i ++
		}
		nums[i], nums[j] = nums[j], nums[i]
	}
	nums[i], nums[left] = nums[left],  nums[i]
	return i
}

func (q *quickSort) quickSort(nums[]int, left, right int) {
	//if left >= right {
	//	return
	//}
	//pivot := q.partition(nums, left, right)
	//q.quickSort(nums, left, pivot -1)
	//q.quickSort(nums, pivot+1, right)
	for left < right {
		pivot := q.partition(nums, left, right)
		if pivot - left < right - pivot {
			q.quickSort(nums, left, pivot-1)
			left = pivot + 1
		}else{
			q.quickSort(nums, pivot+1, right)
			right = pivot - 1
		}
	}
}

func (q *quickSort) medianThree(nums []int, left, mid, right int) int {
	if (nums[left] < nums[mid]) != (nums[left] < nums[right]) {
		return left
	}else if (nums[mid] < nums[left]) != (nums[mid] < nums[right]) {
		return mid
	}
	return right
}

func merge(nums []int, left, mid, right int){
	tmp := make([]int, right - left +1)
	i, j , k := left, mid +1 , 0
	for i <= mid && j <= right {
		if nums[i] <= nums[j] {
			tmp[k] = nums[i]
			i ++
		}else {
			tmp[k] = nums[j]
			j++
		}
		k ++
	}

	for i <= mid {
        tmp[k] = nums[i]
        i++
        k++
    }
    for j <= right {
        tmp[k] = nums[j]
        j++
        k++
    }

	for k := 0; k < len(tmp); k ++ {
		nums[left + k] = tmp[k]
	}
}

func mergeSort(nums []int, left, right int){
	if left >= right {
		return
	}

	mid := (left + right) / 2
	mergeSort(nums, left, mid)
	mergeSort(nums, mid+1, right)
	merge(nums, left, mid, right)
}


func bucketSort(nums []float64) {
	k := len(nums) / 2
	buckets := make([][]float64, k)
	for i := 0; i < k ; i ++ {
		buckets[i] = make([]float64, 0)
	}

	for _, num := range nums {
		i := int(num * float64(k))
		buckets[i] = append(buckets[i], num)
	}

    for i := 0; i < k; i++ {
        sort.Float64s(buckets[i])
    }
    i := 0
    for _, bucket := range buckets {
        for _, num := range bucket {
            nums[i] = num
            i++
        }
    }	
}

func main(){
	nums := []int{9, 12, 4, 4, 3, 5, 6, 8}
	selectionSort(nums)
	fmt.Printf("selectionSort:\n%+v\n", nums)

	bubbleSort(nums)
	fmt.Printf("bubbleSort:\n%+v\n", nums)

	insertionSort(nums)
	fmt.Printf("insertionSort:\n%+v\n", nums)

	qs := quickSort{}
	qs.quickSort(nums, 0, len(nums)-1)
	fmt.Printf("quickSort:\n%+v\n", nums)

	mergeSort(nums, 0, len(nums)-1)
	fmt.Printf("mergeSort:\n%+v\n", nums)

	numsFloat := []float64{0.1, 0.5, 0.43, 0.23, 0.45, 0.67, 0.99, 0.8}
	bucketSort(numsFloat)
	fmt.Printf("bucketSort:\n%+v\n", numsFloat)
}