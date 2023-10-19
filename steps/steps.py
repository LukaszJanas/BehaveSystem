"""

The file contains a description of the test steps that can be used in creating test scenarios

Developed by:
Inż. Janas Łukasz

Last changes:
17.07.2023

"""

from behave import *
import pyvisa as visa
import SCPI_commands as commands
import device_configuration as dev_con
import communication
import time
import tools

def getDeviceIndex(context, name):
    return context.connected_device.index(name)

def getCmd(context):
    return context.device_class[getDeviceIndex(context, context.usedDevice)]

def readMsg(context):
    return context.connections[getDeviceIndex(context, context.usedDevice)].read()

def writeMsg(context, cmd):
    time.sleep(0.5)
    context.connections[getDeviceIndex(context, context.usedDevice)].write(cmd)
    
@step("Wait {seconds}s")
def step_impl(context, seconds):
    time.sleep(float(seconds))
    tools.write_log(f'Device: System -> Wait time: {seconds}s', "log.txt")
    
@step("Measure the value of: {measurement_type} for device: {device} for {min} every {sek}s and save to file: {file}")
def step_impl(context, measurement_type, device, min, sek, file):
    
    context.usedDevice = device
    time_start = time.time()
    time_end = time_start + int(min) * 60
    
    if device == 'Rigol':
        while time.time() < time_end:
            if measurement_type == "VDC":
                writeMsg(context, getCmd(context).MeasureVoltage("DC"))
            elif measurement_type == "VAC":
                writeMsg(context, getCmd(context).MeasureVoltage("AC"))
            elif measurement_type == "IDC":
                writeMsg(context, getCmd(context).MeasureCurrent("DC"))
            elif measurement_type == "IAC":
                writeMsg(context, getCmd(context).MeasureCurrent("AC"))
            
            try:
                f_value = float(readMsg(context))
                tools.write_to_file(f_value, measurement_type, file)
            except ValueError:
                print("Incorrect voltage value.")
                              
            time.sleep(int(sek))

@step("Plot a graph from the variables in the file: {name}")
def step_impl(context, name):
    tools.plot_from_txt_file(name)
    
@step("Read the 2W resistance for the device: {name}")
def step_impl(context, name: str):
    context.usedDevice = name
    writeMsg(context, getCmd(context).MeasureResistance())
    context.resistance = float(readMsg(context))
    tools.write_log(f'Device: {context.usedDevice} -> Resistance: {context.resistance} Ohm', "log.txt")

@step("Set voltage range for type: {type} to: {param}V for Rigol")
def step_impl(context, type: str, param: str):
    context.usedDevice = "Rigol"
    if type == "DC":
        writeMsg(context, getCmd(context).SetMeasureRangeVDC(param))
    
    if type == "AC":
        writeMsg(context, getCmd(context).SetMeasureRangeVAC(param))
    
    tools.write_log(f'Device: {context.usedDevice} -> {type} voltage range set to range {param}', "log.txt")
 
@step('Set current range for type: "{type}" to: "{param}"A for Rigol')
def step_impl(context, type: str, param: str):
    context.usedDevice = "Rigol"
    if type == "DC":
        writeMsg(context, getCmd(context).SetMeasureRangeIDC(param))
    
    if type == "AC":
        writeMsg(context, getCmd(context).SetMeasureRangeIAC(param))
       
    tools.write_log(f'Device: {context.usedDevice} -> {type} current range set to range {param}', "log.txt")


@step('Set the type: "{type}" for measurement: "{measurement}" for Rigol')
def step_impl(context, type: str, measurement: str):
    context.usedDevice = "Rigol"
    """
    Step it is used for setting type of measurement, there is only two way of use this cmd
    Mode:
        Automatic - means that multimeter automaticcaly set the range and resolution for current measurement
        Manual - means that user should set the range and resolution for current measurement

    """
    if measurement == "VDC":
        writeMsg(context, getCmd(context).MeasureVoltage("DC"))
    if measurement == "VAC":
        writeMsg(context, getCmd(context).MeasureVoltage("AC"))
    if measurement == "IDC":
        writeMsg(context, getCmd(context).MeasureCurrent("DC"))
    if measurement == "IAC":
        writeMsg(context, getCmd(context).MeasureCurrent("AC"))
    if measurement == "R2W":
        writeMsg(context, getCmd(context).MeasureResistance())
    
    writeMsg(context, getCmd(context).SetMeasurementType(type))
    
    tools.write_log(f'Device: {context.usedDevice} -> Measurement {measurement} type is set to: {type}', "log.txt")

# __________________________________________________________________________________________________
@step('Turn "{state}" Chroma Output')
def step_impl(context, state: str):
    context.usedDevice = "Chroma"
    writeMsg(context, getCmd(context).SetOutput(state))
    writeMsg(context, "OUTPut ON")
    tools.write_log(f'Device: {context.usedDevice} -> Turn {state} device', "log.txt")

@step('Set the AC voltage amplitude: "{amplitude}" V for Chroma')
def step_impl(context, amplitude: str):
    context.usedDevice = "Chroma"
    writeMsg(context, getCmd(context).SetVoltageAC(amplitude))
    tools.write_log(f'Device: {context.usedDevice} -> AC voltage amplitude is set to: {amplitude}', "log.txt")

@step('Read the "{type}" current from the "{device}"')   
def step_impl(context, type: str, device: str):
    context.usedDevice = device
    writeMsg(context, getCmd(context).MeasureCurrent(type))
    context.voltage = float(readMsg(context))
    tools.write_log(f'Device: {context.usedDevice} -> Current: {context.voltage} A', "log.txt")

