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

Note, if you need to modify / update some piece of packaged code later, you can always
use the magicc command %load mymodule.py to have the content of the file
loaded in the notebook cell, then edit out the unnecessary part, and expand / debug 
the bit of code you are interested in from within the notebook, without having
to re-install the whole package at every new change. When you are happy with the changes, 
copy back into the actual package, make a git commit etc..(of course, this assumes the 
bit you want to edit is not a dependency for other parts of the code)

Limitations of f2py fortran
---------------------------
Just a few things out of my own experience with f2py (please refer to [the official doc](http://docs.scipy.org/doc/numpy-dev/f2py) for more exhaustive information).
- use ìntent(in/out/inout) mentions
- use *simple* input/output arguments in subroutines and functions. This means in particular, no derived type, no allocatable arrays. [Some tools](https://github.com/jameskermode/f90wrap) seem to relax this constraint, but not sure this will work for packaging.
- the approach of globally defining `integer, parameter :: dp = kind(0.d0)` and then using `real(dp)` 
instead of `double precision`, as encouraged [on fortran90.org](http://www.fortran90.org/src/best-practices.html#floating-point-numbers), 
does *not* work with f2py. You should use old-fashioned `double precision`
(or plain `real(8)`, which is more confusing to me than just `double precision`).
- using `private` module with only a few `public` methods/functions does *not* work when wrapping `f2py`. `f2py` blindly attemps to wrap everything it finds in the module, and a subsequent `use moodule, only: my_private_func` 
will fail... So keep everything public.


Notes on packaging
------------------

Packaging is useful to have your code importable from everywhere (as any package installed with pip)
and to cleanly separate base functionality that you do not modify too often from daily work that 
will be done preferentially in the notebook, or anywhere on the disk with various input data, 
notes, output figures etc..., which you do not want to have tracked in git but instead archived.


The built-in packaging in python 2.7 is distutil:

    setup(name = 'mypackage',
      description       = "example package using c++ and fortran",
      author            = "Your Name",
      packages = ["mypackage"],  # also add subpackages !!
      scripts = ["scripts/myscript.py"],  # add scripts to be called globally
      )

Extensions written are added via a `ext_modules` parameter. 
f2py and cython have highly simplified the way of programming extensions, 
by providing their own `setup` function and an `Extension` subclass (for f2py) 
or by providing a user-defined `build_ext` parameter (cython). 

The way they do that does not seem to be compatible, so if both are to be
used in the same pacakge, this needs to be done with two separate `setup` calls.

So in this example, we first install the
python package without any extension (first) setup, then install the 
cython and f2py extensions as subpackages, with two additional setup calls.

... extension : fortran + f2py
------------------------------------
The simplest to use (if you know fortran). Basically, as long as your fortan 
code only have simple types as input/output (scalars, arrays, strings) (no derived types!!), 
and make use of the intent(in) / intent(out) qualifiers, you do not need to 
do anything more than use numpy-extended Extension class and setup function:

    from numpy.distutils.core import Extension
    from numpy.distutils.core import setup

    flib = Extension(name = 'mypackage.flib',
                     extra_compile_args = ['-O3'],
                     sources = ['src_fortran/mymodule.f90'], # you may add several module files under the same extension
                     )

    setup(
        ext_modules = [flib]
        )

... extension : c/c++ + cython
-------------------------------------
In addition to c/c++ source files, it is necessary to add a definition 
indicating the c++ header:

    cdef extern from "path/to/my_header.h":
        int array_div(double *a, double *b, double *c, int n);

(yes, it is redundant since this info is already present in my_header.h
I am happy to hear your suggestion for less redundant alternatives)

And a wrapper in cython (see `cython/*pyx` file)

When this is done, the setup.py part is not more difficult than f2py:

    from distutils.extension import Extension
    from Cython.Distutils import build_ext

    clib = Extension("mypackage.clib",  # indicate where it should be available !
                          sources=["cython/my_func.pyx",
                                   "src_cpp/my_func.cpp",
                                   ],
                          extra_compile_args=["-O3", "--std=c++11", "-ffast-math", "-Wall"],
                          language="c++")

    setup(
        cmdclass = {'build_ext': build_ext},
        ext_modules = [clib]
        )


Credits
-------
Much of the cython part was inspired by the [dbg](https://github.com/pism/regional-tools) package.
