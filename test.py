from sp110e.controller_sync import ControllerSync
import time

device = ControllerSync("ok")
device.connect()  # Optional
device.set_ic_model('WS2811')
device.switch_on()
time.sleep(3)
device.get_ic_models()
device.set_brightness(18)
device.set_color([255,255,255])

device.disconnect()  # Optional

print(device.print_parameters())
print(device.get_ic_model())