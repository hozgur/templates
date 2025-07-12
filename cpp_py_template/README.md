# C++/Python Template with pybind11

This template demonstrates how to create a Python package that wraps C++ code using pybind11. The example includes simple mathematical operations implemented in C++ and exposed to Python.

## Project Structure

```
cpp_py_template/
├── cpp/
│   ├── CMakeLists.txt
│   └── src/
│       ├── main.cpp
│       ├── math_ops.cpp
│       ├── math_ops.hpp
│       └── pybind_wrapper.cpp
└── python/
    ├── __init__.py
    ├── requirements.txt
    └── setup.py
```

## Prerequisites

- Python 3.7 or newer
- C++ compiler with C++20 support
- CMake 3.14 or newer
- pip (Python package installer)

## Installation

### Option 1: Using pip and setup.py (Recommended for Python users)

1. Install the requirements:
```bash
cd python
pip install -r requirements.txt
```

2. Build and install the package:
```bash
# For local development (recommended)
pip install -e .

# OR for regular installation
python setup.py build_ext --inplace
```

The `-e` flag installs the package in "editable" mode, which means:
- You can use the package from any directory
- Changes to the Python code take effect immediately
- Rebuilding is only needed when C++ code changes

⚠️ **Important**: After modifying any C++ files, you must rebuild:
```bash
cd python
python setup.py build_ext --inplace
```
Python changes don't require rebuilding, but C++ changes do.

### Option 2: Using CMake (Recommended for C++ development)

1. Install pybind11:
```bash
pip install pybind11
```

2. Build the project:
```bash
cd cpp
mkdir build && cd build
cmake ..
cmake --build .
```

## Usage

### In Python

```python
from math_ops import add, mul

# Addition
result1 = add(2, 3)  # Returns 5

# Multiplication
result2 = mul(4, 5)  # Returns 20
```

### As C++ Executable

The project also builds a standalone C++ executable that demonstrates the math operations:

```bash
# If built with CMake
./build/math_ops_cli
```

## Available Functions

- `add(a: int, b: int) -> int`: Add two integers
- `mul(a: int, b: int) -> int`: Multiply two integers

## Development

### Adding New Functions

1. Add your C++ function in `cpp/src/math_ops.hpp` and `cpp/src/math_ops.cpp`
2. Expose it in `cpp/src/pybind_wrapper.cpp` using the `PYBIND11_MODULE` macro
3. Update `python/__init__.py` to expose the new function to Python
4. Rebuild the extension with `python setup.py build_ext --inplace`

### Running Tests

TODO: Add testing instructions

## License

TODO: Add license information

## Contributing

TODO: Add contribution guidelines 