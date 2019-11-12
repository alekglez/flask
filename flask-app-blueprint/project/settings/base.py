# Define here the base configuration..
DEBUG = False


# And after that...
# Used to define some configuration in the local environment in order to
# don't modify the repository code...
try:
    from .local import *
except ImportError:
    pass
