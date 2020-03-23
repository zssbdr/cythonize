from setuptools   import setup,find_packages
from Cython.Build import cythonize
import os
import sys
from numpy.distutils.misc_util import Configuration

# from _build_utils import cythonize_extensions

exts = ['plus']
def configuration(parent_package='', top_path=None):
    import numpy

    # if os.name == 'posix':
    #     libraries.append('m')

    #config = Configuration('multiscale_regularize_lr', parent_package, top_path)
    config = Configuration('src', parent_package, top_path)
    if 'build_ext' in sys.argv:
        for ext in exts:
            config.add_extension(ext, ext + '.py')
        # config.add_extension('model', 'model.py')
        config.ext_modules = cythonize(config.ext_modules)

    config.add_data_files("*.pyd")
    config.add_data_files("*.os")
    # Skip cythonization as we do not want to include the generated
    # C/C++ files in the release tarballs as they are not necessarily
    # forward compatible with future versions of Python for instance.
    # if 'sdist' not in sys.argv:
    #     cythonize_extensions(top_path, config)

    return config



if __name__ == '__main__':
    setup(**configuration(top_path='').todict())