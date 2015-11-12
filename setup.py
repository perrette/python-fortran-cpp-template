"""Setup file to compile the sources and install the package on your system
"""
from __future__ import division, absolute_import, print_function
import os, sys, subprocess, warnings
from distutils.core import setup

# First check git version and write a version.py file
# ===================================================
DEFAULT_VERSION = "unknown"

def check_git_version():
    # credit: some this code was taken from pandas' setup.py file
    pipe = None
    for cmd in ['git','git.cmd']:
        try:
            pipe = subprocess.Popen([cmd, "describe", "--always", "--match", "v[0-9]*"],
                                stdout=subprocess.PIPE)
            (so,serr) = pipe.communicate()
            if pipe.returncode == 0:
                break
        except:
            pass

    if pipe is None or pipe.returncode != 0:
        warnings.warn("WARNING: Couldn't get git revision, using generic version string")
        return DEFAULT_VERSION
    else:
      # have git, in git dir, but may have used a shallow clone (travis does this)
      rev = so.strip()
      # makes distutils blow up on Python 2.7
      if sys.version_info[0] >= 3:
          rev = rev.decode('ascii')

      return rev

# write version number to the package before installation
rev = check_git_version()
with open(os.path.join("mypackage","version.py"), "w") as f:
    f.write("VERSION = {}".format(repr(rev)))

# Build the main package, with script etc...
# ==========================================
setup(name = 'mypackage',
  description       = "example package using c++ and fortran",
  author            = "Mahe Perrette",
  packages = ["mypackage"],
  scripts = ["scripts/myscript.py"],
  )

# Build the extensions
# --------------------
# The setup steps have been splitted here, because f2py uses a modified version of the setup.
# If only cython or only f2py is used, the setup file can of course be one.

# Build the cython extension
# --------------------------
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

# Build the f2py fortran extension
# --------------------------------
from numpy.distutils.core import Extension
from numpy.distutils.core import setup

flib = Extension(name = 'mypackage.flib',
                 extra_compile_args = ['-O3'],
                 sources = ['src_fortran/mymodule.f90'], # you may add several modules files under the same extension
                 )

setup(
    ext_modules = [flib]
    )
