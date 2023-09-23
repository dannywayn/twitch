"""
This module helps to perform different activities on twitch app
"""
import uiautomator2 as u2
import time
from modules.automator import Auto
from modules.executor import CMD
from modules.reader import EmailReader
from modules.base_module import BaseClass
import re
import requests
PACKAGE_NAME = "tv.twitch.android.app"
MAIN_ACTIVITY = "tv.twitch.android.feature.viewer.main.MainActivity"


class Twitch(BaseClass):
    """
    This is class that have everything I need for twitch automation
    """

    def __init__(self, device):
        self.parent = device
        self.device = device.device

    def login(self, username: str, password: str, email_config: dict, retries: int = 0):
        if retries <= 0:
            self.device.shell("input keyevent 3")
            CMD.call(f"adb -s {self.device.serial} shell am force-stop {PACKAGE_NAME}")
            self.device.shell("am start -n tv.twitch.android.app/.core.LandingActivity")
            self.device.app_wait(PACKAGE_NAME, 20)
            Auto.click(lambda: self.device(textContains="NONE OF"), self.device)
            Auto.click(lambda: self.device(text="Continue"), self.device)
            if self.device.wait_activity(MAIN_ACTIVITY, timeout=5):
                Auto.click(lambda: self.device(text="Cookies"), self.device)
                Auto.click(lambda: self.device(resourceId="tv.twitch.android.app:id/profile_pic_toolbar"), self.device)
                x = Auto.wait(lambda: self.device(resourceId="tv.twitch.android.app:id/menu_profile_username"), self.device)
                self.sleep(1.5)
                if x.get_text().lower().strip() != username.lower().strip():
                    res = CMD.call(f"adb -s {self.device.serial} shell pm clear {PACKAGE_NAME}")
                    if res[0] != 0:
                        BaseClass.logger_signal.emit({"msg": f"{self.parent.name} Failed to clear twitch cache"})
                        return
                    return self.login(username, password, email_config)
                CMD.call(f"adb -s {self.device.serial} shell input keyevent KEYCODE_BACK")
                return True
            Auto.click(lambda: self.device(resourceId="tv.twitch.android.app:id/login_button"), self.device)
            if not Auto.send_keys(lambda: self.device(resourceId="tv.twitch.android.app:id/login_username_field"), username, self.device):
                return
            Auto.send_keys(lambda: self.device(resourceId="tv.twitch.android.app:id/login_password_field"), password, self.device)
            self.sleep(1)
            Auto.click(lambda: self.device(resourceId="tv.twitch.android.app:id/login_button"), self.device)
            Auto.click(lambda: self.device(textContains="Skip"), self.device)  # skip email verification
        if not self.device.wait_activity(MAIN_ACTIVITY, timeout=5):
            code_input = Auto.wait(lambda: self.device(resourceId="tv.twitch.android.app:id/two_factor_input"), self.device)
            if not code_input:
                BaseClass.logger_signal.emit({"msg": f"{self.parent.name} Invalid twitch username/password"})
                return
            mail = EmailReader(email_config["host"], email_config["port"])
            mail.login(email_config["address"], email_config["password"])
            start_time = time.time()
            code = ""
            while time.time() - start_time < 60 and self.running:
                self.sleep(10)
                result = mail.get_email(
                    mail_atr={'subject': 'Code&Twitch', 'body': 'Twitch', 'from': 'twitch'},
                    which='ALL'
                )
                if result and re.findall("\D(\d{6}) - Your", result):
                    code = re.findall("\D(\d{6}) - Your", result)[0]
                    break
            if not code and retries > 0:
                BaseClass.logger_signal.emit({"msg": f"{self.parent.name} Failed to get verification code."})
                return
            elif retries <= 0:
                Auto.close_keyboard(self.device)
                Auto.click(lambda: self.device(resourceId="tv.twitch.android.app:id/request_new_authy"), self.device)
                return self.login(username, password, email_config, 1)
            Auto.click(lambda: self.device(text="Accept Cookies"), self.device)
            Auto.send_keys(lambda: self.device(resourceId="tv.twitch.android.app:id/two_factor_input"), code, self.device)
            Auto.click(lambda: self.device(resourceId="tv.twitch.android.app:id/submit_authentication"), self.device)
            self.parent.reject_password_save()
        Auto.time_out = 5
        Auto.click(lambda: self.device.xpath('//*[contains(@content-desc, "Dismiss")][1]'), self.device)
        Auto.click(lambda: self.device(textContains="Skip"), self.device)  # skip email verification
        Auto.time_out = 10
        return self.device.wait_activity(MAIN_ACTIVITY, timeout=5)

    def open(self, username: str):
        if CMD.call(f'adb -s {self.device.serial} shell am start -a android.intent.action.VIEW -d twitch://stream/{username}')[0] == 0:
            BaseClass.sleep(*BaseClass.twitch_stream_time)
            return True
        return False
