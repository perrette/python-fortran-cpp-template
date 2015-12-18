"""Setup file to compile the sources and install the package on your system
"""
from distutils.core import setup
import versioneer

# Build the main package, with script etc...
# ==========================================
setup(name = 'mypackage',
      description       = "example package using c++ and fortran",
      author            = "Mahe Perrette",
      packages = ["mypackage"],
      scripts = ["scripts/myscript.py"],
      version = versioneer.get_version(),
      cmdclass = versioneer.get_cmdclass()
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
