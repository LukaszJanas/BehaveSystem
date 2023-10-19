"""

This file contains useful SCPI commands that are used to perform automated tests
SCPI commands are contained in methods implemented in defined classes for specific devices

Developed by:
Inż. Janas Łukasz

Last changes:
17.07.2023

"""

def AddPrefixIfNeeded(command, prefix):
    return ":" + command if prefix else command


class ScpiCommand:
    
    PARAM = {
        "Current" : "CURRent",
        "Resistance" : "RESistance",
        "Power" : "POWer",
        "Voltage": "VOLTage"
        }
    
    TYPE = {
        "DC" : "DC",
        "AC" : "AC"
    }
    
    def __init__(self, usePrefix = True):
        self.usePrefix = usePrefix
    
    def MeasureVoltage(self, variant):
        #Method queries the current measured DC or AC voltage value.
        return AddPrefixIfNeeded(f"MEASure:VOLTage:{self.TYPE.get(variant, 'AC')}?", self.usePrefix)
    
    def MeasureCurrent(self, variant):
        #Method queries the current measured DC or AC current value.
        return AddPrefixIfNeeded(f"MEASure:CURRent:{self.TYPE.get(variant, 'AC')}?", self.usePrefix)
    
    def MeasureResistance(self):
        #Method queries the measured 2-wire resistance value. 
        return AddPrefixIfNeeded("MEASure:RESistance?", self.usePrefix)

class Chroma(ScpiCommand):
    
    def __init__(self, usePrefix):
        super().__init__(usePrefix)
        
        self.STATE = {
            "On" : "ON",
            "Off": "OFF"
        }
        
        self.PHASES = {
            "All" : "ALL",
            "Each": "EACH"
        }
        
        self.COUPLE = {
            "All" : "ALL",
            "None": "NONE"
        }
        
        self.OUTPUT ={
            "A" : "OUTPUT1",
            "B" : "OUTPUT2",
            "C" : "OUTPUT3"
        }
        
    def SetOutput(self, state):
        return f"OUTPut {self.STATE.get(state, 'OFF')}"
    
    def SetVoltageAC(self, amplitude):
        return f"VOLTage:AMPLitude:AC {amplitude}"
    
    def SetPhasesToProgram(self, phases):
        return f"INSTrument:EDIT {self.PHASES.get(phases, 'ALL')}"
        
    def SetPhase(self, phase):
        return f"INSTrument:SELect {self.OUTPUT.get(phase, 'OUTPUT1')}"
    
    def MeasureRealPower(self):
        return f"MEASure:POWer:AC?"
    
    def MeasureApparentPower(self):
        return f"MEASure:POWer:AC:APParent?"
    
    def MeasureReactivePower(self):
        return f"MEASure:POWer:AC:REACtive?"
    
    def Measure3PhaseRealPower(self):
        return f"MEASure:POWer:AC:TOTal?"
    
    def Measure3PhaseApparentPower(self):
        return f"MEASure:POWer:AC:TOTal:APParent?"
    
    def MeasurePowerFactor(self):
        return f"MEASure:POWer:AC:PFACtor?"

    
    
class Itech(ScpiCommand):
    
    def __init__(self, usePrefix):
        super().__init__(usePrefix)
        
        self.STATE = {
            "On" : "ON",
            "Off": "OFF"
        }
        
        self.MODE = {
            "ConstantCurrent" : "CC",
            "ConstantPower": "CP",
            "ConstantResistance": "CR"
        }
    
    def SetInput(self, state):
        return f"SOURce:INPut:STATe {self.STATE.get(state, 'OFF')}"
    
    def SetLoop(self, mode):
        return f"SOURce:LOOP:MODE {self.MODE.get(mode, 'CP')}"
    
    def SetParamLevel(self, param, level):
        return f"SOURce:{self.PARAM.get(param, 'CURRent')}:LEVel {str(level)}"
    
class Rigol(ScpiCommand):
    
    RangeVDC = {
        "0.2":  0,  #0 - Range = 200mV and Resolution = 100nV
        "2":    1,  #1 - Range = 2V and Resolution = 1uV
        "20":   2,  #2 - Range = 20V and Resolution = 10uV
        "200":  3,  #3 - Range = 200V and Resolution = 100uV
        "1000": 4,  #4 - Range = 1000V and Resolution = 100mV
    }

    RangeVAC = {
        "0.2":  0,  #0 - Range = 200mV
        "2":    1,  #1 - Range = 2V
        "20":   2,  #2 - Range = 20V
        "200":  3,  #3 - Range = 200V
        "750":  4,  #4 - Range = 750V
    }

    RangeIDC = {
        "0.0002":  0,  #0 - Range = 200uA and Resolution = 1nA
        "0.002":   1,  #1 - Range = 2mA and Resolution = 10nA
        "0.02":    2,  #2 - Range = 20mA and Resolution = 100nA
        "0.2":     3,  #3 - Range = 200mA and Resolution = 1uA
        "2":       4,  #4 - Range = 2A and Resolution = 10uA
        "10":      5,  #5 - Range = 10A and Resolution = 100 uA
    }

    RangeIAC = {
        "0.02":  0,  #0 - Range = 20mA
        "0.2":   1,  #1 - Range = 200mA
        "2":     2,  #2 - Range = 2A
        "10":    3,  #3 - Range = 10A
    }

    Range2W = {
        "200"   :  0,  #0 - Range = 200 Ohm
        "2000"  :  1,  #1 - Range = 2 kOhm
        "2e+4"  :  2,  #2 - Range = 20 kOhm
        "20e+4" :  3,  #3 - Range = 200 kOhm
        "1e+6"  :  4,  #0 - Range = 1 MOhm
        "10e+6" :  5,  #1 - Range = 10 MOhm
        "100e+6":  6   #2 - Range = 100 MOhm
    }
    
    MeasureType = {
        "Automatic" : "AUTO",
        "Manual" : "MANU"
    }
    
    def __init__(self, usePrefix):
        super().__init__(usePrefix)
    
    def SetMeasureRangeVDC(self, value):
        return f":MEASure:VOLTage:DC {self.RangeVDC.get(value, '4')}"
    
    def SetMeasureRangeVAC(self, value):
        return f":MEASure:VOLTage:AC {self.RangeVAC.get(value, '4')}"
    
    def SetMeasureRangeIDC(self, value):
        return f":MEASure:CURRent:DC {self.RangeIDC.get(value, '5')}"
    
    def SetMeasureRangeIAC(self, value):
        return f":MEASure:CURRent:AC {self.RangeIDC.get(value, '3')}"
    
    def SetMeasureRangeR2W(self, value):
        return f":MEASure:RESistance {self.Range2W.get(value, '6')}"
    
    def SetMeasurementType(self, type):
        return f":MEASure {self.MeasureType.get(type, 'AUTO')}"
    
def ClassCreator(object_name):
    if object_name == "Itech":
        return Itech(usePrefix = True)
    if object_name == "Rigol":
        return Rigol(usePrefix = True)
    if object_name == "Chroma":
        return Chroma(usePrefix = False)