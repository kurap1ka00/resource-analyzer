from incl import SystemMonitor
import os
import time
import keybrd
state = ''


def set_terminal_size(columns, lines):
    try:
        os.system(f"mode con: cols={columns} lines={lines}" if os.name ==
                  "nt" else f"resize -s {lines} {columns}")
    except Exception as e:
        print(f"Ошибка при изменении размера терминала: {e}")

if __name__ == "__main__":
    monitor = SystemMonitor()
    kb = keybrd.KBHit()
    print("Commands: [q]-Quit [s]-Save state [r]-Return state")
    print("     Memory Usage     Usage Swap       CPU Usage              Disk Usage                       Disk changes  ", end="\n")
    while 1:
        

        str = ""
        for partition, usage in monitor.get_disk_usage():
            str += f"{partition}: {usage:.2f}%\t"

        i = 0
        for partition, usage in monitor.get_disk_usage():
            str += f"{partition}: {monitor.default_state_ram[i][1] - usage:.2f}%\t"
            i += 1
        print("\t", monitor.get_memory_usage(), "%\t\t", monitor.get_swap_usage(), "%\t\t",
              monitor.get_cpu_usage(), "%\t\t", str, end="\r")
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
                print("Commands: [q]-Quit [s]-Save state [r]-Return state")
                print("     Memory Usage     Usage Swap       CPU Usage              Disk Usage                       Disk changes  ", end="\n")
            if (key == 114 or key == 170 or key == 82 or key == 138):
                monitor.display_ret_info(input("Filename:"))
                
                print("Commands: [q]-Quit [s]-Save state [r]-Return state")
                print("     Memory Usage     Usage Swap       CPU Usage              Disk Usage                       Disk changes  ", end="\n")
        time.sleep(0.2)
        # os.system("cls" if os.name == "nt" else "clear")
