cmake_minimum_required(VERSION 3.2 FATAL_ERROR)

PROJECT(reproducer LANGUAGES CXX)

find_package(PythonInterp 3.6 REQUIRED)
find_package(PythonLibs 3.6 REQUIRED)
add_subdirectory(pybind11)

set(PY_SOURCES cppmath.cpp)

message("Printing debug information:")
message($ENV{TRAVIS})
message(${WIN32})
message(${MINGW})
if("$ENV{TRAVIS}" STREQUAL "true")
  message("In CI environment")
endif()
if(WIN32)
  message("On Windows")
endif()
if($ENV{TRAVIS} STREQUAL "true" AND WIN32)
  message("Should statically link compiler libraries")
endif()

# Build and link the pylib module
pybind11_add_module(CPPMATH MODULE ${PY_SOURCES})

if("$ENV{TRAVIS}" STREQUAL "true" AND MINGW)
  message("Statically linking compiler libraries")
  target_link_libraries(CPPMATH PRIVATE
    -static -static-libstdc++ -static-libgcc)
endif()
