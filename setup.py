from setuptools import setup, Extension

have_cython = False

try:
    from Cython.Build import cythonize
    have_cython = True
except ImportError:
    from distutils.command.build_ext import build_ext

pytagonist = Extension(
    'pytagonist',
    sources=['pytagonist.pyx' if have_cython else 'pytagonist.c'],
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
    ext_modules=cythonize(pytagonist) if have_cython else [pytagonist],
    cmdclass={} if have_cython else {'build_ext': build_ext},
    include_package_data=True,
    package_data={'': ['pytagonist.c']},
    url='',
    license='MIT',
    author='Josh Benner',
    author_email='josh@bennerweb.com',
    description='Wrapper for Drafter library, a C parser for APIBlueprint.'
)
