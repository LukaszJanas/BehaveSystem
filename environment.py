import pyvisa as visa
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
steps_dir = os.path.join(current_dir, "steps")
sys.path.append(steps_dir)

import communication
import device_configuration as dev_con


def before_scenario(context, scenario):
    context.rm = visa.ResourceManager()
    context.connections, context.connected_device = communication.devices_connect(context.rm, dev_con.Devices)
    
def after_scenario(context, scenario):
    communication.devices_disconnect(context.connections)