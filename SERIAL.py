from time import *
import serial
def WRITE(String):
    ser = serial.Serial(

        port="/dev/ttyS0",
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    ser.write(bytes(String, "utf-8"))
    ser.close()

def READ():
    ser = serial.Serial(

        port="/dev/ttyS0",
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    Temp = ""
    String = ""
    ser.read()
    while True:
        Temp = chr(ord(ser.read()))
        String += Temp
        if Temp == "~":
            return String.replace("~", "")
