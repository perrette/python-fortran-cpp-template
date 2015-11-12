import numpy as np
from mypackage import clib, flib

def py_add(a, b):
    """Pure python addition
    """
    return np.asarray(a) + np.asarray(b)

def f_mult(a, b):
    if not np.shape(a) == np.shape(b):
        raise ValueError("inconsistent shapes")
    return flib.operators.array_mult(a, b)

def c_div(a, b):
    return clib.c_div(np.asarray(a, 'd'), np.asarray(b, 'd'))

# def c_add(a, b):
#     return clib.array_add(a, b)
