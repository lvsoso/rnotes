# hello world

## build

```shell
g++ -o main main.cpp hello/hello.cpp world/world.cpp -I ./world
```

```shell
g++ -c main.cpp -I ./world
g++ -c hello/hello.cpp
g++ -c world/world.cpp
g++ -o main main.o hello.o world.o
```
