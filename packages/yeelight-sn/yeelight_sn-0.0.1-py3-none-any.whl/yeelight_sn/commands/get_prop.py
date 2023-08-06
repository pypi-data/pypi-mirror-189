from .command import create_command as create_command_base

METHOD = "get_prop"

PARAM_POWER = 'power'
PARAM_BRIGHTNESS = 'bright'
PARAM_COLOR_TEMPERATURE = 'ct'
PARAM_COLOR = 'rgb'
PARAM_NAME = 'name'

PARAM_ALL = [
    PARAM_POWER,
    PARAM_BRIGHTNESS,
    PARAM_COLOR_TEMPERATURE,
    PARAM_COLOR,
    PARAM_NAME
]


def create_command(params):
    return create_command_base(
        METHOD,
        validate_params(params)
    )


def validate_params(params):
    for param in params:
        if param not in PARAM_ALL:
            raise Exception(f'Invalid parameter: {param}')

    return params
