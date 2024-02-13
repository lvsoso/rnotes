package main

import (
	"fmt"
	"strconv"
	"strings"

)


type pair struct {
	key int
	val string
}

type arrayHashMap struct {
	buckets []*pair
}


func newArrayHashMap() *arrayHashMap{
	buckets := make([]*pair, 100)
	return &arrayHashMap{buckets: buckets}
}

func (a *arrayHashMap) hashFunc(key int)int{
	index := key %100
	return index
}


func (a *arrayHashMap)get(key int) string{
	index := a.hashFunc(key)
	pair := a.buckets[index]
	if pair == nil {
		return "Not Found"
	}
	return pair.val
}

func (a *arrayHashMap)put(key int, val string){
	pair := &pair{key:key, val: val}
	index := a.hashFunc(key)
	a.buckets[index] = pair
}

func (a *arrayHashMap)remove(key int){
	index := a.hashFunc(key)
	a.buckets[index] = nil
}

func (a *arrayHashMap) keySet() []int {
    var keys []int
    for _, pair := range a.buckets {
        if pair != nil {
            keys = append(keys, pair.key)
        }
    }
    return keys
}

func (a *arrayHashMap) valueSet() []string {
    var values []string
    for _, pair := range a.buckets {
        if pair != nil {
            values = append(values, pair.val)
        }
    }
    return values
}

func (a *arrayHashMap) print() {
    for _, pair := range a.buckets {
        if pair != nil {
            fmt.Println(pair.key, "->", pair.val)
        }
    }
}


type hashMapChaining struct {
	size int
	capacity int
	loadThres float64
	extendRatio int
	buckets [][]pair
}


func newHashMapChaining() *hashMapChaining {
	buckets := make([][]pair, 4)
	for i := 0; i < 4; i ++ {
		buckets[i] = make([]pair, 0)
	}
	return &hashMapChaining{
		size: 0,
		capacity: 4,
		loadThres: 2.0/3.0,
		extendRatio: 2,
		buckets: buckets,
	}
}


func (m *hashMapChaining) hashFunc(key int) int {
	return key % m.capacity
}


func (m *hashMapChaining) loadFactor() float64 {
    return float64(m.size) / float64(m.capacity)
}


func (m *hashMapChaining)get(key int) string {
	idx := m.hashFunc(key)
	bucket := m.buckets[idx]
	for _, p := range bucket {
		if p.key == key {
			return p.val
		}
	}
	return ""
}

func (m *hashMapChaining) put(key int, val string){
	if m.loadFactor() > m.loadThres {
		m.extend()
	}

	idx := m.hashFunc(key)
	for i := range m.buckets[idx]{
		if m.buckets[idx][i].key == key {
			m.buckets[idx][i].val = val
			return
		}
	}

	p := pair{
		key:key,
		val: val,
	}
	m.buckets[idx] = append(m.buckets[idx], p)
	m.size += 1
}


func (m *hashMapChaining) remove(key int){
	idx := m.hashFunc(key)
	for i,p := range m.buckets[idx]{
		if p.key == key {
			m.buckets[idx] = append(m.buckets[idx][:i], m.buckets[idx][i+1:]...)
			m.size -= 1
			break
		}
	}	
}


func (m *hashMapChaining)extend(){
	tmpBuckets := make([][]pair, len(m.buckets))
	for i := 0; i < len(m.buckets); i ++ {
		tmpBuckets[i] = make([]pair, len(m.buckets[i]))
		copy(tmpBuckets[i], m.buckets[i])
	}

	m.capacity *= m.extendRatio
    m.buckets = make([][]pair, m.capacity)
    for i := 0; i < m.capacity; i++ {
        m.buckets[i] = make([]pair, 0)
    }
    m.size = 0
    for _, bucket := range tmpBuckets {
        for _, p := range bucket {
            m.put(p.key, p.val)
        }
    }
}

