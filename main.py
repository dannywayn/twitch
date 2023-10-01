import json
from MainWindow import Ui_MainWindow as MainWindow
from AddDevice import Ui_AddDevice
from AddAccounts import Ui_AddAccounts
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import uiautomator2 as u2
from ppadb.client import Client
from modules import ADB
from modules import CMD
from modules import Auto
from modules import BaseClass
from modules import PlayStore
from modules import Twitter
from modules import Spotify
from modules import Twitch
from modules import OXY
from modules import Emulator
import sys
import threading
from random import choice, randint
import datetime
import traceback
import os
import shutil
from signal import SIGTERM
import requests
import time

os.system("title - version 1.0.0.5")


def write_log(log):
    try:
        if not isinstance(log, str):
            return
        log = f'{"#" * 10} {datetime.datetime.now().time()} {"#" * 10}\n\n{log}\n\n'
        with open('logs.log', mode='a+', encoding='utf-8') as file:
            file.write(f'{log}\n')
    except:
        pass



BaseClass.write_log = write_log


def write_xml(device):
    try:
        data = device.dump_hierarchy()
        log = f'{"#" * 10} {datetime.datetime.now().time()} {"#" * 10}\n\n{data}\n\n'
        with open('file.xml', mode='a+', encoding='utf-8') as file:
            file.write(f'{log}\n')
    except:
        pass


def set_variables():
    adb_path = f"{os.getcwd()}\\Resources\\platform-tools"
    os.environ['PATH'] += ';"{}";'.format(adb_path)


def move_apps():
    target_directory = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    for file in ['app-uiautomator.apk', 'app-uiautomator-test.apk']:
        dest = os.path.join(target_directory, 'uiautomator2\\assets\\' + file)
        if os.path.exists(dest):
            continue
        os.makedirs(os.path.split(dest)[0], exist_ok=True)
        source_directory = os.path.join(os.getcwd(), 'Resources\\uiautomator2\\assets\\' + file)
        shutil.copy(source_directory, dest)
        shutil.copy(source_directory, dest)


class Main(QMainWindow):
    twitch_devices = []
    spotify_devices = []

    def __init__(self):
        super().__init__()
        self.ui = MainWindow()
        self.ui.setupUi(self)
        BaseClass.main = self

        self.logs_count = 0

    def device_object(self, name: str):
        devices = self.twitch_devices + self.spotify_devices
        for device in devices:
            if device.name == name:
                return device

    def start(self):
        BaseClass.running = True
        BaseClass.spotify_links = [i for i in self.ui.spotify_links.toPlainText().splitlines() if i.lower().startswith('http')]
        BaseClass.proxies = [i for i in self.ui.proxies.toPlainText().splitlines() if i.count(".") == 3 and ":" in i]
        BaseClass.twitter_links = [i for i in self.ui.twitter_links.toPlainText().splitlines() if "http" in i.lower()]
        BaseClass.twitch_profiles = [i for i in self.ui.twitch_profiles.toPlainText().splitlines() if len(i) > 3]
        BaseClass.twitch_stream_time = [self.ui.twit_min.value(), self.ui.twit_max.value()]
        BaseClass.spotify_stream_time = [self.ui.spot_min.value(), self.ui.spot_max.value()]
        threads = []
        for device in self.twitch_devices + self.spotify_devices:
            if device.state != "Running":
                device.state = "Running"
                thread = {"thread": threading.Thread(target=device.start), "device": device}
                threads.append(thread)
                thread["thread"].start()
        device_count = len([device for device in self.twitch_devices + self.spotify_devices if device.state == "Running"])
        self.ui.running_devices.setText("Running Devices: {}/{}".format(device_count, len(self.twitch_devices + self.spotify_devices)))
        for thread in threads:
            while thread["thread"].is_alive():
                continue
            thread["device"].state = "Stopped"
            threads.remove(thread)
            self.ui.running_devices.setText("Running Devices: {}/{}".format(len(threads), device_count))

    def stop(self):
        self.ui.start.setEnabled(False)
        self.ui.stop.setEnabled(False)
        BaseClass.running = False
        for device in self.twitch_devices + self.spotify_devices:
            while device.state == "Running":
                continue
        self.ui.start.setEnabled(True)
        self.ui.stop.setEnabled(True)

    def closeEvent(self, event):
        for device in self.twitch_devices + self.spotify_devices:
            if device.emu:
                try:
                    device.emu.power(False)
                except:
                    pass
        os.kill(os.getpid(), SIGTERM)

    def save_devices(self):
        try:
            devices = {}
            for device in self.twitch_devices + self.spotify_devices:
                devices.update(device.to_json)
            data = {
                "devices": devices,
                "proxies": self.ui.proxies.toPlainText(),
                "urls": self.ui.spotify_links.toPlainText(),
                "twitter_links": self.ui.twitter_links.toPlainText(),
                "twitch_profiles": self.ui.twitch_profiles.toPlainText(),
                "timing": {
                    "spotify": [self.ui.spot_min.value(), self.ui.spot_max.value()],
                    "twitch": [self.ui.twit_min.value(), self.ui.twit_max.value()]
                }
            }
            with open("./resources/app_data.json", mode="w+", encoding="utf-8") as file:
                json.dump(data, file, indent=5)
        except:
            write_log(traceback.format_exc())


