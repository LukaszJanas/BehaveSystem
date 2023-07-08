from behave import *
import pyvisa as visa
import SCPI_commands as commands
import device_configuration as dev_con
import communication
import time
import tools

def get_device_index(context, name):
    return context.connected_device.index(name)

def getCmd(context):
    return context.device_class[get_device_index(context, context.usedDevice)]

def readMsg(context):
    return context.connections[get_device_index(context, context.usedDevice)].read()

def write_msg(context, cmd):
    context.connections[get_device_index(context, context.usedDevice)].write(cmd)
    
@step("Czekaj {seconds} sekund")
def step_impl(context, seconds):
    time.sleep(float(seconds))
    
@step("Zmierz wartości: {measurement_type} dla urządzenia: {device} przez {min} min co {sek} sek i zapisz do pliku: {file}")
def step_impl(context, measurement_type, device, min, sek, file):
    
    context.usedDevice = device
    time_start = time.time()
    time_end = time_start + int(min) * 60
    
    if device == 'Rigol':
        while time.time() < time_end:
            if measurement_type == "VDC":
                write_msg(context, getCmd(context).MeasureVoltage("DC"))
            elif measurement_type == "VAC":
                write_msg(context, getCmd(context).MeasureVoltage("AC"))
            elif measurement_type == "IDC":
                write_msg(context, getCmd(context).MeasureCurrent("DC"))
            elif measurement_type == "IAC":
                write_msg(context, getCmd(context).MeasureCurrent("AC"))
            
            try:
                f_value = float(readMsg(context))
                tools.write_to_file(f_value, measurement_type, file)
            except ValueError:
                print("Niepoprawna wartość napięcia.")
                              
            time.sleep(int(sek))

@step("Wyrysuj wykres ze zmiennych z pliku: {name}")
def step_impl(context, name):
    tools.plot_from_txt_file(name)

@step("Odczytaj prąd: {param} dla urządzenia: {name}")
def step_impl(context, name: str, param: str):
    context.usedDevice = name
    write_msg(context, getCmd(context).MeasureCurrent(param))
    print(float(readMsg(context)))
    
@step("Odczytaj napięcie: {param} dla urządzenia: {name}")
def step_impl(context, name: str, param: str):
    context.usedDevice = name
    write_msg(context, getCmd(context).MeasureVoltage(param))
    print(float(readMsg(context)))
    
@step("Odczytaj rezystancję 2W dla urządzenia: {name}")
def step_impl(context, name: str):
    context.usedDevice = name
    write_msg(context, getCmd(context).MeasureResistance())
    print(float(readMsg(context)))
    
@step("Ustaw zakres napięcia: {type} na: {param}V dla urządzenia Rigol")
def step_impl(context, type: str, param: str):
    context.usedDevice = "Rigol"
    if type == "DC":
        write_msg(context, getCmd(context).SetMeasureRangeVDC(param))
    
    if type == "AC":
       write_msg(context, getCmd(context).SetMeasureRangeVAC(param))
       
@step("Ustaw zakres prądu: {type} na: {param}A dla urządzenia Rigol")
def step_impl(context, type: str, param: str):
    context.usedDevice = "Rigol"
    if type == "DC":
        write_msg(context, getCmd(context).SetMeasureRangeIDC(param))
    
    if type == "AC":
       write_msg(context, getCmd(context).SetMeasureRangeIAC(param))

@step("Ustaw tryb pomiaru: {type} dla pomiaru: {measurement} dla urządzenia Rigol")
def step_impl(context, type: str, measurement: str):
    context.usedDevice = "Rigol"
    """
    Step it is used for setting type of measurement, there is only two way of use this cmd
    Mode:
        AUTO - means that multimeter automaticcaly set the range and resolution for current measurement
        MANU - means that user should set the range and resolution for current measurement

    """
    if measurement == "VDC":
        write_msg(context, getCmd(context).MeasureVoltage("DC"))
    if measurement == "VAC":
        write_msg(context, getCmd(context).MeasureVoltage("AC"))
    if measurement == "IDC":
        write_msg(context, getCmd(context).MeasureCurrent("DC"))
    if measurement == "IAC":
        write_msg(context, getCmd(context).MeasureCurrent("AC"))
    if measurement == "R2W":
        write_msg(context, getCmd(context).MeasureResistance())
    
    write_msg(context, getCmd(context).SetMeasurementType(type))