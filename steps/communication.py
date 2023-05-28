# connect all devices declared in dictionary
def devices_connect(resource_manager, device_dict):
    connections = []
    connected_device = []
    for i in device_dict:
        if device_dict[i] is not None:
            try:
                inst = resource_manager.open_resource(device_dict[i])
            except:
                print(f"Connection Error! The device: [{i}] has the wrong address: [{device_dict[i]}]")
                break
            
            connections.append(inst)
            connected_device.append(i)

    return connections, connected_device

# disconnect all devices declared in dictionary
def devices_disconnect(connections):
    if connections:
        for i in range(len(connections)):
            connections[i].close()
            connections.remove(connections[i])