@step('Read the "{type}" voltage from the "{device}"')   
def step_impl(context, type: str, device: str):
    context.usedDevice = device
    writeMsg(context, getCmd(context).MeasureVoltage(type))
    context.voltage = float(readMsg(context))
    tools.write_log(f'Device: {context.usedDevice} -> Voltage: {context.voltage} V', "log.txt")

@step('Set the AC voltage amplitude: "{level}" V for the phase "{phase}" for Chroma')
def step_impl(context, level: str, phase: str):
    context.usedDevice = "Chroma"
    writeMsg(context, getCmd(context).SetPhasesToProgram("Each"))
    writeMsg(context, getCmd(context).SetPhase(phase))
    writeMsg(context, getCmd(context).SetVoltageAC(level))
    tools.write_log(f'Device: {context.usedDevice} -> AC voltage amplitude: {level} for phase {phase} is set', "log.txt")
    
@step('Setting all phases for Chroma')
def step_impl(context):
    context.usedDevice = "Chroma"
    writeMsg(context, getCmd(context).SetPhasesToProgram("All"))
    tools.write_log(f'Device: {context.usedDevice} -> Setting parameters for all phases', "log.txt")

@step('Turn "{state}" Itech')
def step_impl(context, state: str):
    context.usedDevice = "Itech"
    writeMsg(context, getCmd(context).SetInput(state))
    tools.write_log(f'Device: {context.usedDevice} -> Turn {state} device', "log.txt")

@step('Set load method: "{method}" for Itech')
def step_impl(context, method: str):
    context.usedDevice = "Itech"
    writeMsg(context, getCmd(context).SetLoop(method))
    tools.write_log(f'Device: {context.usedDevice} -> Load method set to: {method}', "log.txt")

@step('Set: "{param}" to: "{level}" for Itech')
def step_impl(context, param: str, level: str):
    context.usedDevice = "Itech"
    writeMsg(context, getCmd(context).SetParamLevel(param, level))
    tools.write_log(f'Device: {context.usedDevice} -> Parameter: {param} set to value: {level}', "log.txt")
    
@step('Expect voltage is in the range: <"{range}"> V')   
def step_impl(context, range: str):
    inRange = False
    left_band = float(range.split("-")[0])
    right_band = float(range.split("-")[1])
    
    if left_band >= right_band:
        raise Exception("Left band bigger or equal than right band") 
    
    if context.voltage >= left_band and context.voltage <= right_band:
        inRange = True
        tools.write_log(f'Device: {context.usedDevice} -> Voltage is in expected range', "log.txt")
        
    assert inRange, f"The read voltage is out of range, got: {context.voltage}"
    
@step('Expect current is in the range: <"{range}"> A')   
def step_impl(context, range: str):
    inRange = False
    context.current = 12
    left_band = float(range.split("-")[0])
    right_band = float(range.split("-")[1])
    
    if left_band >= right_band:
        raise Exception("Left band bigger or equal than right band") 
    
    if context.current >= left_band and context.current <= right_band:
        inRange = True
        tools.write_log(f'Device: {context.usedDevice} -> Current is in expected range', "log.txt")
        
    assert inRange, f"The read current is out of range, got: {context.current}"

@step('Expect power is in the range: <"{range}">')   
def step_impl(context, range: str):
    inRange = False
    left_band = float(range.split("-")[0])
    right_band = float(range.split("-")[1])
    
    if left_band >= right_band:
        raise Exception("Left band bigger or equal than right band") 
    
    if context.power >= left_band and context.power <= right_band:
        inRange = True
        tools.write_log(f'Device: {context.usedDevice} -> Power is in expected range', "log.txt")
        
    assert inRange, f"The read power is out of range, got: {context.voltage}"

@step('Measure "{type}" power for Chroma')
def step_impl(context, type: str):
    context.usedDevice = "Chroma"
    if type == "real":
        writeMsg(context, getCmd(context).MeasureRealPower())
        context.power = float(readMsg(context))
        tools.write_log(f'Device: {context.usedDevice} -> Real power: {context.power} W', "log.txt")
    if type == "apparent":
        writeMsg(context, getCmd(context).MeasureApparentPower())
        context.power = float(readMsg(context))
        tools.write_log(f'Device: {context.usedDevice} -> Apparent power: {context.power} VA', "log.txt")
    if type == "reactive":
        writeMsg(context, getCmd(context).MeasureReactivePower())
        context.power = float(readMsg(context))
        tools.write_log(f'Device: {context.usedDevice} -> Reactive power: {context.power} VAr', "log.txt")
        
@step('Measure 3-phase "{type}" power for Chroma')
def step_impl(context, type: str):
    context.usedDevice = "Chroma"
    if type == "real":
        writeMsg(context, getCmd(context).Measure3PhaseRealPower())
        context.power = float(readMsg(context))
        tools.write_log(f'Device: {context.usedDevice} -> 3-phase real power: {context.power} W', "log.txt")
    if type == "apparent":
        writeMsg(context, getCmd(context).Measure3PhaseApparentPower())
        context.power = float(readMsg(context))
        tools.write_log(f'Device: {context.usedDevice} -> 3-phase apparent power: {context.power} VA', "log.txt")
        
@step('Measure power factor for Chroma')
def step_impl(context):
    context.usedDevice = "Chroma"
    writeMsg(context, getCmd(context).MeasurePowerFactor())
    context.PowerFactor = float(readMsg(context))
    tools.write_log(f'Device: {context.usedDevice} -> Power factor: {context.PowerFactor}', "log.txt")