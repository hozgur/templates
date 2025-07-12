#include <pybind11/pybind11.h>
#include "math_ops.hpp"

namespace py = pybind11;

PYBIND11_MODULE(math_ops_cpp, m) {
    m.def("add", &add, "Add two integers");
    m.def("mul", &mul, "Multiply two integers");
} 