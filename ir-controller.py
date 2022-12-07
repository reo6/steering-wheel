#!/usr/bin/env python3

"""
Simple pyautogui controller for gas, brake, horn and things like that.
This is supposed to run as an external script besides mouse2steer.py
"""
import serial
from threading import Thread
from pyautogui import keyDown, keyUp, press

PORT = "/dev/ttyUSB0"

class Signals:
    SIDE_LEFT     = "3860463360"
    SIDE_RIGHT    = "4061003520"
    HORN          = "3158572800"
    ESC           = "4127850240"
    SPEED_LIMITER = "3108437760"

    SPEED_LIMITER_INCREASE = "3091726080"
    SPEED_LIMITER_DECREASE = "3125149440"
    SPEED_LIMITER_RESUME   = "3910598400"

    LOOK_LEFT = "3175284480"
    LOOK_RIGHT = "3041591040"
    LOOK_RESET = "2907897600"


MAPPING = {
    Signals.HORN: "h",
    Signals.ESC: "ESC",
    Signals.SPEED_LIMITER: "c",
    Signals.SPEED_LIMITER_INCREASE: ".",
    Signals.SPEED_LIMITER_DECREASE: ",",
    Signals.SPEED_LIMITER_RESUME: "/",
    Signals.LOOK_LEFT: 'num7',
    Signals.LOOK_RIGHT: 'num9',
    Signals.LOOK_RESET: 'num5',
    Signals.SIDE_LEFT: "[",
    Signals.SIDE_RIGHT: "]",
}

def safe_get_dict(d, elem):
    try:
        return d[elem]
    except KeyError:
        return None

def main():
    ser = serial.Serial(PORT)

    try:
        while True:
            signal = ser.readline().decode('ASCII').strip()

            if signal.startswith("-1"):
                if int(signal[2]):
                    keyDown("w")
                else:
                    keyUp("w")
                continue

            if signal.startswith("-2"):
                if int(signal[2]):
                    keyDown("s")
                else:
                    keyUp("s")
                continue

            keyname = safe_get_dict(MAPPING, signal)
            keyname = keyname if keyname is not None else ""
            press(keyname)

    except KeyboardInterrupt:
        ser.close()

if __name__ == "__main__":
    main()
