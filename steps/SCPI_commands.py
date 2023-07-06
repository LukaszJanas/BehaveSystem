"""

This file contains useful SCPI command which are available for configured devices.
When using devices that are not supported by the software, add the configuration 
for the new device "if the new device supports communication in the SCPI language"

Developed by:
Inż. Janas Łukasz

Last changes:
09.05.2023

"""
RIGOL_DM3068_DC_voltage_range = {
    "0.2":  0,  #0 - Range = 200mV and Resolution = 100nV
    "2":    1,  #1 - Range = 2V and Resolution = 1uV
    "20":   2,  #2 - Range = 20V and Resolution = 10uV
    "200":  3,  #3 - Range = 200V and Resolution = 100uV
    "1000": 4,  #4 - Range = 1000V and Resolution = 100mV
}

RIGOL_DM3068_AC_voltage_range = {
    "0.2":  0,  #0 - Range = 200mV
    "2":    1,  #1 - Range = 2V
    "20":   2,  #2 - Range = 20V
    "200":  3,  #3 - Range = 200V
    "750":  4,  #4 - Range = 750V
}

RIGOL_DM3068_DC_current_range = {
    "0.0002":  0,  #0 - Range = 200uA and Resolution = 1nA
    "0.002":   1,  #1 - Range = 2mA and Resolution = 10nA
    "0.02":    2,  #2 - Range = 20mA and Resolution = 100nA
    "0.2":     3,  #3 - Range = 200mA and Resolution = 1uA
    "2":       4,  #4 - Range = 2A and Resolution = 10uA
    "10":      5,  #5 - Range = 10A and Resolution = 100 uA
}

RIGOL_DM3068_AC_current_range = {
    "0.02":  0,  #0 - Range = 20mA
    "0.2":   1,  #1 - Range = 200mA
    "2":     2,  #2 - Range = 2A
    "10":    3,  #3 - Range = 10A
}

RIGOL_DM3068_2W_resistance_range = {
    "200"   :  0,  #0 - Range = 200 Ohm
    "2000"  :  1,  #1 - Range = 2 kOhm
    "2e+4"  :  2,  #2 - Range = 20 kOhm
    "20e+4" :  3,  #3 - Range = 200 kOhm
    "1e+6"  :  4,  #0 - Range = 1 MOhm
    "10e+6" :  5,  #1 - Range = 10 MOhm
    "100e+6":  6   #2 - Range = 100 MOhm
}

CHROMA_61511_current_range = {
    "8" : 1,
    "32" : 2,
    "128" : 3,
    "AUTO" : "Auto",
}

RIGOL_DM3068 = {
    # MEASURE query
    "VDC": ":MEASure:VOLTage:DC?",  #The command queries the current measured DC voltage value.
    "VAC": ":MEASure:VOLTage:AC?",  #The command queries the measured AC current value.
    "IDC": ":MEASure:CURRent:DC?",  #The command queries the measured DC current value.
    "IAC": ":MEASure:CURRent:AC?",  #The command queries the measured AC current value.
    "R"  : ":MEASure:RESistance?",  #The command queries the measured 2-wire resistance value.
    # CONFIGURATION
    "CfgRangeVDC": ":MEASure:VOLTage:DC",   #The command sets the range and resolution of DC voltage measurement.
    "CfgRangeVAC": ":MEASure:VOLTage:AC",   #The command sets the range of AC voltage measurement.
    "CfgRangeIDC": ":MEASure:CURRent:DC",   #The command sets the range and resolution of DC current measurement.
    "CfgRangeIAC": ":MEASure:CURRent:AC",   #The command sets the AC current range.
    "CfgRangeR"  : ":MEASure:RESistance",   #The command sets the desired 2-wire resistance range.
    "CfgMeasType": ":MEASure"               #The command selects the measurement type as Auto or Manual.
}

