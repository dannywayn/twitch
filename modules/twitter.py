"""
This module will be used to automate Twitter
"""
from modules.automator import Auto
from modules.executor import CMD
from modules.base_module import BaseClass
PACKAGE_NAME = "com.twitter.android"
START_ACTIVITY = "com.twitter.android.StartActivity"
MAIN_ACTIVITY = "com.twitter.app.main.MainActivity"


class Twitter(BaseClass):
    """
    Spotify class to automate spotify
    """

    def __init__(self, device):
        """
        Constructor function that initializes class instance attributes
        :param device: The device to work on
        """
        self.parent = device
        self.device = device.device

    def open(self, link: str):
        if CMD.call(f'adb -s {self.device.serial} shell am start -a android.intent.action.VIEW -d "{link}"')[0] == 0:
            Auto.time_out = 5
            self.open_in_chrome()
            if Auto.click(lambda: self.device(resourceId="com.android.chrome:id/terms_accept"), self.device):
                Auto.click(lambda: self.device(resourceId="com.android.chrome:id/negative_button"), self.device)
            Auto.time_out = 10
            Auto.click(lambda: self.device(textContains="twitch.tv", clickable="true", focusable="true"), self.device)
            if self.parent.app_wait("tv.twitch.android.app"):
                Auto.click(lambda: self.device(text="Accept Cookies"), self.device)
                BaseClass.sleep(*BaseClass.twitch_stream_time)
                return True
            return False

    def open_in_chrome(self):
        if Auto.click(lambda: self.device(textContains="Chrome"), self.device):
            BaseClass.sleep(1)
            Auto.click(lambda: self.device(resourceId="android:id/button_always"), self.device)
