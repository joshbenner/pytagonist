import os
from setuptools import setup, Extension
from setuptools.command.sdist import sdist
from distutils.command.build import build
from distutils import log
from subprocess import call

SETUP_PATH = os.path.dirname(os.path.abspath(__file__))
DRAFTER_PATH = os.path.join(SETUP_PATH, 'drafter')

# This package can build/install without Cython, only if Cython had previously
# been used to generate the C source code. Installing a built package without
# having Cython installed will work, but installing from source will require
# Cython to be installed.
USE_CYTHON = False

try:
    from Cython.Build import cythonize
    USE_CYTHON = True
except ImportError:
    from setuptools.command.build_ext import build_ext


class Build(build):
    """
    Custome builder that runs drafter Makefile instead of build_clib.

    This is to avoid having to reproduce all the build configurations of drafter
    (and its dependencies).
    """
    def run(self):
        log.info('Building drafter')
        code = call(['make', 'drafter'], cwd=DRAFTER_PATH)
        if code != 0:
            raise RuntimeError('Cannot build drafter library')
        build.run(self)


class SourceDistribution(sdist):
    """
    Custom source distribution prep that makes sure we don't mistakenly include
    build output in the source distribution.

    While MANIFEST.in can do this, keeping the MANIFEST.in up-to-date is much
    more difficult than just asking the dependencies to clean themselves first.
    """
    def run(self):
        log.info('Cleaning drafter')
        code = call(['make', 'clean'], cwd=DRAFTER_PATH)
        if code != 0:
            raise RuntimeError('Cannot clean drafter library')
        sdist.run(self)

pytagonist = Extension(
    'pytagonist',
    sources=['pytagonist.pyx' if USE_CYTHON else 'pytagonist.c'],
    libraries=['drafter', 'sos', 'snowcrash', 'markdownparser', 'sundown',
               'stdc++'],
    library_dirs=['drafter/build/out/Release'],
    include_dirs=[
        'drafter/src',
        'drafter/ext/snowcrash/ext/markdown-parser/src',
        'drafter/ext/snowcrash/ext/markdown-parser/ext/sundown/src',
        'drafter/ext/sos/src',
        'drafter/ext/snowcrash/src'
    ]
)

setup(
    name='pytagonist',
    setup_requires=['setuptools_scm', 'Cython'],
    use_scm_version=True,
    ext_modules=cythonize(pytagonist) if USE_CYTHON else [pytagonist],
    cmdclass={'build': Build, 'sdist': SourceDistribution},
    include_package_data=True,
    package_data={'': ['pytagonist.c']},
    url='',
    license='MIT',
    author='Josh Benner',
    author_email='josh@bennerweb.com',
    description='Wrapper for Drafter library, a C parser for APIBlueprint.'
)
