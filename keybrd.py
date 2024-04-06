import os

# Windows
if os.name == 'nt':
    import msvcrt

# Posix (Linux, OS X)
else:
    import sys
    import termios
    import atexit
    from select import select


class KBHit:

    def no_echo(self):
        # Save the terminal settings
        self.__fd = sys.stdin.fileno()
        self.__new_term = termios.tcgetattr(self.__fd)
        self.__old_term = termios.tcgetattr(self.__fd)

        # New terminal setting unbuffered
        self.__new_term[3] = (self.__new_term[3] & ~
                              termios.ICANON & ~termios.ECHO)
        termios.tcsetattr(self.__fd, termios.TCSAFLUSH, self.__new_term)

        # Support normal-terminal reset at exit
        atexit.register(self.set_normal_term)

    def __init__(self):
        self.__fd = None
        self.__new_term = None
        self.__old_term = None
        if os.name == 'nt':
            pass
        else:
            self.no_echo()

    def set_normal_term(self):
        # Resets to normal terminal.  On Windows this is a no-op.
        if os.name == 'nt':
            pass
        else:
            termios.tcsetattr(self.__fd, termios.TCSAFLUSH, self.__old_term)

    def getch(self):
        # Returns a keyboard character after kbhit() has been called.
        if os.name == 'nt':
            return msvcrt.getch()  # .decode('utf-8')
        else:
            c = sys.stdin.read(1)
            if (c == '\x1b'):
                return sys.stdin.read(2)[1]
            return c

    def kbhit(self):
        # Returns True if keyboard character was hit, False otherwise.
        if os.name == 'nt':
            return msvcrt.kbhit()

        else:
            dr, dw, de = select([sys.stdin], [], [], 0)
            return dr != []


# Test
if __name__ == "__main__":

    kb = KBHit()

    print('Hit any key, or ESC to exit')

    while True:

        if kb.kbhit():
            c = kb.getch()
            print(ord(c))

    kb.set_normal_term()
