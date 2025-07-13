import os
import sys
import unittest

# Add the current directory to Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import the test module
from cpp_py_template.python.test import TestMathOps

if __name__ == '__main__':
    unittest.main(argv=['run_tests.py', '-v']) 