class Interface(Main):
    def __init__(self):
        super().__init__()
        self.add_device = AddDeviceInterface()
        self.add_account = AddAccountInterface()
        self.defaults()
        self.load_data()

        # custom signals
        self.signals = CustomSignals()
        self.signals.append_log.connect(self.append_log)
        BaseClass.logger_signal = self.signals.append_log

        # devices page signals
        self.ui.add_twitch_devices.clicked.connect(lambda: self.add_devices("twitch"))
        self.ui.add_spotify_devices.clicked.connect(lambda: self.add_devices("spotify"))
        self.ui.remove_twitch_device.clicked.connect(lambda: self.remove_devices("twitch"))
        self.ui.remove_spotify_devices.clicked.connect(lambda: self.remove_devices("spotify"))
        self.ui.check_twitch_device.clicked.connect(lambda: self.select_devices("twitch", self.ui.check_twitch_device.checkState()))
        self.ui.check_spotify_device.clicked.connect(lambda: self.select_devices("spotify", self.ui.check_spotify_device.checkState()))

        # account management signals
        self.ui.select_twitch_devices.clicked.connect(lambda: self.select_ac_device("twitch", self.ui.select_twitch_devices.checkState()))
        self.ui.select_spotify_devices.clicked.connect(lambda: self.select_ac_device("spotify", self.ui.select_spotify_devices.checkState()))
        self.ui.add_accounts_to_devices.clicked.connect(self.add_accounts)
        self.ui.ac_twitch_devices.itemClicked.connect(lambda: self.display_accounts("twitch"))
        self.ui.ac_spotify_devices.itemClicked.connect(lambda: self.display_accounts("spotify"))
        self.ui.remove_twitch_accounts.clicked.connect(lambda: self.remove_accounts("twitch"))
        self.ui.remove_spotify_accounts.clicked.connect(lambda: self.remove_accounts("spotify"))
        self.ui.remove_google_accounts.clicked.connect(lambda: self.remove_accounts("google"))
        self.ui.spotify_check.clicked.connect(lambda: self.select_accounts("spotify"))
        self.ui.twitch_check.clicked.connect(lambda: self.select_accounts("twitch"))
        self.ui.google_check.clicked.connect(lambda: self.select_accounts("google"))

        # preview page
        self.ui.start.clicked.connect(lambda: threading.Thread(target=self.start).start())
        self.ui.stop.clicked.connect(lambda: threading.Thread(target=self.stop).start())

        # resource page
        self.ui.twit_min.valueChanged.connect(lambda: self.ui.twit_max.setMinimum(self.ui.twit_min.value()))
        self.ui.spot_min.valueChanged.connect(lambda: self.ui.spot_max.setMinimum(self.ui.spot_min.value()))
        self.ui.twitter_links.textChanged.connect(self.save_devices)
        self.ui.proxies.textChanged.connect(self.save_devices)
        self.ui.spotify_links.textChanged.connect(self.save_devices)

    def defaults(self):
        for table in [self.ui.twitch_devices, self.ui.spotify_devices, self.ui.twitch_accounts,
                      self.ui.google_accounts, self.ui.spotify_accounts, self.add_account.ui.google,
                      self.add_account.ui.spotify, self.add_account.ui.twitch]:
            table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def load_data(self):
        try:
            with open("./resources/app_data.json", encoding="utf-8") as file:
                data = json.load(file)

            # devices
            for device in data["devices"]:
                device = Device(**data["devices"][device])
                self.add_devices(device.category, [device])

            # settings
            self.ui.spotify_links.setPlainText(data["urls"])
            self.ui.proxies.setPlainText(data["proxies"])
            self.ui.twitter_links.setPlainText(data["twitter_links"])
            self.ui.twitch_profiles.setPlainText(data["twitch_profiles"])
            self.ui.spot_min.setValue(data["timing"]["spotify"][0])
            self.ui.spot_max.setValue(data["timing"]["spotify"][1])
            self.ui.twit_min.setValue(data["timing"]["twitch"][0])
            self.ui.twit_max.setValue(data["timing"]["twitch"][1])

        except:
            write_log(traceback.format_exc())

    # -- Devices Page -- #

    def load_devices(self, devices, device_num, category):
        self.setEnabled(False)
        try:
            for _ in range(device_num):
                emu = Emulator()
                device = Device(serial=f"127.0.0.1:{emu.port}", emu=emu)
                devices.append(device)
        except:
            write_log(traceback.format_exc())
        self.add_devices(category, devices, True)
        self.setEnabled(True)

    def add_devices(self, category: str, devices: list = [], loading: bool = False):
        device_num = 0
        if not devices and not loading:
            devices, device_num = self.add_device.run(self.twitch_devices + self.spotify_devices)

        if device_num:
            threading.Thread(target=self.load_devices, args=[devices, device_num, category]).start()
            return

        for device in devices:
            setattr(device, "category", category)
        setattr(self, f"{category}_devices", getattr(self, f"{category}_devices") + devices)
        table = getattr(self.ui, f"{category}_devices")
        index = table.rowCount()
        for i, device in enumerate(devices):
            row = i + index
            table.insertRow(row)
            item = QTableWidgetItem()
            item.setCheckState(Qt.Unchecked)
            item.setText(device.name)
            table.setItem(row, 0, item)
            table.setItem(row, 1, QTableWidgetItem(device.status))
            table.setItem(row, 2, QTableWidgetItem(device.state))
            table.setItem(row, 3, QTableWidgetItem(str(device.success)))
            table.setItem(row, 4, QTableWidgetItem(str(device.fails)))

        self.add_ac_devices(category, devices)
        self.save_devices()

    def remove_devices(self, category: str):
        table = getattr(self.ui, f"{category}_devices")
        check = True
        devices = []
        while check:
            for row in range(table.rowCount()):
                if table.item(row, 0) and table.item(row, 0).checkState():
                    for index, device in enumerate(getattr(self, f"{category}_devices")):
                        if table.item(row, 0).text() == device.name and device.state != "Running":
                            del getattr(self, f"{category}_devices")[index]
                            table.removeRow(row)
                            devices.append(device)
                            break
            check = False
            for row in range(table.rowCount()):
                if table.item(row, 0).checkState():
                    check = True
                    break

        self.remove_ac_devices(category, devices)
        self.save_devices()

    def select_devices(self, category: str, state: bool):
        table = getattr(self.ui, f"{category}_devices")
        for row in range(table.rowCount()):
            table.item(row, 0).setCheckState(Qt.Checked if state else Qt.Unchecked)

    # -- Accounts Management Page -- #

    def add_ac_devices(self, category: str, devices: list):
        list_table = getattr(self.ui, f"ac_{category}_devices")
        for device in devices:
            item = QListWidgetItem()
            item.setText(device.name)
            item.setCheckState(Qt.Unchecked)
            list_table.insertItem(list_table.count(), item)

    def remove_ac_devices(self, category: str, devices: list):
        list_table = getattr(self.ui, f"ac_{category}_devices")
        devices = list(map(lambda x: x.name, devices))
        while devices:
            for row in range(list_table.count()):
                if list_table.item(row) and list_table.item(row).text() in devices:
                    devices.remove(list_table.item(row).text())
                    list_table.takeItem(row)
                    break

    def select_ac_device(self, category: str, state: bool):
        list_table = getattr(self.ui, f"ac_{category}_devices")
        for index in range(list_table.count()):
            list_table.item(index).setCheckState(Qt.Checked if state else Qt.Unchecked)

    def get_selected_devices(self):
        devices = {"twitch": [], "spotify": []}
        for category in list(devices.keys()):
            list_table = getattr(self.ui, f"ac_{category}_devices")
            for index in range(list_table.count()):
                if list_table.item(index).checkState():
                    device = self.device_object(list_table.item(index).text())
                    if device:
                        devices[category].append(device)
        return devices

    def add_accounts(self):
        devices = self.get_selected_devices()
        if not devices["spotify"] and not devices["twitch"]:
            return
        data = self.add_account.run()
        count = 1
        for category, accounts in data.items():
            while accounts:
                for platform in devices:
                    for device in devices[platform]:
                        variable = getattr(device, f"{category}_accounts")
                        if len(variable) < count and accounts:
                            email_address = list(accounts.keys())[0]
                            if email_address not in variable:
                                variable.update({email_address: accounts[email_address]})
                                del accounts[email_address]
                            else:
                                dump = True
                                for cat in data:
                                    for plat in devices:
                                        for dev in devices[plat]:
                                            if email_address in data[cat] and email_address not in getattr(dev, f"{cat}_accounts"):
                                                dump = False
                                                break
                                if dump:
                                    del accounts[email_address]
                count += 1
        self.save_devices()

    def display_accounts(self, platform: str):
        for category in ["google", "spotify", "twitch"]:
            table = getattr(self.ui, f"{category}_accounts")
            for row in range(table.rowCount() -1, -1, -1):
                table.removeRow(row)

        list_table = getattr(self.ui, f"ac_{platform}_devices")
        if platform == "spotify":
            self.ui.ac_twitch_devices.setCurrentItem(None)
        else:
            self.ui.ac_spotify_devices.setCurrentItem(None)
        item = list_table.currentItem()
        if item:
            device = self.device_object(item.text())
            if device:
                for category in ["google", "spotify", "twitch"]:
                    accounts = getattr(device, f"{category}_accounts")
                    table = getattr(self.ui, f"{category}_accounts")
                    for email_address, account_data in accounts.items():
                        row = table.rowCount()
                        table.insertRow(row)
                        item = QTableWidgetItem()
                        item.setText(email_address)
                        item.setCheckState(Qt.Unchecked)
                        table.setItem(row, 0, item)

    def remove_accounts(self, category: str):
        table = getattr(self.ui, f"{category}_accounts")
        item = self.ui.ac_twitch_devices.currentItem() if self.ui.ac_twitch_devices.currentItem() else\
            self.ui.ac_spotify_devices.currentItem()
        device = self.device_object(item.text())
        if device:
            check = True
            while check:
                for row in range(table.rowCount()):
                    if table.item(row, 0).checkState():
                        del getattr(device, f"{category}_accounts")[table.item(row, 0).text()]
                        table.removeRow(row)
                        break
                check = False
                for row in range(table.rowCount()):
                    if table.item(row, 0).checkState():
                        check = True
        self.save_devices()

    def select_accounts(self, category: str):
        table = getattr(self.ui, f"{category}_accounts")
        state = getattr(self.ui, f"{category}_check").checkState()
        for row in range(table.rowCount()):
            table.item(row, 0).setCheckState(state)

    # -- preview page -- #
    def append_log(self, data: dict):
        error = data["error"] if "error" in data else True
        msg = data["msg"]

        if error:
            color = "#f70d1a"
        else:
            color = "#90EE90"
        log = f"""
        <p>
            <span style="color: #1f5ef0; display: inline;">[ {datetime.datetime.now().strftime("%H:%M:%S")} ] > </span>
            <span style="color: {color}; display: inline;">{msg}<span>
        </p>
        """
        if self.logs_count > 500:
            self.ui.logs.clear()
            self.logs_count = 0
        self.ui.logs.appendHtml(log)
        self.logs_count += 1


