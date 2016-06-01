from libc.stdlib cimport free

cdef extern from "drafter/src/cdrafter.h":
    cdef int drafter_c_parse(const char* source,
                             unsigned int options,
                             int ast_type,
                             char** result);

def parse(source, options = 0, ast_type = 1):
    cdef char *result = NULL
    drafter_c_parse(source, options, ast_type, &result)
    ast = str(result)
    free(result)
    return ast

cpdef enum:
    SC_RENDER_DESCRIPTIONS_OPTION = (1 << 0)
    SC_REQUIRE_BLUEPRINT_NAME_OPTION = (1 << 1)
    SC_EXPORT_SOURCEMAP_OPTION = (1 << 2)
    DRAFTER_NORMAL_AST_TYPE = 0
    DRAFTER_REFRACT_AST_TYPE = 1
