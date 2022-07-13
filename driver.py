import joystick
import serial
# from pynput.keyboard import Key, Controller
import threading

PORT = "/dev/ttyUSB0"
STEERING_MIN, STEERING_MAX = (-32767, 32767)
ACCEL_MAX = 65535
WHEEL_PREFIX = "WH"
BREAK_PREFIX = "B"
GAS_PREFIX = "G"

v = joystick.VirtualJoystick(name="Reo's Steering Wheel Code")
ser = serial.Serial(PORT)
# cont = Controller()

def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def smooth_progress(f, n, n2):
    for i in range(n, n2, 100):
        f(n)

def a():
    for i in range(last_gas, accel, 100):
        v.emit(_v, accel=i)
        print("ACCEL", accel)
    for i in range(last_break, brk, 100):
        v.emit(_v, brk=i)
        print("BRK", brk)


def accel_set_0(): # Sorry for the dirty code.
    for i in range(0, ACCEL_MAX+1, 100):
        v.emit(_v, accel=i)

def accel_set_max():
    for i in reversed(range(0, ACCEL_MAX+1, 100)):
        v.emit(_v, accel=i)

def brk_set_0():
    for i in range(0, ACCEL_MAX+1, 100):
        v.emit(_v, brk=i)

def brk_set_max():
    for i in reversed(range(0, ACCEL_MAX+1, 100)):
        v.emit(_v, brk=i)


try:
    value = 0
    gas = 1
    _break = 1

    last_gas = 0
    last_break = 0
    while True:
        inp = ser.readline().decode()
        if inp.startswith(WHEEL_PREFIX):
            value = int(inp.strip(WHEEL_PREFIX))
        elif inp.startswith(BREAK_PREFIX):
            _break = int(inp.strip(BREAK_PREFIX))
        elif inp.startswith(GAS_PREFIX):
            gas = int(inp.strip(GAS_PREFIX))
        
        accel = ACCEL_MAX if gas == 1 else 0
        brk = ACCEL_MAX if _break == 1 else 0
        _v = map_range(value, 0, 1023, STEERING_MIN//2, STEERING_MAX//2)
        v.emit(_v)
        
        if last_gas == 0 and accel == ACCEL_MAX:
            threading.Thread(target=lambda: accel_set_max()).start()
        elif last_gas == ACCEL_MAX and accel == 0:
            threading.Thread(target=lambda: accel_set_0()).start()
        
        if last_break == 0 and brk == ACCEL_MAX:
            threading.Thread(target=lambda: brk_set_max()).start()
        elif last_break == ACCEL_MAX and brk == 0:
            threading.Thread(target=lambda: brk_set_0()).start()


        last_gas = accel
        last_break = brk

        # print("Value: ", value, "Break: ", ACCEL_MAX if _break == 0 else 0, "Gas: ", ACCEL_MAX if gas == 0 else 0)


except KeyboardInterrupt:
    ser.close()
    del v
