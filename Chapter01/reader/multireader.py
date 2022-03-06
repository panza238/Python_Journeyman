"""MultiReader class. """
import os

# These are both relative imports!
from .compressed import my_bz2 as bzipped
from .compressed import my_gzip as gzipped
#import compressed.my_bz2 as bzipped
#import compressed.my_gzip as gzipped

# This maps file extensions to corresponding open methods.
extension_map = {
    '.bz2': bzipped.opener,
    '.gz': gzipped.opener,
}
# This magic mapping allows me to open .txt, .bz and .gz files with a single command,
#   not having to specify anything else!


class MultiReader(object):
    """MultiReader class"""
    def __init__(self, filename):
        self.filename = filename
        extension = os.path.splitext(filename)[1]  # Este es un buen truco! os.path.splitext and os.split
        opener = extension_map.get(extension, open)
        self.f = opener(filename, mode='rt', encoding='utf-8')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()