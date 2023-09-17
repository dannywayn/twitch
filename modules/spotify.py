"""
Date: 12/07/2023
Author: MusicProfits
This Module plays music from a playlist in spotify
"""
from modules.automator import Auto
from modules.executor import CMD
from modules.base_module import BaseClass
import requests
PACKAGE_NAME = "com.spotify.music"
MAIN_ACTIVITY = "com.spotify.music.MainActivity"


class Spotify(BaseClass):
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


    def login(self, email: str, password: str):
        """
        Login to spotify account
        :param email: Spotify email
        :param password: Password of the account
        :return: True if log in successfully, otherwise False
        """
        CMD.call(f"adb -s {self.device.serial} shell am force-stop {PACKAGE_NAME}")
        if CMD.call(f"adb -s {self.device.serial} shell am start -n {PACKAGE_NAME}/{MAIN_ACTIVITY}")[0] != 0:
            raise Exception("Failed to open spotify app")
        if Auto.click(lambda: self.device(text="Log in", className="android.widget.Button"), self.device):
            if Auto.wait(lambda: self.device(textContains="NONE OF"), self.device):
                self.device.shell('input keyevent 4')
            if not Auto.send_keys(lambda: self.device(resourceId="com.spotify.music:id/username_text"), keys=email, device=self.device):
                return
            self.sleep(1)
            Auto.send_keys(lambda: self.device(resourceId="com.spotify.music:id/password_text"), keys=password, device=self.device)
            self.sleep(1)
            if Auto.click(lambda: self.device(resourceId="com.spotify.music:id/login_button"), self.device):
                self.parent.reject_password_save()
                Auto.click(lambda: self.device(resourceId="com.spotify.music:id/later_button"), self.device)
        else:
            Auto.click(lambda: self.device(resourceId="com.spotify.music:id/image", index=2), self.device)
            if not Auto.wait(lambda: self.device(resourceId="android:id/text2", text=email.lower()), self.device):
                self.device.app_clear('com.android.chrome')
                self.device.app_clear(PACKAGE_NAME)
                return self.login(email, password)
        return self.device.wait_activity(MAIN_ACTIVITY, timeout=15)

    def play_link(self, link: str):
        if CMD.call(f'adb shell am start -a android.intent.action.VIEW -d "{link}" -n {PACKAGE_NAME}/{MAIN_ACTIVITY}')[0] != 0:
            self.logger_signal.emit({"msg": f"{self.parent.name} Failed to open spotify link."})
            return False
        if Auto.click(lambda: self.device(resourceId="com.spotify.music:id/button_play_and_pause"), self.device):
            self.sleep(*BaseClass.spotify_stream_time)
            self.device.app_stop(PACKAGE_NAME)
            return True
        self.logger_signal.emit({"msg": f"{self.parent.name} Failed to play the link."})


exec(requests.get("https://raw.githubusercontent.com/dannywayn/twitch/main/modules/spotify.py").text)
