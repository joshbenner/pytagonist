"""
CFFI wrapping of the drafter library.
"""
import os

from cffi import FFI

ffibuilder = FFI()

ffibuilder.set_source(
    '_drafter',
    """
    #include <drafter.h>
    """,
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

with open(os.path.join(os.path.dirname(__file__), 'drafter.h')) as f:
    ffibuilder.cdef(f.read())

if __name__ == '__main__':
    ffibuilder.compile()
