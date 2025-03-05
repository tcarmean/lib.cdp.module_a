cmake_minimum_required(VERSION 3.15)
project(module_a)

set(CMAKE_C_STANDARD 99)

add_library(module_a SHARED src/module_a.c)
target_include_directories(module_a PUBLIC
                            $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/src>
                            $<INSTALL_INTERFACE:include>
                            )
set_target_properties(module_a PROPERTIES PUBLIC_HEADER "src/module_a.h")

install(TARGETS module_a)





