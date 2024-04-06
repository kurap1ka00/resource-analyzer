import threading
import time

x = ""


def re():
    global x
    x = input()


def te():
    while 1:
        print('5')
        time.sleep(2)


thread1 = threading.Thread(target=te)
thread2 = threading.Thread(target=re)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
