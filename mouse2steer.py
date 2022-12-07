import evdev
import joystick

STEERING_MIN, STEERING_MAX = (-32767, 32767)
PHYSICAL_STEER_MIN, PHYSICAL_STEER_MAX = (-4095, 4095)

v = joystick.VirtualJoystick("Mouse to Steering Wheel Controller")

def get_device():
    for p in evdev.list_devices():
        dv = evdev.InputDevice(p)
        cap = dv.capabilities()
        if evdev.ecodes.EV_REL in cap:
            yield dv

def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

try:
    mouse = next(get_device())
except StopIteration:
    print("Mouse not found, make sure you have access to /dev/input/eventX")
    exit()

print("Found mouse: ", mouse.name)

try:
    x = 0
    for event in mouse.read_loop():
        if event.code == 0:
            x += event.value
            v.emit(map_range(x, PHYSICAL_STEER_MIN, PHYSICAL_STEER_MAX, STEERING_MIN, STEERING_MAX))

except KeyboardInterrupt:
    del v