CHROMA_61511 = {
    # MEASURE query
    "VDC": "MEASure:VOLTage:DC?",  #The command queries the current measured DC voltage value.
    "VAC": "MEASure:VOLTage:AC?",  #The command queries the measured AC current value.
    "IDC": "MEASure:CURRent:DC?",  #The command queries the measured DC current value.
    "IAC": "MEASure:CURRent:AC?",  #The command queries the measured AC current value.
    "R"  : "MEASure:RESistance?",  #The command queries the measured 2-wire resistance value.
    "F"  : "MEASure:FREQuency?",   #These queries return the output frequency in Hertz.
    "VAmplMax" : "MEASur:VOLTage:AMPLitude:MAXimum?", #These queries return the rms that is output from the output terminal.
    "VLINE":  "MEASure:LINE:V12?",   #These queries return the line voltage between phase 1 and 2.
    "V23":  "MEASure:LINE:V23?",   #These queries return the line voltage between phase 2 and 3.
    "V31":  "MEASure:LINE:V31?",   #These queries return the line voltage between phase 3 and 1
    # OUTPUT
    "OUT": "OUTPut",    #This command enables or disables the output of the AC Source. Disabled output is to set the output voltage amplitude to 0 Volt
    "Coupling": "OUTPut : COUPling", #This command selects the coupling of the output signals.
    "OutR" : "OUTPut:IMPedance:RESistor", #This command sets the resistance of output impedance.
    "OutIn": "OUTPut:IMPedance:INDuction", #This command sets the inductance of output impedance.
    # SOURCE
    "SetFreq" : "FREQuency",  #This command sets the output waveform frequency for the AC Source in Hz.
    "SetVAC" : "VOLTage:LEVel:AC", #This command sets the AC level output voltage in Volts
    "SetAmplVAC" : "VOLTage:AMPLitude:AC", #This command sets the AC amplitude output voltage in Volts
    "SetVDC" : "VOLTage:LEVel:AC", #This command sets the DC level output voltage in Volts
    "SetAmplVDC" : "VOLTage:AMPLitude:DC", #This command sets the DC amplitude output voltage in Volts
    "SetCurrentRange" : "CURRent:RANGe", #This command sets the current measurement range for output
    # FUNCTION
    "FShape" : "FUNCtion:SHAPe:A", #This command specifies the waveform buffer A for use.
    "InstrumentEdit" : "INSTrument:EDIT", #Select ALL or EACH phases to programm
    "InstrumentCouple" : "INSTrument:COUPle", #Programm all phases or single one
    "InstrumentProgrammPhase": "INSTrument:NSELect", #Set individual output for subsequent commands
    "InstrumentProgrammPhase2": "INSTrument:SELect", #Set individual output for subsequent commands
    "InstrumentPhase": "INSTrument:PHASe" #It switches between single phase and three-phase mode
}

ITECH_IT8600 = {
    # INPUT
    "InputOn": ":SOURce:INPut:STATe ON",
    "InputOff": ":SOURce:INPut:STATe OFF",
    # SET LOOP
    "SetLoopCC": ":SOURce:LOOP:MODE CC",
    "SetLoopCR": ":SOURce:LOOP:MODE CR",
    "SetLoopCP": ":SOURce:LOOP:MODE CP",
    # QUERY LOOP
    "WhichLoop": ":SOURce:LOOP:MODE?",
    # SET FUNCTION
    "SetFunctionConstCurrent": ":SOURce:FUNCtion CURRent",
    "SetFunctionConstResistance": ":SOURce:FUNCtion RESistance",
    "SetFunctionConstCPOWer": ":SOURce:FUNCtion POWer",
    "SetResistanceValue": ":SOURce:RESistance:LEVel",
    "SetPowerValue": ":SOURce:POWer:LEVel",
    "SetCurrentValue": ":SOURce:CURRent:LEVel",
    "SetVoltageValue": ":SOURce:VOLTage:LEVel"
}

def AddPrefixIfNeeded(command, prefix):
    return ":"+command if prefix else command


class ScpiCommand:
    
    def __init__(self, usePrefix = True):
        self.usePrefix = usePrefix
    
    def MeasureVoltage(self, variant):
        #Method queries the current measured DC or AC voltage value.
        return AddPrefixIfNeeded(f"MEASure:VOLTage:{variant}?", self.usePrefix)
    
    def MeasureCurrent(self, variant):
        #Method queries the current measured DC or AC current value.
        return AddPrefixIfNeeded(f"MEASure:CURRent:{variant}?", self.usePrefix)
    
    def MeasureResistance(self):
        #Method queries the measured 2-wire resistance value. 
        return AddPrefixIfNeeded("MEASure:RESistance?", self.usePrefix)
    
class ITECH_IT8600(ScpiCommand):
    
    def __init__(self, usePrefix):
        super().__init__(usePrefix)
        
        self.PARAM = {
            "Current" : "CURRent",
            "Resistance" : "RESistance",
            "Power" : "POWer",
            "Voltage": "VOLTage"
        }
        
        self.STATE = {
            "On" : "ON",
            "Off": "OFF"
        }
        
        self.MODE = {
            "ConstantCurrent" : "CC",
            "ConstantPower": "CP",
            "ConstantResistance": "CR"
        }
    
    def SetFunction(self, function):
        return f":SOURce:FUNCtion {self.PARAM.get(function, 'CURRent')}"
    
    def SetInput(self, state):
        return f":SOURce:FUNCtion {self.STATE.get(state, 'OFF')}"
    
    def SetLoop(self, mode):
        return f":SOURce:FUNCtion {self.MODE.get(mode, 'OFF')}"
    
    def SetParamLevel(self, param, level):
        return f":SOURce:{self.PARAM.get(param, 'CURRent')}:LEVel {str(level)}"

def ClassCreator(object_name):
    if object_name == "ITECH_IT8600":
        return ITECH_IT8600(usePrefix = True)