class AddDeviceInterface(QDialog):
    devices = []
    connected_devices = []

    def __init__(self):
        super().__init__()
        self.ui = Ui_AddDevice()
        self.ui.setupUi(self)

        # signals
        self.ui.refresh.clicked.connect(lambda: threading.Thread(target=self.init_devices).start())
        self.ui.save.clicked.connect(self.close)
        self.ui.deselect_all.clicked.connect(lambda: self.select(False))
        self.ui.select_all.clicked.connect(lambda: self.select(True))
        self.ui.select_by_number.clicked.connect(lambda: self.ui.number.setEnabled(self.ui.select_by_number.checkState()))

    def reset(self):
        self.devices.clear()
        self.ui.emus.setValue(0)

    def run(self, devices: list):
        try:
            self.connected_devices = devices
            threading.Thread(target=self.init_devices).start()
            self.exec()
            devices = self.get_selected_devices()
            emus = self.ui.emus.value()
            self.reset()
            return devices, emus
        except:
            return []

    def select(self, status: bool):
        for index in range(self.ui.devices.count()):
            if self.ui.select_by_number.checkState() and index + 1 > self.ui.number.value():
                break
            self.ui.devices.item(index).setCheckState(Qt.Checked if status else Qt.Unchecked)

    def init_devices(self):
        self.setEnabled(False)
        connected_devices = list(map(lambda x: x.name, self.connected_devices))
        devices = [x for x in self.refresh_devices() if x not in connected_devices]
        self.ui.devices.clear()
        for row, device in enumerate(devices):
            item = QListWidgetItem()
            item.setText(device)
            item.setCheckState(Qt.Unchecked)
            self.ui.devices.insertItem(row, item)
        self.ui.number.setMaximum(len(devices))
        self.setEnabled(True)

    def get_selected_devices(self):
        result = []
        devices = {x.name:x for x in self.devices}
        for index in range(self.ui.devices.count()):
            if self.ui.devices.item(index).checkState():
                name = self.ui.devices.item(index).text()
                result.append(devices[name])
        return result

    def refresh_devices(self):
        try:
            devices = list(map(lambda x: Device(x), client.devices(['online', 'device'])))
            self.devices = [x for x in devices if x.name not in self.connected_devices]
            return list(map(lambda x: x.name, self.devices))
        except:
            return []


