import os
from distutils.errors import CCompilerError, DistutilsExecError, DistutilsPlatformError

from setuptools import Extension
from setuptools.command.build_ext import build_ext

import numpy

np = numpy.get_include()

ext_modules = [
    Extension(
        'thinning',
        sources=['c_thinning.c'],
        include_dirs=[np, os.path.join(np, "numpy")]
    ),
]


class BuildFailed(Exception):
    pass


class ExtBuilder(build_ext):

    def run(self):
        try:
            build_ext.run(self)
        except (DistutilsPlatformError, FileNotFoundError):
            raise BuildFailed('File not found. Could not compile C extension.')

    def build_extension(self, ext):
        try:
            build_ext.build_extension(self, ext)
        except (CCompilerError, DistutilsExecError, DistutilsPlatformError, ValueError):
            raise BuildFailed('Could not compile C extension.')


def build(setup_kwargs):
    setup_kwargs.update({"ext_modules": ext_modules, "cmdclass": {"build_ext": ExtBuilder}})