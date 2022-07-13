import pyautogui
import serial

WIDTH, HEIGHT = pyautogui.size()
PORT = "/dev/ttyUSB0"

ser = serial.Serial(PORT)


def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


last_value = -1
while True:
    value = int(ser.readline())
    if value == last_value:
        continue
    last_value = value

    pyautogui.moveTo(map_range(value, 0, 1023, 0, WIDTH), HEIGHT//2, _pause=False)