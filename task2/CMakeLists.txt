cmake_minimum_required(VERSION 3.0) #
find_package(GTest QUIET)

add_subdirectory(B)
target_include_directories(A)
target_include_directories(C)
target_include_directories(${GTEST_INCLUDE_DIRS})

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/lib)
set_target_properties(library PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/lib)

add_executable(C C/main.cpp C/main.h A/index.h)
target_link_libraries(C library)

add_executable(Google_Tests C/test.cpp)
target_link_libraries(Google_Tests ${GTEST_LIBRARIES} Threads::Threads)
target_link_libraries(Google_Tests library)

add_custom_target(
    running_target ALL
    DEPENDS ${CMAKE_SOURCE_DIR}/A/index.h
)

add_custom_command(
    PRE_BUILD
    OUTPUT ${CMAKE_SOURCE_DIR}/A/index.h
    COMMAND python3 ${CMAKE_SOURCE_DIR}/A/preparing.py
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/A/
)
