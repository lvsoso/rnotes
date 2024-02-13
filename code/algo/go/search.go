package main

func binarySearch(nums []int, target int) int {
	i, j := 0, len(nums) -1
	for i <= j {
		m := i + (j - i)/2
		if nums[m] < target {
			i = m + 1
		}else if nums[m] > target {
			j = m - 1
		} else {
			return m
		}
	}
	return -1
}


func binarySearchLCRO(nums []int, target int) int {
    i, j := 0, len(nums)
    for i < j {
        m := i + (j-i)/2
        if nums[m] < target { 
            i = m + 1
        } else if nums[m] > target {
            j = m
        } else { 
            return m
        }
    }
    return -1
}

func binarySearchInsertionSimple(nums []int, target int) int {
    i, j := 0, len(nums)-1
    for i <= j {
        m := i + (j-i)/2
        if nums[m] < target {
            i = m + 1
        } else if nums[m] > target {
            j = m - 1
        } else {
            return m
        }
    }
    return i
}

func binarySearchInsertion(nums []int, target int) int {
    i, j := 0, len(nums)-1
    for i <= j {
        m := i + (j-i)/2
        if nums[m] < target {
            i = m + 1
        } else if nums[m] > target {
            j = m - 1
        } else {
            j = m - 1
        }
    }
    return i
}


func main(){

}