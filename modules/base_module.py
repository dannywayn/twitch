"""
This module as base class which will be used for the whole project
"""
from random import randint
from time import time
import datetime


class BaseClass:
    """
    Base class for the modules
    Attributes:
        running (bool): Checks if the bot is running
    """
    running = False
    main = None
    logger_signal = None
    twitch_stream_time = [0, 0]
    spotify_stream_time = [0, 0]
    spotify_links = []
    proxies = []
    twitter_links = []
    twitch_profiles = []


    @staticmethod
    def sleep(min: float = 0, max: float = 0):
        """
        This function adds a time break in the bot functionalities
        :param min: the minimum time to sleep
        :param max: trhe maximum time to sleep
        """
        if min > max:
            min, max = max, min
        sleep_time = randint(int(min), int(max))
        start_time = time()
        while BaseClass.running and time() - start_time < sleep_time:
            continue

    @staticmethod
    def write_log(log):
        try:
            if not isinstance(log, str):
                return
            log = f'{"#" * 10} {datetime.datetime.now().time()} {"#" * 10}\n\n{log}\n\n'
            with open('logs.log', mode='a+', encoding='utf-8') as file:
                file.write(f'{log}\n')
        except:
            pass

