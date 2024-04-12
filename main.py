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

        str = ""
        for partition, usage in monitor.get_disk_usage():
            str += f"{partition}: {usage:.2f}%\n"
        str += "Disk changes:\n"
        i = 0
        for partition, usage in monitor.get_disk_usage():
            str += f"{partition}: {monitor.default_state_ram[i][1] - usage:.2f}%\n"
            i += 1
        print(
            f"""\r\t\tSystem Information:
Virtual Memory Usage: {monitor.get_memory_usage():.2f}%
Swap Memory Usage: {monitor.get_swap_usage():.2f}%
CPU Usage: {monitor.get_cpu_usage():.2f}%
Disk Usage:
{str}
Commands:\t [q]-Quit\t [s]-Save state\t [r]-Return state\n\r""", end="\r", flush=True)
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
        time.sleep(0.02)
        # os.system("cls" if os.name == "nt" else "clear")
