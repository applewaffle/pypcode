cmake_minimum_required(VERSION 3.8)

project(
    asm2llvmir
	LANGUAGES C CXX
)

add_subdirectory(src)
add_executable(sleighexample
	sleighexample.cc
)

target_link_libraries(sleighexample
    sla
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