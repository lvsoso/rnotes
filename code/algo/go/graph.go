package main

import (
	"fmt"
	"strings"
	"strconv"
)

type graphAdjMat struct {
    vertices []int
    adjMat [][]int
}

func newGraphAdjMat(vertices []int, edges [][]int) *graphAdjMat {
    n := len(vertices)
    adjMat := make([][]int, n)
    for i := range adjMat {
        adjMat[i] = make([]int, n)
    }
    g := &graphAdjMat{
        vertices: vertices,
        adjMat:   adjMat,
    }
    for i := range edges {
        g.addEdge(edges[i][0], edges[i][1])
    }
    return g
}

func (g *graphAdjMat) size() int {
    return len(g.vertices)
}

func (g *graphAdjMat) addVertex(val int) {
    n := g.size()
    g.vertices = append(g.vertices, val)
    newRow := make([]int, n)
    g.adjMat = append(g.adjMat, newRow)
    for i := range g.adjMat {
        g.adjMat[i] = append(g.adjMat[i], 0)
    }
}

func (g *graphAdjMat) removeVertex(index int) {
    if index >= g.size() {
        return
    }
    g.vertices = append(g.vertices[:index], g.vertices[index+1:]...)
    g.adjMat = append(g.adjMat[:index], g.adjMat[index+1:]...)
    for i := range g.adjMat {
        g.adjMat[i] = append(g.adjMat[i][:index], g.adjMat[i][index+1:]...)
    }
}

func (g *graphAdjMat) addEdge(i, j int) {
    if i < 0 || j < 0 || i >= g.size() || j >= g.size() || i == j {
        fmt.Println(fmt.Errorf("%s", "Index Out Of Bounds Exception"))
		return
    }
    g.adjMat[i][j] = 1
    g.adjMat[j][i] = 1
}

func (g *graphAdjMat) removeEdge(i, j int) {
    if i < 0 || j < 0 || i >= g.size() || j >= g.size() || i == j {
        fmt.Println(fmt.Errorf("%s", "Index Out Of Bounds Exception"))
		return
    }
    g.adjMat[i][j] = 0
    g.adjMat[j][i] = 0
}

func (g *graphAdjMat) print() {
    fmt.Printf("\t顶点列表 = %v\n", g.vertices)
    fmt.Printf("\t邻接矩阵 = \n")
    for i := range g.adjMat {
        fmt.Printf("\t\t\t%v\n", g.adjMat[i])
    }
}


type Vertex = int

type graphAdjList struct {
    adjList map[Vertex][]Vertex
}

func newGraphAdjList(edges [][]Vertex) *graphAdjList {
    g := &graphAdjList{
        adjList: make(map[Vertex][]Vertex),
    }
    for _, edge := range edges {
        g.addVertex(edge[0])
        g.addVertex(edge[1])
        g.addEdge(edge[0], edge[1])
    }
    return g
}

func (g *graphAdjList) size() int {
    return len(g.adjList)
}

func (g *graphAdjList) addEdge(vet1 Vertex, vet2 Vertex) {
    _, ok1 := g.adjList[vet1]
    _, ok2 := g.adjList[vet2]
    if !ok1 || !ok2 || vet1 == vet2 {
        panic("error")
    }
    g.adjList[vet1] = append(g.adjList[vet1], vet2)
    g.adjList[vet2] = append(g.adjList[vet2], vet1)
}

func (g *graphAdjList) removeEdge(vet1 Vertex, vet2 Vertex) {
    _, ok1 := g.adjList[vet1]
    _, ok2 := g.adjList[vet2]
    if !ok1 || !ok2 || vet1 == vet2 {
        panic("error")
    }
    g.adjList[vet1] = DeleteSliceElms(g.adjList[vet1], vet2)
    g.adjList[vet2] = DeleteSliceElms(g.adjList[vet2], vet1)
}

func (g *graphAdjList) addVertex(vet Vertex) {
    _, ok := g.adjList[vet]
    if ok {
        return
    }
    g.adjList[vet] = make([]Vertex, 0)
}

func (g *graphAdjList) removeVertex(vet Vertex) {
    _, ok := g.adjList[vet]
    if !ok {
        panic("error")
    }
    delete(g.adjList, vet)
    for v, list := range g.adjList {
        g.adjList[v] = DeleteSliceElms(list, vet)
    }
}

func (g *graphAdjList) print() {
    var builder strings.Builder
    fmt.Printf("邻接表 = \n")
    for k, v := range g.adjList {
        builder.WriteString("\t\t" + strconv.Itoa(k) + ": ")
        for _, vet := range v {
            builder.WriteString(strconv.Itoa(vet) + " ")
        }
        fmt.Println(builder.String())
        builder.Reset()
    }
}

func DeleteSliceElms(list []Vertex ,vec Vertex) [] Vertex{
	return list
}


func graphBFS(g *graphAdjList, startVet Vertex)[]Vertex {
	res := make([]Vertex, 0)

	visited := make(map[Vertex]struct{})
	visited[startVet] = struct{}{}

	queue := make([]Vertex, 0)
	queue = append(queue, startVet)

	for len(queue) > 0 {
		vet := queue[0]
		queue = queue[1:]
		res = append(res, vet)
		for _, adjVet := range g.adjList[vet] {
			_, isExist := visited[adjVet]
			if !isExist {
				queue = append(queue, adjVet)
				visited[adjVet] = struct{}{}
			}
		}
	}
	return res
}

func dfs(g *graphAdjList, visited map[Vertex]struct{}, res *[]Vertex, vet Vertex){
	*res = append(*res, vet)
	visited[vet] = struct{}{}
	for _, adjVet := range g.adjList[vet] {
		_, isExist := visited[adjVet]
		if !isExist {
			dfs(g, visited, res, adjVet)
		}
	}
}

func graphDFS(g *graphAdjList, startVet Vertex) []Vertex {
	res := make([]Vertex, 0)
	visited := make(map[Vertex]struct{})
	dfs(g, visited, &res, startVet)
	return res
}