# -*- mode: python -*-
#cython: boundscheck=False
#cython: wraparound=False
# Comments above are special. Please do not remove.
cimport numpy as np  # needed for function arguments
import numpy as np # needed for np.empty_like

cimport my_func_c

ctypedef np.float32_t float_t
ctypedef np.float64_t double_t
ctypedef np.int32_t int_t

def c_div(np.ndarray[dtype=double_t, ndim=1, mode="c"] a, 
          np.ndarray[dtype=double_t, ndim=1, mode="c"] b):
    """divide two arrays

    Parameters
    ----------
    a : 1-D numpy array 
        first operand
    b : 1-D numpy array
        second operand

    Returns
    -------
    c : 1-D numpy array
        result of division of a by b
    """
    cdef np.ndarray[dtype=double_t, ndim=1, mode="c"] output
    output = np.empty_like(a, dtype='d')

    if not (a.shape[0] == b.shape[0]):
        raise ValueError("a and b shapes are not consistent")

    my_func_c.array_div(<double*>a.data, <double*>b.data, <double*>output.data, a.shape[0])

    return output

