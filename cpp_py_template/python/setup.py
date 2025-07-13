import sys
import pybind11
from setuptools import setup
from setuptools.command.build_ext import build_ext


class BuildExt(build_ext):
    def build_extensions(self):
        # Add pybind11 include dirs
        for ext in self.extensions:
            ext.include_dirs.append(pybind11.get_include())
            # Add C++20 flags
            ext.extra_compile_args = ['/std:c++20'] if sys.platform == 'win32' else ['-std=c++20']
        super().build_extensions()

setup(
    cmdclass={
        "build_ext": BuildExt,
    }
) 