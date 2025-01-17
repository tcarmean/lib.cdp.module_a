cmake_minimum_required(VERSION 3.15)
project(module_a)

set(CMAKE_C_STANDARD 99)

add_library(module_a src/module_a.c)
target_include_directories(module_a PUBLIC include)


install(TARGETS module_a)
