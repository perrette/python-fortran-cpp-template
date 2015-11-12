# so that mypackage.__version__ gives you the right version (git check sum)
from .version import VERSION as __version__

# This line to import all of core content at the top level of the package.
# This is not always desirable, especially when this implies heavy dependencies
# that are not always needed. 
from .core import *
