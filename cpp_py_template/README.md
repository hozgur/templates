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
    ├── pyproject.toml    # Modern Python package configuration
    ├── setup.py         # Build customization
    ├── requirements.txt # Runtime dependencies
    └── test.py         # Unit tests
```

## Prerequisites

- Python 3.7 or newer
- C++ compiler with C++20 support
- CMake 3.14 or newer (for C++ development)
- pip (Python package installer)

## Installation

### Option 1: Using pip (Recommended for Python users)

1. Install the package in development mode:
```bash
cd python
pip install -e .
```

This will:
- Install all required dependencies
- Build the C++ extension
- Install the package in "editable" mode

The `-e` flag installs the package in "editable" mode, which means:
- You can use the package from any directory
- Changes to the Python code take effect immediately
- Rebuilding is only needed when C++ code changes

### Quick Rebuild for C++ Changes

After modifying C++ files, you can quickly rebuild just the extension:
```bash
cd python
python setup.py build_ext --inplace
```

### Clean Rebuild

If you need a complete rebuild:
```bash
cd python
pip install -e . --no-cache-dir --force-reinstall
```

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
4. Add type hints to `math_ops_cpp.pyi` if needed
5. Add tests in `test.py`
6. Rebuild the extension with `python setup.py build_ext --inplace`

### Running Tests

Run the tests with verbose output:
```bash
cd python
python test.py -v
```

This will run all unit tests and show detailed results.

### Package Configuration

The project uses modern Python packaging:
- `pyproject.toml`: Main package configuration (PEP 517/518)
- `setup.py`: Build customization for C++ extension
- `requirements.txt`: Runtime dependencies

Note: The `ext-modules` configuration in `pyproject.toml` is experimental in setuptools and you may see warnings about this during builds. This is expected and doesn't affect functionality.

For more detailed development information, see [DEVELOPMENT.md](DEVELOPMENT.md).

## License

TODO: Add license information

## Contributing

TODO: Add contribution guidelines 