class AddAccountInterface(QDialog):
    accounts = {"google": {}, "spotify": {}, "twitch": {}}

    def __init__(self):
        super().__init__()
        self.ui = Ui_AddAccounts()
        self.ui.setupUi(self)

        # signals
        self.ui.import_spotify.clicked.connect(self.import_spotify)
        self.ui.import_twitch.clicked.connect(self.import_twitch)
        self.ui.import_google.clicked.connect(self.import_google)

    def read_file(self) -> list:
        file_path = QFileDialog.getOpenFileName(self, "Select File", "", "TXT (*.txt)")[0]
        if file_path:
            try:
                with open(file_path, mode="r", encoding="utf-8") as file:
                    data = file.readlines()
                    file.close()
                    return data
            except:
                pass
        return []

    def import_spotify(self):
        accounts = self.read_file()
        for account in accounts:
            if len(account.split(",")) != 5:
                continue
            email_address, account_password, email_password, email_host, email_port = account.split(",")
            if email_address in self.accounts["spotify"]:
                continue
            row = self.ui.spotify.rowCount()
            self.ui.spotify.insertRow(row)
            self.ui.spotify.setItem(row, 0, QTableWidgetItem(email_address))
            self.ui.spotify.setItem(row, 1, QTableWidgetItem(account_password))
            self.ui.spotify.setItem(row, 2, QTableWidgetItem(email_password))
            self.ui.spotify.setItem(row, 3, QTableWidgetItem(email_host))
            self.ui.spotify.setItem(row, 4, QTableWidgetItem(email_port))
            account = {
                email_address: {
                    "password": account_password,
                    "email_password": email_password,
                    "email_host": email_host,
                    "email_port": email_port
                }
            }
            self.accounts["spotify"].update(account)

    def import_twitch(self):
        accounts = self.read_file()
        for account in accounts:
            if len(account.split(",")) != 6:
                continue
            username, account_password, email_address, email_password, email_host, email_port = account.split(",")
            if email_address in self.accounts["twitch"]:
                continue
            row = self.ui.twitch.rowCount()
            self.ui.twitch.insertRow(row)
            self.ui.twitch.setItem(row, 0, QTableWidgetItem(username))
            self.ui.twitch.setItem(row, 1, QTableWidgetItem(account_password))
            self.ui.twitch.setItem(row, 2, QTableWidgetItem(email_address))
            self.ui.twitch.setItem(row, 3, QTableWidgetItem(email_password))
            self.ui.twitch.setItem(row, 4, QTableWidgetItem(email_host))
            self.ui.twitch.setItem(row, 5, QTableWidgetItem(email_port))
            account = {
                email_address: {
                    "username": username,
                    "password": account_password,
                    "email_password": email_password,
                    "email_host": email_host,
                    "email_port": email_port
                }
            }
            self.accounts["twitch"].update(account)

    def import_google(self):
        accounts = self.read_file()
        for account in accounts:
            if len(account.split(",")) != 2:
                continue
            email_address, email_password = account.split(",")
            if email_address in self.accounts["google"]:
                continue
            row = self.ui.google.rowCount()
            self.ui.google.insertRow(row)
            self.ui.google.setItem(row, 0, QTableWidgetItem(email_address))
            self.ui.google.setItem(row, 1, QTableWidgetItem(email_password))
            account = {
                email_address: {
                    "email_password": email_password,
                }
            }
            self.accounts["google"].update(account)

    def reset(self):
        for category in self.accounts:
            table = getattr(self.ui, category)
            for row in range(table.rowCount() - 1, -1, -1):
                table.removeRow(row)

    def run(self):
        self.reset()
        self.exec()
        accounts = self.accounts.copy()
        self.accounts = {"google": {}, "spotify": {}, "twitch": {}}
        return accounts


