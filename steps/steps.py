from behave import *
import pyvisa as visa
import SCPI_commands as commands
import device_configuration as dev_con
import communication
import time
import tools

@step("Ustaw odczyt napięcia stałego dla urządzenia {device}")
def step_impl(context, device):
    if device == 'Miernik Rigol':
        context.connections[context.connected_device.index("Multimeter_Rigol")].write(commands.RIGOL_DM3068["VDC"])
        DC_value = context.connections[context.connected_device.index("Multimeter_Rigol")].read()

@step("Czekaj {seconds} sekund")
def step_impl(context, seconds):
    time.sleep(float(seconds))
    
@step("Skonfiguruj zakres: {range} {unit} dla pomiaru {measurement_type} urządzeniem: {device}")
def step_impl(context, range, unit, measurement_type, device):
    if device == 'Miernik Rigol':
        try:
            if measurement_type == "VDC":
                context.connections[context.connected_device.index("Multimeter_Rigol")].write(commands.RIGOL_DM3068["CfgRangeVDC"]+f" {commands.RIGOL_DM3068_DC_voltage_range[range]}")
            elif measurement_type == "VAC":
                context.connections[context.connected_device.index("Multimeter_Rigol")].write(commands.RIGOL_DM3068["CfgRangeVAC"]+f" {commands.RIGOL_DM3068_AC_voltage_range[range]}")
            elif measurement_type == "IDC":
                context.connections[context.connected_device.index("Multimeter_Rigol")].write(commands.RIGOL_DM3068["CfgRangeIDC"]+f" {commands.RIGOL_DM3068_DC_current_range[range]}")
            elif measurement_type == "IAC":
                context.connections[context.connected_device.index("Multimeter_Rigol")].write(commands.RIGOL_DM3068["CfgRangeIAC"]+f" {commands.RIGOL_DM3068_AC_current_range[range]}")
            elif measurement_type == "R":
                context.connections[context.connected_device.index("Multimeter_Rigol")].write(commands.RIGOL_DM3068["CfgRangeR"]+f" {commands.RIGOL_DM3068_2W_resistance_range[range]}")
                
        except KeyError:
            print("    !!!!ERROR!!!!")
            print("    Niepoprawne wartości zakresu!!! Ustawienie zakresu automatycznie")
            if measurement_type == "VDC":
                context.connections[context.connected_device.index("Multimeter_Rigol")].write(commands.RIGOL_DM3068["VDC"])
                context.connections[context.connected_device.index("Multimeter_Rigol")].write(commands.RIGOL_DM3068["CfgMeasType"]+f" AUTO")
            elif measurement_type == "VAC":
                context.connections[context.connected_device.index("Multimeter_Rigol")].write(commands.RIGOL_DM3068["VAC"])
                context.connections[context.connected_device.index("Multimeter_Rigol")].write(commands.RIGOL_DM3068["CfgMeasType"]+f" AUTO")
            elif measurement_type == "IDC":
                context.connections[context.connected_device.index("Multimeter_Rigol")].write(commands.RIGOL_DM3068["IDC"])
                context.connections[context.connected_device.index("Multimeter_Rigol")].write(commands.RIGOL_DM3068["CfgMeasType"]+f" AUTO")
            elif measurement_type == "IAC":
                context.connections[context.connected_device.index("Multimeter_Rigol")].write(commands.RIGOL_DM3068["IAC"])
                context.connections[context.connected_device.index("Multimeter_Rigol")].write(commands.RIGOL_DM3068["CfgMeasType"]+f" AUTO")
            elif measurement_type == "R":
                context.connections[context.connected_device.index("Multimeter_Rigol")].write(commands.RIGOL_DM3068["R"])
                context.connections[context.connected_device.index("Multimeter_Rigol")].write(commands.RIGOL_DM3068["CfgMeasType"]+f" AUTO")

@step("Zmierz wartości: {measurement_type} dla urządzenia: {device} przez {min} min co {sek} sek i zapisz do pliku: {file}")
def step_impl(context, measurement_type, device, min, sek, file):
    
    time_start = time.time()
    time_end = time_start + int(min) * 60
    
    if device == 'Miernik Rigol':
        while time.time() < time_end:
            if measurement_type == "VDC":
                context.connections[context.connected_device.index("Multimeter_Rigol")].write(commands.RIGOL_DM3068["VDC"])
            elif measurement_type == "VAC":
                context.connections[context.connected_device.index("Multimeter_Rigol")].write(commands.RIGOL_DM3068["VAC"])
            elif measurement_type == "IDC":
                context.connections[context.connected_device.index("Multimeter_Rigol")].write(commands.RIGOL_DM3068["IDC"])
            elif measurement_type == "IAC":
                context.connections[context.connected_device.index("Multimeter_Rigol")].write(commands.RIGOL_DM3068["IAC"])
            
            try:
                    f_value = float(context.connections[context.connected_device.index("Multimeter_Rigol")].read())
                    tools.write_to_file(f_value, measurement_type, file)
            except ValueError:
                    print("Niepoprawna wartość napięcia.")
                              
            time.sleep(int(sek))

@step("Wyrysuj wykres ze zmiennych z pliku: {name}")
def step_impl(context, name):
    tools.plot_from_txt_file(name)

@step("Ustaw tryb pomiaru na: {MODE}")
def step_impl(context, MODE):
    """
    Step it is used for setting type of measurement, there is only two way of use this command
    Mode:
    AUTO - means that multimeter automaticcaly set the range and resolution for current measurement
    MANU - means that user should set the range and resolution for current measurement

    """
    context.connections[context.connected_device.index("Multimeter_Rigol")].write(commands.RIGOL_DM3068["CfgMeasType"]+f" {MODE}")
    
@step("Krok testowy")
def step_impl(context):
    load = commands.ITECH_IT8600(usePrefix=True)
    print(load.SetFunction("Resistance"))
    print(load.MeasureVoltage("DC"))
    print(load.SetParamLevel("Current", 100))
    print(load.SetInput("On"))
    # context.connections[context.connected_device.index("Multimeter_Rigol")].write('CONFigure:VOLTage:DC ')
    # DC_value = context.connections[context.connected_device.index("Multimeter_Rigol")].read()
    # print(DC_value)    