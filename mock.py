
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
            f"Virtual Memory Usage:{self.state['memory_usage']}%\nSwap Memory Usage: {self.state['swap_usage']}%\nCPU Usage: {self.state['cpu_usage']}%\nDisk Usage:")
        print("\n")
        for partition, usage in self.state['disk_usage']:
            print(f"\n\n\n\n\n{partition}: {usage:.2f}%")
        print("[q] - Quit")
        while input(":") != 'q':
            print("Error input")