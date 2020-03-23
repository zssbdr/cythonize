from setuptools   import setup,find_packages
from Cython.Build import cythonize
import os
import sys
from numpy.distutils.misc_util import Configuration

# from _build_utils import cythonize_extensions


def configuration(parent_package='', top_path=None):
    import numpy

    # if os.name == 'posix':
    #     libraries.append('m')

    #config = Configuration('multiscale_regularize_lr', parent_package, top_path)
    config = Configuration('myplus', parent_package, top_path)

    # submodules with build utilities
    config.add_subpackage('src')
    config.name = 'myplus'
    config.version = '1.0.0'
    # Skip cythonization as we do not want to include the generated
    # C/C++ files in the release tarballs as they are not necessarily
    # forward compatible with future versions of Python for instance.
    # if 'sdist' not in sys.argv:
    #     cythonize_extensions(top_path, config)

    return config



if __name__ == '__main__':
    setup(**configuration(top_path='').todict())