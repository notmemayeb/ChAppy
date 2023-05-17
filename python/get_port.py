import serial.tools.list_ports

def find_arduino_port(system: str):
    if (system == "Mac"):
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if "usbmodem" in port.name:
                return port
        return None  
    else:
        return None
    

