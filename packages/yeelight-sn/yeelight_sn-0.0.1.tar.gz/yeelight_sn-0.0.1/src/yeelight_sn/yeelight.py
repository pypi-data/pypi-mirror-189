from . import commands
import json
from .network import dispatch


class Yeelight:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def __str__(self):
        status = self.get_status()
        return str(status)

    def send_command(self, command):
        dispatch.send_command(self.ip_address, command)

    def get_status(self):
        cmd = commands.get_prop.create_command(commands.get_prop.PARAM_ALL)
        response = dispatch.send_command(self.ip_address, cmd)
        values = json.loads(response)['result']

        status = {}
        for i in range(0, len(values)):
            status[commands.get_prop.PARAM_ALL[i]] = values[i]

        status['ip'] = self.ip_address

        return status

    def turn_on(self):
        cmd = commands.set_power.create_command(commands.set_power.STATE_ON)
        self.send_command(cmd)

    def turn_off(self):
        cmd = commands.set_power.create_command(commands.set_power.STATE_OFF)
        self.send_command(cmd)

    def set_brightness(self, brightness):
        cmd = commands.set_brightness.create_command(brightness, commands.EFFECT_SUDDEN)
        self.send_command(cmd)

    def set_color(self, color):
        cmd = commands.set_color.create_command(color, commands.EFFECT_SUDDEN)
        self.send_command(cmd)

    def set_color_temp(self, temp):
        cmd = commands.set_color_temp.create_command(temp, commands.EFFECT_SUDDEN)
        self.send_command(cmd)
