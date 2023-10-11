from saving_finance.settings.environment import env

SPECTACULAR_SETTINGS = {
    'COMPONENT_SPLIT_REQUEST': True,
    'SCHEMA_PATH_PREFIX': '/api/v[0-9]',
    'SWAGGER_UI_SETTINGS': {
        'persistAuthorization': True,
    },
}
SWAGGER_URL = env.str('SWAGGER_URL', None)
