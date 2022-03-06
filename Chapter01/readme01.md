# README Chapter01

#### Remember to set the PYTHONPATH env variable
The PYTHONPATH environment variable is a list of paths that are added to sys.path when Python starts.

#### Relative imports are cool... but to be used with care! 

#### You can make executable directories and .zip files! 
#### And packages too! (just add the -m flag! python -m <package>)

#### Recomended layout:

```
project_name/
  setup.py
  project_name/
    __init__.py
    more_source.py
    subpackage1/
      __init__.py
  test/
    test_code.py
```