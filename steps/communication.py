"""

The file contains functionalities related to creating a connection or closing a connection with assigned measuring devices

Developed by:
Inż. Janas Łukasz

Last changes:
17.07.2023

"""

import SCPI_commands as command
# connect all devices declared in dictionary
def devices_connect(resource_manager, device_dict):
    connections = []
    connected_device = []
    device_class = []
    for i in device_dict:
        if device_dict[i] is not None:
            try:
                inst = resource_manager.open_resource(device_dict[i])
            except:
                print(f"Connection Error! The device: [{i}] has the wrong address: [{device_dict[i]}]")
                break
            
            connections.append(inst)
            connected_device.append(i)
            device_class.append(command.ClassCreator(i))

    return connections, connected_device, device_class

# disconnect all devices declared in dictionary
def devices_disconnect(connections):
    if connections:
        for i in range(len(connections)):
            connections[i].close()
