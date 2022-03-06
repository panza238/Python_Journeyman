from .my_bz2 import opener as bz2_opener
from .my_gzip import opener as gzip_opener

__all__ = ['bz2_opener', 'gzip_opener']
# with the __all__ variable, I control what gets imported with *
# in this case, the modules my_... won't be imported. Only
