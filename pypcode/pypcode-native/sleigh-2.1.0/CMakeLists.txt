cmake_minimum_required(VERSION 3.8)

project(
    asm2llvmir
	LANGUAGES C CXX
)

add_subdirectory(src)

set(CMAKE_CXX_STANDARD 14)
find_package(LLVM REQUIRED CONFIG)
add_definitions(${LLVM_DEFINITIONS})
include_directories(${LLVM_INCLUDE_DIRS})
link_directories(${LLVM_LIBRARY_DIRS})

add_executable(sleighexample
	sleighexample.cc
)

target_link_libraries(sleighexample
    sla
    LLVMSupport
)

target_include_directories(sleighexample
                        PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/src
                        )

target_compile_options(sleighexample PRIVATE
                        -Wall 
                        -Wno-sign-compare
                        )

#set_target_properties(capstone2llvmirtool
#	PROPERTIES
#		OUTPUT_NAME "retdec-capstone2llvmir"
#)