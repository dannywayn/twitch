from ppadb.client import Client as AdbClient
import time
from typing import Callable
from modules.executor import CMD
import sys

ADB_HOST = '127.0.0.1'
ADB_PORT = 5037


class ADB(AdbClient):
    """
    This class will help me connect to an android device
    """

    def __init__(self):
        super().__init__(ADB_HOST, ADB_PORT)
        res = CMD.call("adb start-server")
        if res[0] != 0:
            sys.exit(1)

    def list_devices_serial(self, state: list = None):
        """
        retrieves list of devices connected
        :return: list of devices.
        """
        return [x.serial for x in self.devices(state=state if state else [])]

    def connectivity(self, old: list, connected_callback: Callable, disconnected_callback: Callable):
        """
        Checks for connected and disconnected devices
        :param old: List of connected devices
        :param connected_callback: Callback function when a device is connected
        :param disconnected_callback: Callback function when a device is disconnected
        :return: Current connected devices.
        """
        current = self.devices()
        if old != current:
            if set(map(lambda x: x.serial, current)).difference(set(map(lambda x: x.serial, old))):
                connected_callback(list(set(current).difference(set(old))))
            if set(map(lambda x: x.serial, old)).difference(set(map(lambda x: x.serial, current))):
                disconnected_callback(list(set(old).difference(set(current))))
        time.sleep(2)
        return current

    @classmethod
    def list_packages(cls, serial):
        packages = map(lambda x: x.replace("\r", '').split(':')[1],
                       CMD.call(f"adb -s {serial} shell pm list packages")[1].split('\n'))
        return list(packages)
