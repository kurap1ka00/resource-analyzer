from incl import SystemMonitor
import os
import threading
import time
import keybrd
state = ''


def set_terminal_size(columns, lines):
    try:
        os.system(f"mode con: cols={columns} lines={lines}" if os.name ==
                  "nt" else f"resize -s {lines} {columns}")
    except Exception as e:
        print(f"Ошибка при изменении размера терминала: {e}")


def inp():
    global st

    st = input()


if __name__ == "__main__":
    monitor = SystemMonitor()
    kb = keybrd.KBHit()
    while 1:
        th = threading.Thread(target=monitor.display_info)
        th1 = threading.Thread(target=inp)
        monitor.display_info()

        press = False
        key = 0
        if (kb.kbhit()):
            key = ord(kb.getch())
            press = True
        if (press):
            if (key == 113 or key == 169 or key == 81 or key == 137):
                exit()
            if (key == 115 or key == 235 or key == 83 or key == 155):
                monitor.save_state(input("Filename:"))
            if (key == 114 or key == 170 or key == 82 or key == 138):
                monitor.display_ret_info(input("Filename:"))
        time.sleep(0.0002)
        os.system("cls" if os.name == "nt" else "clear")
