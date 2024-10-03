cmake_minimum_required(VERSION 3.10)

project(suma)
set(CMAKE_CXX_STANDARD 11)
set(PYBIND11_PYTHON_VERSION 3.10)
set(CMAKE_CXX_FLAGS "-Wall -Wextra -fPIC")

find_package(pybind11 REQUIRED)

pybind11_add_module(${PROJECT_NAME} pynsuma.cpp)

target_compile_definitions(${PROJECT_NAME} PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
target_include_directories(${PROJECT_NAME} PRIVATE ${PYBIND11_INCLUDE_DIRS})
#target_link_libraries(${PROJECT_NAME} PRIVATE Eigen3::Eigen)
#g++ -O3 -Wall -shared -std=c++17 -fPIC $(python3 -m pybind11 --includes) pysuma.cpp -o suma$(python3-config --extension-suffix)

# add the executable
# add_executable(${PROJECT_NAME} main.cpp)
# target_include_directories( ${PROJECT_NAME} PRIVATE)
# target_link_libraries(${PROJECT_NAME} PRIVATE Eigen3::Eigen)
