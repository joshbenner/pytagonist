// This file is read by build_drafter.py to generate Python bindings.
// It is a simplified declaration of the drafter library API used by pytagonist.

typedef struct drafter_result drafter_result;

typedef enum {
    DRAFTER_SERIALIZE_YAML = 0,
    DRAFTER_SERIALIZE_JSON
} drafter_format;

typedef struct {
    bool sourcemap;
    drafter_format format;
} drafter_options;

int drafter_parse_blueprint_to(const char* source,
                               char** out,
                               const drafter_options options);

drafter_result* drafter_check_blueprint(const char* source);

char* drafter_serialize(drafter_result* res, const drafter_options options);
