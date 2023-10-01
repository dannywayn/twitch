from modules.executor import CMD
from modules.base_module import BaseClass
import re
import os
from random import randint
import socket
import time


def check_if_port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0


def get_a_port() -> int:
    while True:
        port = randint(4000, 5050)
        if not check_if_port_in_use(port):
            break
    return port


class Emulator(BaseClass):
    """
    This class will help me launch vbox emulators
    """

    def __init__(self, name: str = "", **kwargs):
        """Constructor function that initialises my class object
        args:
            name: the name of the emulator
        """
        self.port = kwargs.get("port", get_a_port())
        self.name = self.init_device_name(name)

    @property
    def serial(self):
        return self.available_devices().get(self.name, "")

    @staticmethod
    def available_devices() -> dict:
        """Fetches all available emulators"""
        res = CMD.call("vboxmanage list vms")
        emulators = {}
        if res[0] == 0:
            data = res[1]
            for emu in data.splitlines():
                emulators[re.findall('"(.*?)"', emu)[0]] = re.findall('\{(.*?)}', emu)[0]
        else:
            BaseClass.write_log(res[2])
        return emulators

    def init_device_name(self, name: str):
        """Initializes the name attributes of the class object"""
        devices = self.available_devices()
        if name in devices:
            return name
        else:
            if not name:
                for num in range(1, 1_000_000):
                    name = f"Android #{num}"
                    if name not in devices:
                        break
            res = CMD.call("vboxmanage import '{}' --vsys 0 --vmname '{}'".format(
                os.path.join(os.getcwd(), 'resources\\Android.ova'), name))
            if res[0] != 0 or 'Successfully imported the appliance.' not in res[1]:
                raise Exception(res[2])
            res = CMD.call(f'VBoxManage modifyvm "{name}" --natpf1 ADB,tcp,127.0.0.1,{self.port},,5555')
            if res[0] != 0:
                raise Exception(res[2])
            return name

    def power(self, on=True):
        """Power vm"""
        if not on:
            command = f"vboxmanage controlvm {self.serial} poweroff"
        else:
            command = f"vboxmanage startvm {self.serial}"
        res = CMD.call(command)
        if res[0] != 0:
            raise Exception(res[2])
        if on:
            start_time = time.time()
            while time.time() - start_time < 80:
                if "connected" in CMD.call(f"adb connect 127.0.0.1:{self.port}")[1]:
                    break
                time.sleep(3)
        else:
            CMD.call(f"adb disconnect 127.0.0.1:{self.port}")

    def state(self):
        res = CMD.call(f'vboxmanage showvminfo {self.serial} --machinereadable | findstr VMState=')
        if res[0] == 0:
            return re.findall('"(.*?)"', res[1])[0]
        return "NAN"
