from sp110e.controller_sync import ControllerSync

device = ControllerSync('A8:8A:1E:1A:F1:CD', timeout=2, retries=1)
device.connect()  # Optional
device.print_parameters()
device.switch_on()
device.set_brightness(255)
device.switch_off()
device.disconnect()  # Optional