func (m *hashMapChaining) print() {
    var builder strings.Builder

    for _, bucket := range m.buckets {
        builder.WriteString("[")
        for _, p := range bucket {
            builder.WriteString(strconv.Itoa(p.key) + " -> " + p.val + " ")
        }
        builder.WriteString("]")
        fmt.Println(builder.String())
        builder.Reset()
    }
}




type hashMapOpenAddressing struct {
	size int
	capacity int
	loadThres float64
	extendRatio int
	buckets []pair
	removed pair
}

func newHashMapOpenAddressing() *hashMapOpenAddressing {
	buckets := make([]pair, 4)
	return &hashMapOpenAddressing{
		size : 0,
		capacity: 4,
		loadThres: 2.0/3.0,
		extendRatio: 2,
		buckets: buckets,
		removed: pair{
			key: -1,
			val: "-1",
		},
	}
}

func (m *hashMapOpenAddressing) hashFunc(key int) int {
    return key % m.capacity
}

func (m *hashMapOpenAddressing) loadFactor() float64 {
    return float64(m.size) / float64(m.capacity)
}


func (m *hashMapOpenAddressing)get(key int) string {
	idx := m.hashFunc(key)
	for i := 0; i < m.capacity; i ++ {
		j := (idx + i) % m.capacity
		if m.buckets[j] == (pair{}){
			return ""
		}

		if m.buckets[j].key == key && m.buckets[j] != m.removed {
			return m.buckets[j].val
		}
	}

	return ""
}

func (m *hashMapOpenAddressing)put(key int, val string){
	if m.loadFactor() > m.loadThres {
		m.extend()
	}
	idx := m.hashFunc(key)
	for i := 0; i < m.capacity; i ++ {
		j := (idx + i) % m.capacity
		if m.buckets[j] == (pair{}) || m.buckets[j] == m.removed {
            m.buckets[j] = pair{
                key: key,
                val: val,
            }
            m.size += 1
            return
        }

		if m.buckets[j].key == key {
			m.buckets[j].val = val
			return
		}
	}
}

func (m *hashMapOpenAddressing)remove(key int){
	idx := m.hashFunc(key)
	for i := 0; i < m.capacity; i ++ {
		j := (idx + i)%m.capacity
		if m.buckets[j] == (pair{}) {
			return
		}

		if m.buckets[j].key == key {
			m.buckets[j] = m.removed
			m.size -= 1
		}
	}
}

func (m *hashMapOpenAddressing)extend(){
	tmpBuckets := make([]pair, len(m.buckets))
	copy(tmpBuckets, m.buckets)

	m.capacity *= m.extendRatio
	m.buckets = make([]pair, m.capacity)
	m.size = 0
	
	for _, p := range tmpBuckets{
		if p != (pair{}) && p != m.removed {
			m.put(p.key, p.val)
		}
	}
}

func (m *hashMapOpenAddressing) print() {
    for _, p := range m.buckets {
        if p != (pair{}) {
            fmt.Println(strconv.Itoa(p.key) + " -> " + p.val)
        } else {
            fmt.Println("nil")
        }
    }
}

func main(){
	hashMap := newHashMapChaining()
	hashMap.put(1, "asdsd")
	hashMap.put(2, "asdsd")
	hashMap.put(3, "asdsd")
	hashMap.put(4, "asdsd")

	hashMap.print()
	println("-------------------------------------")
	hashMap.put(4, "as")
	hashMap.print()

	println("------------------------------------- +++++++++++++++++++++++++++++")

	hashMapOA := newHashMapOpenAddressing()
	hashMapOA.put(1, "abc")
	hashMapOA.put(2, "abc")
	hashMapOA.put(3, "abc")
	hashMapOA.print()
	println("-------------------------------------")

	hashMapOA.put(4, "abc")
	hashMapOA.put(5, "abc")
	hashMapOA.print()
	println("-------------------------------------")

	hashMapOA.remove(4)
	hashMapOA.print()
}