class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def charge(self):
        self.battery = 100
        print(self.name, "is fully charged.")

    def move(self):
        pass


class DeliveryRobot(Robot):
    def move(self):
        if self.battery >= 20:
            print(self.name, "moves to a delivery location.")
        else:
            print(self.name, "cannot move. Low Battery.")


class SecurityRobot(Robot):
    def move(self):
        if self.battery >= 20:
            print(self.name, "patrols a specific area.")
        else:
            print(self.name, "cannot move. Low Battery.")


class RescueRobot(Robot):
    def move(self):
        if self.battery >= 20:
            print(self.name, "moves toward a disaster location.")
        else:
            print(self.name, "cannot move. Low Battery.")


r1 = DeliveryRobot("DeliveryBot", 70)
r2 = SecurityRobot("GuardBot", 15)
r3 = RescueRobot("RescueBot", 80)

r1.move()
r2.move()
r3.move()
