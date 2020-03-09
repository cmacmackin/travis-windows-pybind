cmake_minimum_required(VERSION 3.2 FATAL_ERROR)

PROJECT(reproducer LANGUAGES CXX)

find_package(PythonInterp 3.6 REQUIRED)
find_package(PythonLibs 3.6 REQUIRED)
add_subdirectory(pybind11)

set(PY_SOURCES cppmath.cpp)

# Build and link the pylib module
pybind11_add_module(CPPMATH MODULE ${PY_SOURCES})

if("$ENV{TRAVIS}" STREQUAL "true" AND MINGW)
#  target_compile_options(CPPMATH PRIVATE -fno-lto)
  target_link_libraries(CPPMATH PRIVATE #-fno-lto
    -static -static-libstdc++ -static-libgcc)

  set(CMAKE_AR  "gcc-ar")
  CMAKE_CXX_ARCHIVE_CREATE ( = <CMAKE_AR> qcs <TARGET> <LINK_FLAGS> <OBJECTS>)
  CMAKE_CXX_ARCHIVE_FINISH ( = true)
endif()
