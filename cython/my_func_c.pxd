# -*- mode: python -*-

# This could be part of the  my_func.pyx file, but it useful to have a specific namespace (import my_func_c)
cdef extern from "../src_cpp/my_func.h":
    int array_div(double *a, double *b, double *c, int n);
