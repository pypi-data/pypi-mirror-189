from .command import validate_effect, validate_duration, create_command as create_command_base


METHOD = 'set_bright'
MIN_BRIGHTNESS = 1
MAX_BRIGHTNESS = 100


def create_command(brightness, effect, duration=30):
    return create_command_base(
        METHOD,
        [
            validate_brightness(brightness),
            validate_effect(effect),
            validate_duration(duration)
        ]
    )


def validate_brightness(brightness):
    if type(brightness) is not int:
        raise Exception('Brightness must be given as int')

    if brightness < MIN_BRIGHTNESS or brightness > MAX_BRIGHTNESS:
        raise Exception('Brightness value out of range 1-100')

    return brightness
