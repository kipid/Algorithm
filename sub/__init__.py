# Needed because we are in a sub folder
"""
The __init__.py file is required to make
Python treat directories containing files as package.
This prevents directories with a common name, such as string,
unintentionally hiding valid modules that occur later on the module search path.
In the simplest case, __init__.py can just be an empty file,
but it can also execute initialization code for the package.
"""

from .test import *
# If the above does not exist,
"""
		test.doTest()
    ^^^^^^^^^^^
AttributeError: 'function' object has no attribute 'doTest'
"""

# . current directory
# .. parent directory