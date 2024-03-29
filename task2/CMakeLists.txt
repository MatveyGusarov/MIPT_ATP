cmake_minimum_required(VERSION 3.16)
find_package(GTest REQUIRED)

add_subdirectory(B)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/lib)
set_target_properties(library PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/lib)

add_executable(C C/main.cpp C/main.h A/index.h)
target_include_directories(C PUBLIC A)
target_link_libraries(C library)

add_executable(CTest C/main_test.cpp)
target_include_directories(CTest PUBLIC ${GTEST_INCLUDE_DIRS})
target_link_libraries(CTest ${GTEST_LIBRARIES} Threads::Threads)
target_link_libraries(CTest library)

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
