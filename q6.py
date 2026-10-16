class Computer:
    def __init__(self, cpu, ram, battery):
        self.cpu = cpu
        self.ram = ram
        self.battery = battery

    def system_status(self):
        print("\nSystem Status")

        warning = False

        if self.cpu > 80:
            print("Heavy CPU Load")
            warning = True

        if self.ram > 85:
            print("High Memory Usage")
            warning = True

        if self.battery < 20:
            print("Low Battery")
            warning = True

        if not warning:
            print("System Operating Normally")


c1 = Computer(90, 70, 15)
c2 = Computer(45, 60, 90)

c1.system_status()
c2.system_status()
