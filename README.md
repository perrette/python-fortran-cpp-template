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

Usage
-----

After downloading the repo, install your pacakge on your system:

    python setup.py install

Then you may:

- execute myscript.py from anywhere on your system (to see excellent argparse at work)

    myscript.py --help
    myscript.py -a 1 2 3 -b 2 2 2
    myscript.py -a 1 2 3 -b 2 2 2 -o c_div
    myscript.py -a 1 2 3 -b 2 2 2 -o f_mult

- copy the notebook template in your work directory, and start working...

Then feel free to use these pattern for your real work by editing these files
at your convenience. Do not forget:

- `setup.py` 
- `mypackage/__init__.py`

