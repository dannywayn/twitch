"""
This module helps to set proxy in the device
"""
from modules.base_module import BaseClass
from modules.automator import Auto
import uiautomator2 as u2

PACKAGE_NAME = "io.oxylabs.proxymanager"


class OXY(BaseClass):
    """
    Oxy class that controls oxy proxy app
    """

    def __init__(self, device):
        """
        Constructor function that initializes device in the class's instance
        :param device: the device to work with
        """
        self.parent = device
        self.device = self.parent.device

    def reconnect(self, serial):
        self.sleep(10)
        self.parent.device = u2.Device(serial)

    def set_proxy(self, proxy: str):
        serial = self.device.serial
        self.device.app_clear(PACKAGE_NAME)
        self.reconnect(serial)
        if ':' not in proxy:
            return False
        ip, port, *credentials = proxy.split(':')
        self.device.shell('input keyevent 3')
        if not self.device.shell(f'monkey -p {PACKAGE_NAME} -c android.intent.category.LAUNCHER 1').output.startswith('Events injected: 1'):
            BaseClass.logger_signal.emit({"msg": f'failed to start app on device: {self.device.serial}'})
            return False

        Auto.click(lambda: self.device(index="0", text="Add new proxy"), self.device)
        Auto.click(lambda: self.device(index="2", className="android.widget.EditText"), self.device)
        Auto.send_keys(lambda: self.device(index="2", className="android.widget.EditText"), "My Proxy", self.device)
        Auto.send_keys(lambda: self.device(index="7", className="android.widget.EditText"), ip, self.device)
        Auto.send_keys(lambda: self.device(index="9", className="android.widget.EditText"), port, self.device)
        if len(credentials) == 2:
            Auto.send_keys(lambda: self.device(index="12", className="android.widget.EditText"), credentials[0], self.device)
            Auto.send_keys(lambda: self.device(index="14", className="android.widget.EditText"), credentials[1], self.device)
        Auto.click(lambda: self.device(text="Create"), self.device)
        Auto.click(lambda: self.device(text="My Proxy"), self.device)
        Auto.click(lambda: self.device(resourceId="android:id/button1"), self.device)
        return True if Auto.wait(lambda: self.device(textContains="Connected to "), self.device) else False
