EFFECT_SUDDEN = 'sudden'
EFFECT_SMOOTH = 'smooth'
MIN_DURATION = 30


def create_command(method, params):
    return {
        "id": 1,
        "method": method,
        "params": params
    }




def validate_effect(effect):
    if effect not in [EFFECT_SUDDEN, EFFECT_SMOOTH]:
        raise Exception('Effect must be one of [' + EFFECT_SUDDEN + ', ' + EFFECT_SMOOTH + ']')

    return effect


def validate_duration(duration):
    if type(duration) is not int:
        raise Exception('Duration must be given as int')

    if duration < MIN_DURATION:
        raise Exception('Duration must be greater than or equal to 30')

    return duration

