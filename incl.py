
import os

import psutil
import json

import keyboard as k

st = ''


class SystemMonitor():
    global st
    default_state_ram = []

    def __init__(self):

        self.state = {"memory_usage": 0, "swap_usage": 0,
                      "cpu_usage": 0, "disk_usage": 0}  # Словарь для хранения состояния
        self.default_state_ram = self.get_disk_usage()

    def get_memory_usage(self):
        return psutil.virtual_memory()[2]

    def get_swap_usage(self):
        return psutil.swap_memory()[3]

    def get_cpu_usage(self):
        return psutil.cpu_percent()

    def get_disk_usage(self):
        disk_info = []
        for partition in psutil.disk_partitions():
            usage_percent = psutil.disk_usage(partition[1])[3]
            disk_info.append((partition[1], usage_percent))
        return disk_info

    def save_state(self, filename="system_state.json"):

        self.state["memory_usage"] = self.get_memory_usage()
        self.state["swap_usage"] = self.get_swap_usage()
        self.state["cpu_usage"] = self.get_cpu_usage()
        self.state["disk_usage"] = self.get_disk_usage()

        with open(filename, "w") as f:
            json.dump(self.state, f)
        print(f"State saved to {filename}")

    def load_state(self, filename="system_state.json"):
        try:
            with open(filename, "r") as f:
                self.state = json.load(f)
            print(f"State loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found. No state loaded.")

    def display_ret_info(self, filename):
        self.load_state(filename=filename)
        os.system("cls" if os.name == "nt" else "clear")
        print("\t\tSystem Information:")

        print(
            f"""Virtual Memory Usage:{self.state['memory_usage']}%\n
            Swap Memory Usage: {self.state['swap_usage']}%\n
            CPU Usage: {self.state['cpu_usage']}%
            Disk Usage:""", end='\r')
        print("\n")
        for partition, usage in self.state['disk_usage']:
            print(f"\n\n\n\n\n{partition}: {usage:.2f}%", end='\r')
        print("[q] - Quit", end='\r')
        while input(":") != 'q':
            print("Error input")


def set_terminal_size(columns, lines):
    try:
        os.system(f"mode con: cols={columns} lines={lines}" if os.name ==
                  "nt" else f"resize -s {lines} {columns}")
    except Exception as e:
        print(f"Ошибка при изменении размера терминала: {e}")


class Inp:
    inp = None
    a = 0

    def __init__(self, a):
        t = threading.Thread(target=self.get_input)
        t.daemon = True
        t.start()
        t.join(timeout=2)
        self.a = a

    def get_input(self):
        self.inp = input()
        for i in range(1, self.a):
            k.send("\n")

    def get(self):
        return self.inp


def get_key(key):
    # key_map = {0x01 : "UP", 0x02 : "DOWN", 0x03 : "LEFT", 0x04 : "RIGHT", 0x05 : "RET", 0x06 : "PAU", 0x07 : "QUI", 0x00 : "NOU"}
    ret = 0x00
    if (key == "A" or key == "w"):
        ret = 0x01
    elif (key == "B" or key == "s"):  # 115 = s; 113 = q
        ret = 0x02
    elif (key == "D" or key == "a"):
        ret = 0x03
    elif (key == "C" or key == "d"):
        ret = 0x04
    elif (key == "\n"):
        ret = 0x05
    elif (key == 'p'):
        ret = 0x06
    elif (key == "q"):
        ret = 0x07
    else:
        ret = 0x00
    return ret


if __name__ == "__main__":
    monitor = SystemMonitor()
    a = 0

    while 1:
        a += 1

        os.system("cls" if os.name == "nt" else "clear")
        monitor.display_info()

        k.on_press_key("q", exit(), suppress=True)
        k.on_press_key("s", monitor.save_state(filename=input("\nfilename:")))
        k.wait()