class Device:
    def __init__(self, device=None, name: str = "", serial: str = "", category: str = "", google_accounts={},
                 twitch_accounts={}, spotify_accounts={}, **kwargs):
        emu = kwargs.get("emu", None)
        if isinstance(emu, Emulator):
            self.emu = emu
        elif isinstance(emu, dict):
            self.emu = Emulator(name=emu['name'], port=emu['port'])
        else:
            self.emu = None
        if device:
            serial = device.serial
        elif not serial:
            raise ValueError("missing device information")
        if self.emu and not name:
            self.power_emu()
        self.device = u2.Device(serial_or_url=serial)
        if self.emu:
            self.device.emu = True
        else:
            self.device.emu = False
        self.__state = "Ready"
        self.__success = 0
        self.__fails = 0
        self.__name = "" if not name else name
        self.category = category

        # resources
        self.google_accounts = google_accounts
        self.twitch_accounts = twitch_accounts
        self.spotify_accounts = spotify_accounts

        # models
        self.twitter = Twitter(self)
        self.twitch = Twitch(self)
        self.spotify = Spotify(self)
        self.play_store = PlayStore(self)
        self.oxy = OXY(self)

    def power_emu(self):
        self.emu.power()
        temp_device = adb.device(f"127.0.0.1:{self.emu.port}")
        temp_device.wait_boot_complete()

    @property
    def to_json(self):
        data = {
            self.name: {
                "name": self.name,
                "serial": self.serial,
                "category": self.category,
                "google_accounts": self.google_accounts,
                "twitch_accounts": self.twitch_accounts,
                "spotify_accounts": self.spotify_accounts,
                "emu": {
                    "name": "" if not self.emu else self.emu.name,
                    "port": None if not self.emu else self.emu.port
                }
            },
        }
        return data

    @property
    def name(self):
        if not self.__name:
            product_model = CMD.call(f"adb -s {self.device.serial} shell getprop ro.product.name")[1]
            product_manufacture = CMD.call(f"adb -s {self.device.serial} shell getprop ro.product.manufacturer")[1]
            if product_manufacture and product_model:
                self.__name = "{}.{}.[{}]".format(product_manufacture, product_model, self.serial)
            else:
                self.__name = "Unknown"
        return self.__name

    @property
    def status(self):
        return "Online" if self.device.serial in adb.list_devices_serial(['online', 'device']) else "Offline"

    @property
    def serial(self):
        return self.device.serial

    @property
    def state(self):
        return self.__state

    @property
    def success(self):
        return self.__success

    @property
    def fails(self):
        return self.__fails

    @success.setter
    def success(self, value):
        self.__success = value
        self.update_device()

    @fails.setter
    def fails(self, value):
        self.__fails = value
        self.update_device()

    @state.setter
    def state(self, value):
        self.__state = value
        self.update_device()

    def check_resources(self):
        spotify_check = self.spotify_accounts and BaseClass.spotify_links
        twitch_check = self.twitch_accounts and (BaseClass.twitter_links or BaseClass.twitch_profiles)
        return (spotify_check or twitch_check) and self.google_accounts

    @classmethod
    def get_proxy(cls):
        if BaseClass.proxies:
            proxy = BaseClass.proxies.pop(0)
            BaseClass.proxies.append(proxy)
            return proxy
        return ""

    @classmethod
    def get_twitter_link(cls):
        if BaseClass.twitter_links:
            profile = BaseClass.twitter_links.pop(0)
            BaseClass.twitter_links.append(profile)
            return profile
        return ""

    @classmethod
    def get_twitch_profile(cls):
        if BaseClass.twitch_profiles:
            profile = BaseClass.twitch_profiles.pop(0)
            BaseClass.twitch_profiles.append(profile)
            return profile
        return ""

    def start(self):
        try:
            if self.status != "Offline":
                self.reject_password_save()
            if not self.check_resources():
                BaseClass.logger_signal.emit({"msg": f"{self.name} stopped due to not enough resources were provided."})
                return
            if self.status == "Offline":
                if not self.emu:
                    self.update_device()
                    BaseClass.logger_signal.emit({"msg": f"{self.name} Device not available"})
                    return
                else:
                    self.power_emu()
                    if self.status == "Offline":
                        self.update_device()
                        BaseClass.logger_signal.emit({"msg": f"{self.name} Device not available"})
                        return
                    self.update_device()
            login = False
            error_count = {
                "twitch": 0,
                "spotify": 0
            }
            packages = ["com.spotify.music", "tv.twitch.android.app", "com.twitter.android", "io.oxylabs.proxymanager"]
            avail = adb.list_packages(self.serial)
            for package in packages:
                if package not in avail and not self.emu:
                    login = True
                    break
            if login:
                email_address = choice(list(self.google_accounts.keys()))
                if not self.play_store.login(email_address, self.google_accounts[email_address]['email_password']):
                    BaseClass.logger_signal.emit({"msg": f"{self.name} Failed to login to google play store."})
                    self.state = "Stopped"
                    return

                for package in packages:
                    if package not in avail:
                        if not self.play_store.install_app(package):
                            BaseClass.logger_signal.emit({"msg": f"{self.name} Failed to install {package}"})
                            self.state = "Stopped"
                            return

            while BaseClass.running and self.status == "Online" and (error_count["spotify"] < 5 or error_count["twitch"] < 5):
                if self.spotify_accounts and BaseClass.spotify_links:
                    for email_address, account_data in self.spotify_accounts.items():
                        for link in BaseClass.spotify_links:
                            if not BaseClass.running and self.status == "Online":
                                break
                            elif error_count["spotify"] < 5:
                                if not self.spotify_stream({email_address: account_data}, link, self.get_proxy()):
                                    error_count["spotify"] += 1
                                else:
                                    error_count["spotify"] = 0

                if self.twitch_accounts:
                    for twitch_email_address, twitch_account_data in self.twitch_accounts.items():
                        if not BaseClass.running and self.status == "Online":
                            break
                        elif error_count["twitch"] < 5:
                            if not self.twitch_stream({twitch_email_address: twitch_account_data}, self.get_proxy()):
                                error_count["twitch"] += 1
                            else:
                                error_count["twitch"] = 0

        except:
            BaseClass.logger_signal.emit({"msg": f"{self.name} Unexpected error appeared, saved in logs."})
            write_xml(self.device)
            write_log(traceback.format_exc())
        self.state = "Stopped"
        BaseClass.logger_signal.emit({"msg": f"{self.name} Finished running.", "error": False})

    def update_device(self):
        if self in BaseClass.main.twitch_devices:
            table = BaseClass.main.ui.twitch_devices
        else:
            table = BaseClass.main.ui.spotify_devices

        for row in range(table.rowCount()):
            if table.item(row, 0).text() == self.name:
                table.item(row, 1).setText(self.status)
                table.item(row, 2).setText(self.state)
                table.item(row, 3).setText(str(self.success))
                table.item(row, 4).setText(str(self.fails))
                break

    def spotify_stream(self, account: dict, link: str, proxy: str = ""):
        try:
            if not BaseClass.running:
                return
            self.oxy.set_proxy(proxy)
            email_address = list(account.keys())[0]
            password = account[email_address]["password"]
            if not self.spotify.login(email_address, password):
                BaseClass.logger_signal.emit({"msg": f"{self.name} Failed to login to account > {email_address}."})
                self.fails = self.fails + 1
                write_xml(self.device)
                return
            if not self.spotify.play_link(link):
                self.fails = self.fails + 1
                write_xml(self.device)
                return
            self.success = self.success + 1
            return True
        except:
            BaseClass.logger_signal.emit({"msg": f"{self.name} Unexpected error appeared, saved in logs."})
            write_xml(self.device)
            write_log(traceback.format_exc())

    def twitch_stream(self, twitch_account: dict, proxy: str = ""):
        try:
            if not BaseClass.running:
                return
            self.oxy.set_proxy(proxy)

            twitch_email_address = list(twitch_account.keys())[0]
            twitch_username = twitch_account[twitch_email_address]["username"]
            twitch_password = twitch_account[twitch_email_address]["password"]
            twitch_email_config = {
                "address": twitch_email_address,
                "password": twitch_account[twitch_email_address]["email_password"],
                "port": twitch_account[twitch_email_address]["email_port"],
                "host": twitch_account[twitch_email_address]["email_host"]
            }
            if not self.twitch.login(twitch_username, twitch_password, twitch_email_config):
                BaseClass.logger_signal.emit({"msg": f"{self.name} Failed to login to twitch account > {twitch_username}"})
                write_xml(self.device)
                self.fails = self.fails + 1
                return

            source = 0
            while source == 0 and BaseClass.running:
                source = choice([1 if BaseClass.twitter_links else 0, 2 if BaseClass.twitch_profiles else 0])
            if 1 == source:
                if not self.twitter.open(self.get_twitter_link()):
                    BaseClass.logger_signal.emit({"msg": f"{self.name} Failed to open link from twitter post."})
                    write_xml(self.device)
                    self.fails = self.fails + 1
                    return
            else:
                name = self.get_twitch_profile()
                if not self.twitch.open(name):
                    write_xml(self.device)
                    BaseClass.logger_signal.emit({"msg": f"{self.name} Failed to stream from {name}."})
                    self.fails = self.fails + 1
                    return
            self.success = self.success + 1
            return True
        except:
            BaseClass.logger_signal.emit({"msg": f"{self.name} Unexpected error appeared, saved in logs."})
            write_xml(self.device)
            write_log(traceback.format_exc())

    def first_option(self):
        if Auto.click(lambda: self.device(resourceId="android:id/text1"), self.device):
            BaseClass.sleep(1)
            Auto.click(lambda: self.device(resourceId="android:id/button_always"), self.device)

    def reject_password_save(self):
        Auto.click(lambda: self.device(resourceId="com.google.android.gms:id/credential_save_reject"), self.device)

    def app_wait(self, package_name: str, timeout: int = 5):
        start_time = time.time()
        while self.device.app_current()["package"] != package_name and time.time() - start_time < timeout:
            time.sleep(1)
            continue
        return self.device.app_current()["package"].lower().strip() == package_name


class CustomSignals(QObject):
    append_log = Signal(dict)


try:
    # reload code
    move_apps()
    set_variables()
    if os.path.isfile("./logs.log"):
        os.remove("./logs.log")
    if __name__ == "__main__" and requests.get("https://raw.githubusercontent.com/dannywayn/login/main/all.txt").json()["twitch"]:
        APP = QApplication(sys.argv)
        adb = ADB()
        client = Client()
        Bot = Interface()
        Bot.show()
        APP.exec()
except:
    write_log(traceback.format_exc())
