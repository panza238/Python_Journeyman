"""Module to show how sys.path works!"""
import os


def found():
    """If I do not manually add this file to sys.path, Python will not find it
    and thus will not import it!"""
    path = os.getenv('PYTHONPATH')
    print('PYTHONPATH', path)
    return "Python found me!"

# in order for this to be imported, the following command should be executed from the REPL
# sys.path.append('/Users/ezequiel.panzarasa/Desktop/Panza/Repos/Python_Journeyman/Chapter01/not_in_path')
