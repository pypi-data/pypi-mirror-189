from .command import create_command as create_command_base


METHOD = "set_power"
STATE_ON = 'on'
STATE_OFF = 'off'


def create_command(state):
    return create_command_base(
        METHOD,
        [
            validate_state(state)
        ]
    )


def validate_state(state):
    if state not in [STATE_ON, STATE_OFF]:
        raise Exception('Invalid state: ' + state)

    return state
