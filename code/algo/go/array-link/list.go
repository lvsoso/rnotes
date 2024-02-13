package main

func show(arr []int){
	for i := range arr {
		print(arr[i])
		print(" " )
	}
	println()
}

type myList struct {
	arrCapacity int
	arr []int
	arrSize int
	extendRate int
}

func newMyList() *myList {
	return &myList{
		arrCapacity: 10,
		arr: make([]int, 10),
		arrSize: 0,
		extendRate: 2,
	}
}

func (l *myList) size() int {
	return l.arrSize
}

func (l *myList)capacity() int {
	return l.arrCapacity
}

func (l *myList)get(index int)int {
	if index < 0 || index >= l.arrSize {
		panic("out of index")
	}
	return l.arr[index]
}

func (l *myList)set(num, index int){
	if index < 0 || index >= l.arrSize {
		panic("out of index")
	}
	l.arr[index] = num
}

func (l *myList)add(num int){
	if l.arrSize == l.arrCapacity {
		l.extendCapacity()
	}

	l.arr[l.arrSize] = num
	l.arrSize ++
}

func (l *myList)insert(num, index int){
	if index < 0 || index >= l.arrSize {
		panic("out of index")
	}

	if l.arrSize == l.arrCapacity {
		l.extendCapacity()
	}

	for j := l.arrSize - 1; j >= index; j -- {
		l.arr[j+1] = l.arr[j]
	}

	l.arr[index] = num
	l.arrSize ++
}

func (l *myList)remove(index int)int {
	if index < 0 || index >= l.arrSize {
		panic("out of index")
	}

	num := l.arr[index]
	for j := index; j < l.arrSize - 1; j ++ {
		l.arr[j] = l.arr[j + 1]
	}
	l.arrSize --

	return num
}

func (l *myList) extendCapacity() {
	l.arr = append(l.arr, make([]int, l.arrCapacity * (l.extendRate - 1))...)
	l.arrCapacity = len(l.arr)
}

func (l *myList) toArray() []int{
	return l.arr[:l.arrSize]
}

func main(){
	nums := []int{1, 2, 3, 4, 5}

	show(nums)

	nums =  append(nums,  9)
	show(nums)

	nums = append(nums[:3], append([]int{6}, nums[3:]...)... )
	show(nums)

	nums = append(nums[:3],  nums[4:]...)
	show(nums)
}