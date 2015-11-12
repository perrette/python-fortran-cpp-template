python-fortran-cpp template
===========================

This repository is a minimal example to make a python package 
that makes use of fortran (f2py) and C++ (cython) extensions
with a setup.py file.

It also contains other patterns such as script installation, 
with the excellent argparse, and ipython notebooks, as example 
of user interaction.

With these various tools at hand, jungling between git-managed packages
and normal work folders (NOT managaed by git, but keeping track of the 
git-version used), the work becomes very productive and reproducible.
And excellent to share work in a team.

Dependencies
------------

This template was tested in python 2.7 with:

- numpy : 1.9.2 (f2py)
- cython : 0.22 (c++ extension)
- ipython : 3.1.0 (ipython notebook)

Install
-------

Install the pacakge on your system:

    python setup.py install

Usage
-----

Then you may:

- execute myscript.py from anywhere on your system (to see excellent argparse at work)

        myscript.py --help
        myscript.py --version
        myscript.py -a 1 2 3 -b 2 2 2
        myscript.py -a 1 2 3 -b 2 2 2 -o c_div
        myscript.py -a 1 2 3 -b 2 2 2 -o f_mult

- copy the notebook template in your work directory, and start working...

Then feel free to use these pattern for your real work by editing these files
at your convenience. Do not forget:

- `setup.py` 
- `mypackage/__init__.py`


Workflow
--------

You need to install everytime you want the changes to be accessible from the 
notebook or other components that depend on mypackage. For that reason, it is 
better to only add functions and pieces of code that you consider stable.

In the development process, it is more convenient to work in the notebook 
and only add the functions to the actual package when you think you won't 
edit them every 5 min. Then your next notebook will be thinner, as it only 
need to `from mypackage import my_func` instead of having the whole body inside.

fortran with f2py
-----------------
The simplest to use (if you know fortran). Basically, as long as your fortan 
code only have simple types as input/output (scalars, arrays, strings), 
and make use of the intent(in) / intent(out) qualifiers, you do not need to 
do anything more than use numpy-extended Extension class and setup function:

    from numpy.distutils.core import Extension
    from numpy.distutils.core import setup

    flib = Extension(name = 'mypackage.flib',
                     extra_compile_args = ['-O3'],
                     sources = ['src_fortran/mymodule.f90'], # you may add several modules files under the same extension
                     )

    setup(
        ext_modules = [flib]
        )

c/c++ with cython
-----------------
In addition to c/c++ source files, it is necessary to add a definition 
indicating the c++ header:

    cdef extern from "path/to/my_header.h":
        int array_div(double *a, double *b, double *c, int n);

(yes, it is redundant since this info is already present in my_header.h
I am happy to hear your suggestion for less redundant alternatives)

And a wrapper in cython (see cython/*pyx file)
