"""

The file contains functionalities provided by behave, which enable, for example, 
the execution of actions before the end or start of a given test scenario

Developed by:
Inż. Janas Łukasz

Last changes:
17.07.2023

"""

import pyvisa as visa
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
steps_dir = os.path.join(current_dir, "steps")
sys.path.append(steps_dir)

import communication
import device_configuration as dev_con


def before_scenario(context):
    context.rm = visa.ResourceManager()
    context.connections, context.connected_device, context.device_class = communication.devices_connect(context.rm, dev_con.Devices)
    
# def after_scenario(context):
#     communication.devices_disconnect(context.connections)