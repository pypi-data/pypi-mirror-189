from .command import validate_duration, validate_effect, create_command as create_command_base

METHOD = 'set_rgb'
MIN_COLOR = 0
MAX_COLOR = 16777215


def create_command(color, effect, duration=30):
    return create_command_base(
        METHOD,
        [
            validate_color(color),
            validate_effect(effect),
            validate_duration(duration)
        ]
    )


def validate_color(color):
    if type(color) is not int:
        raise Exception('Color must be given as int')

    if color < MIN_COLOR or color > MAX_COLOR:
        raise Exception('Color is out of range 0-16777215')

    return color
