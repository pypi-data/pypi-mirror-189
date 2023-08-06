from .command import validate_duration, validate_effect, create_command as create_command_base


METHOD = 'set_ct_abx'
MIN_TEMP = 1700
MAX_TEMP = 6500


def create_command(temp, effect, duration=30):
    return create_command_base(
        METHOD,
        [
            validate_temp(temp),
            validate_effect(effect),
            validate_duration(duration)
        ]
    )


def validate_temp(temp):
    if type(temp) is not int:
        raise Exception('Color temperature must be given as int')

    if temp < MIN_TEMP or temp > MAX_TEMP:
        raise Exception('Temperature value must be in the range 1700-6500')

    return temp
