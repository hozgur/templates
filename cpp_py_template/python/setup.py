from setuptools import setup, Extension
import pybind11
import sys

# Use MSVC-specific flag for C++20 on Windows
extra_compile_args = ['/std:c++20'] if sys.platform == 'win32' else ['-std=c++20']

cpp_module = Extension(
    "math_ops_cpp",
    sources=["../cpp/src/pybind_wrapper.cpp", "../cpp/src/math_ops.cpp"],
    include_dirs=[pybind11.get_include(), "../cpp/src"],
    language='c++',
    extra_compile_args=extra_compile_args
)

setup(
    name="math_ops",
    version="0.1.0",
    author="Your Name",
    description="A Python package wrapping C++ math operations using pybind11",
    ext_modules=[cpp_module],
    setup_requires=["pybind11>=2.10.0"],
    install_requires=["pybind11>=2.10.0"],
    python_requires=">=3.7",
    package_data={"": ["py.typed"]},
    zip_safe=False
) 