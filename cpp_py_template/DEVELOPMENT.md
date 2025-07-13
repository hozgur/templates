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

### `python/pyproject.toml`
- Modern Python package configuration
- Defines package metadata, dependencies, and build settings
- Configures the C++ extension module
- Uses the newer PEP 517/518 build system

### `python/setup.py`
- Minimal setup file for build customization
- Handles platform-specific C++ flags
- Manages pybind11 include directories
- Works alongside pyproject.toml for better compatibility

### `python/__init__.py`
- Makes the directory a Python package
- Imports and exposes the C++ functions
- Defines what users can import from the package

### `python/requirements.txt`
- Lists runtime Python package dependencies
- Required for using the package
- Build dependencies are in pyproject.toml

### `python/test.py`
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
- Created by setuptools and CMake
- Can be safely deleted to clean the project

## Development Workflow

1. Modify C++ code in `cpp/src/`
2. Add new functions to `pybind_wrapper.cpp`
3. Update Python type stubs in `math_ops_cpp.pyi`
4. Add tests in `test.py`
5. Build and test using one of these methods:

   ### Quick Development (recommended for C++ changes)
   ```bash
   # Rebuild only the C++ extension
   python setup.py build_ext --inplace
   
   # Run tests
   python test.py -v
   ```

   ### Full Package Installation
   ```bash
   # Install in development mode
   pip install -e .
   
   # Force rebuild everything
   pip install -e . --no-cache-dir --force-reinstall
   ```

   ### Distribution Build
   ```bash
   # Install build tool
   pip install build
   
   # Create distribution packages
   python -m build
   ```

6. For C++-centric development, you can still use:
   ```bash
   cmake && cmake --build .
   ```

## Modern Package Structure

The project now uses a hybrid approach:
- `pyproject.toml`: Main package configuration (PEP 517/518)
  - Note: The `ext-modules` configuration is experimental in setuptools and may change in future releases
  - You may see warnings about this during build, which is normal
- `setup.py`: Build customization for C++ extension
- `requirements.txt`: Runtime dependencies only
- Build dependencies are specified in `pyproject.toml`

This structure provides better compatibility with modern Python packaging tools while maintaining easy development workflows.

## Known Issues and Notes

### Experimental Features
The `ext-modules` configuration in `pyproject.toml` is marked as experimental by setuptools. You will see this warning during builds:
```
_ExperimentalConfiguration: `[tool.setuptools.ext-modules]` in `pyproject.toml` is still *experimental* and likely to change in future releases.
```
This is expected and the functionality works correctly. We use this configuration to stay aligned with modern Python packaging practices, but be aware that the syntax might change in future setuptools releases. 