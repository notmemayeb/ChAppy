from get_os import get_operating_system
from get_port import find_arduino_port
from AppKit import NSWorkspace, NSApplication, NSApp, NSRunningApplication

from time import sleep
from exc import ArduinoNotConnectedError
import serial
import subprocess
import objc

data = b''

arduino_port = find_arduino_port(get_operating_system())
if arduino_port:
    print("Arduino is conected to", arduino_port.device)
    ser = serial.Serial(arduino_port.device, 9600)
    print("Listening to arduino signal on", arduino_port.device)

    try:
        while True:
            priv = data
            data = ser.read()
            if data == b'A':
                if priv != data:
                    print("Warning, somebody is coming!")
                running_apps = NSWorkspace.sharedWorkspace().runningApplications()

                current_app = NSRunningApplication.currentApplication()

                for app in running_apps:
                    if app != current_app:
                        app.hide()
            elif data ==  b'Q':
                if priv != data:
                    print("All quiet")
            else:
                print("Arduino is already used by some subprocess")
                break;
            #     raise ArduinoNotConnectedError
    except serial.serialutil.SerialException as _exc:
        print("Arduino not found")
else:
    print("Arduino is not connected")
    raise ArduinoNotConnectedError;
