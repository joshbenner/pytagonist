import os
from setuptools import setup
from setuptools.command.sdist import sdist
from distutils.command.build import build
from distutils import log
from subprocess import call

SETUP_PATH = os.path.dirname(os.path.abspath(__file__))
DRAFTER_PATH = os.path.join(SETUP_PATH, 'drafter')


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
        code = call(['make', 'distclean'], cwd=DRAFTER_PATH)
        if code != 0:
            raise RuntimeError('Cannot clean drafter library')
        sdist.run(self)

setup(
    name='pytagonist',
    setup_requires=['setuptools_scm', 'cffi>=1.0.0,<2.0.0'],
    use_scm_version=True,
    cmdclass={
        'build': Build,
        'sdist': SourceDistribution
    },
    py_modules=['pytagonist'],
    url='https://github.com/joshbenner/pytagonist',
    license='MIT',
    author='Josh Benner',
    author_email='josh@bennerweb.com',
    description='Wrapper for Drafter library, a C parser for APIBlueprint.',
    install_requires=[
        'cffi>=1.0.0,<2.0.0'
    ],
    cffi_modules=[
        './build_drafter.py:ffibuilder'
    ],
    extras_require={
        'test': ['pytest']
    }
)
