# Development Guide

This document explains the purpose of each file in the project and why it's needed.

## C++ Files (`cpp/`)

### `cpp/src/math_ops.hpp`
- Header file declaring the core C++ functions
- Defines the interface for mathematical operations
- Used by both the C++ executable and Python bindings

### `cpp/src/math_ops.cpp`
- Implements the core mathematical functions
- Contains the actual C++ logic that Python will use
- Keeps the implementation separate from the interface

### `cpp/src/main.cpp`
- Entry point for the standalone C++ executable
- Demonstrates how to use the math operations in pure C++
- Useful for testing the C++ code without Python

### `cpp/src/pybind_wrapper.cpp`
- Creates the bridge between C++ and Python
- Uses pybind11 to expose C++ functions to Python
- Defines how C++ types map to Python types

### `cpp/CMakeLists.txt`
- CMake build configuration for C++ code
- Sets up both the executable and Python module builds
- Configures pybind11 and compiler settings

## Python Files (`python/`)

### `python/setup.py`
- Python package build configuration
- Tells pip how to build the C++ extension
- Defines package metadata and dependencies

### `python/__init__.py`
- Makes the directory a Python package
- Imports and exposes the C++ functions
- Defines what users can import from the package

### `python/requirements.txt`
- Lists Python package dependencies
- Required for building and using the package
- Helps others reproduce the development environment

### `python/test_math_ops.py`
- Unit tests for the Python bindings
- Ensures C++ functions work correctly in Python
- Provides usage examples through tests

### `python/test_repl.py`
- Interactive demonstration script
- Shows how to use the package in practice
- Useful for quick testing and examples

### `python/math_ops_cpp.pyi`
- Type stub file for IDE support
- Helps with code completion and type checking
- Makes development more efficient with better tooling

### `python/py.typed`
- Marks the package as type-hinted
- Enables better IDE support
- Required for proper typing support

## Build Outputs

### `*.pyd` files
- Compiled Python extension modules
- Created when building the package
- Contains the actual C++ code Python can use

### `build/` directory
- Contains temporary build files
- Created by setup.py and CMake
- Can be safely deleted to clean the project

## Development Workflow

1. Modify C++ code in `cpp/src/`
2. Add new functions to `pybind_wrapper.cpp`
3. Update Python type stubs in `math_ops_cpp.pyi`
4. Add tests in `test_math_ops.py`
5. Build using either:
   - `python setup.py build_ext --inplace` (Python-centric)
   - `cmake && cmake --build .` (C++-centric) 