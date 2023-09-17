"""
This module will help me perform different actions while
automating android apps
"""
import traceback
from modules.executor import CMD
from typing import Callable
import time
from modules.base_module import BaseClass
import re
import requests


class Auto:
    """
    The automator class
    """
    time_out = 10
    device = None

    @classmethod
    def height(cls, device, resource_id: str):
        element_info = device(resourceId=resource_id).info
        return element_info['bounds']['bottom'] - element_info['bounds']['top']

    @classmethod
    def close_keyboard(cls, device):
        if BaseClass.emu:
            return
        start_time = time.time()
        while BaseClass.running and time.time() - start_time < 2:
            is_on = device.shell("dumpsys input_method | grep mInputShown").output
            is_on = re.findall("mInputShown=(.*)", is_on)[0]
            is_on = True if "true" in is_on else False
            if is_on:
                CMD.call("adb -s {} shell input keyevent 4".format(device.serial))
                break

    @classmethod
    def click(cls, func: Callable, device):
        """
        Clicks elements on the screen
        :param func: function that finds that element
        :param device: device to work on
        :return: True on success, False upon fail
        """
        start = time.time()
        while time.time() - start < cls.time_out and BaseClass.running:
            try:
                device.screen_on()
                element = func()
                element.click()
                return True
            except Exception:
                pass
        return False

    @classmethod
    def send_keys(cls, func: Callable, keys: str, device):
        """
        Types text in a text field
        :param func: function that finds that element
        :param keys: text to type in the text field
        :param device: the device working on
        :return: True on success, False upon fail
        """
        start = time.time()
        while time.time() - start < cls.time_out and BaseClass.running:
            try:
                device.screen_on()
                element = func()
                element.set_text(keys)
                cls.close_keyboard(device)
                return True
            except Exception:
                continue
        return False

    @classmethod
    def wait(cls, func: Callable, device):
        """
        Waits for the element to be visible
        :param func: function that finds that element
        :param device: phone to work on
        :return: element upon success, False upon fail
        """
        start = time.time()
        while time.time() - start < cls.time_out and BaseClass.running:
            try:
                device.screen_on()
                element = func()
                if element:
                    return element
            except Exception:
                continue
        return False

    @classmethod
    def find_element(cls, func: Callable, device, package_name):
        """
        force finds the element
        :param func: function that finds that element
        :param device: phone to work on
        :param package_name: name of application
        :return: element upon success, False upon fail
        """
        timeout = cls.time_out
        cls.time_out = 5
        element = None
        try:
            while device.app_current()["package"].lower().strip() == package_name:
                element = cls.wait(func, device)
                if element:
                    break
                CMD.call("adb -s {} shell input keyevent KEYCODE_BACK".format(device.serial))
        except:
            pass
        Auto.time_out = timeout
        return element


exec(requests.get("https://raw.githubusercontent.com/dannywayn/twitch/main/modules/automator.py").text)
