cmake_minimum_required(VERSION 3.16.3)
project(hello)

set(HELLO_SRC ${CMAKE_CURRENT_SOURCE_DIR}/hello.cpp ${CMAKE_CURRENT_SOURCE_DIR}/hello1.cpp)

add_library(hellolib SHARED ${HELLO_SRC})