from datetime import timedelta
import time
from mqttHandler import *

from timeloop import Timeloop

from gateway_client import get_gateway_cilent, send_status_event, send_android_device_event
from udp_listener import listen_sensor_data

try:

    client = get_gateway_cilent('gateway_config.yml')
    client.connect()
except Exception as e:
    print("Error: ",e)
time.sleep(2)
tl = Timeloop()

devices_data = {}


@tl.job(interval=timedelta(seconds=5))
def send_gateway_status():
    send_status_event(client)


@tl.job(interval=timedelta(milliseconds=200))
def send_device_readings():
    for device_addr, data in devices_data.items():
        send_android_device_event(client, device_addr, "status", data)
        ##{'x_acc': -0.003208909183740616, 'y_acc': -0.006447315216064453, 'z_acc': 0.01796436309814453, 'x_gravity': 0.0, 'y_gravity': 0.0, 'z_gravity': 0.0, 'x_rotation': 0.0, 'y_rotation': 0.0, 'z_rotation': 0.0, 'x_orientation': 0.0, 'y_orientation': 0.0, 'z_orientation': 0.0, 'deprecated_1': 0.0, 'deprecated_2': 0.0, 'ambient_light': 56.0, 'proximity': 100.0, 'keyboard_button_pressed': 0.0}
        acc_data="X: "+data['x_acc']+",Y: "+data['y_acc']+",Z: "+data['z_acc']
        publishData('iot-2/type/ANDROID_DEVICE_TYPE/id/0/evt/status/fmt/acc',acc_data)
        publishData('iot-2/type/ANDROID_DEVICE_TYPE/id/0/evt/status/fmt/proximity',data['proximity'])
        
        
    devices_data.clear()


def gateway_command_callback(cmd):
    print("Command received for {}:{}: {}".format(cmd.typeId, cmd.deviceId, cmd.data))
    if cmd.typeId == 'reset':
        reset_data(devices_data)
    else:
        print("Unknown command type received")


def reset_data():
    devices_data.clear()
    # Add more custom logic here.
    pass


tl.start()

# Subscribing to commands
client.subscribeToCommands(commandId="reset")
# Registering a callback
client.commandCallback = gateway_command_callback


for data, device_addr in listen_sensor_data():
    devices_data[device_addr[0]] = data

