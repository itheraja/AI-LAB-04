class ThreatDetector:
    def __init__(self, device_name, ip_address, threat_level):
        self.device_name = device_name
        self.ip_address = ip_address
        self.threat_level = threat_level

    def scan(self):
        print("\nDevice Name:", self.device_name)
        print("IP Address:", self.ip_address)

        if self.threat_level.lower() == "low":
            print("System Safe")
        elif self.threat_level.lower() == "medium":
            print("Suspicious Activity")
        elif self.threat_level.lower() == "high":
            print("Critical Threat Detected")
        else:
            print("Unknown Threat Level")


d1 = ThreatDetector("Office-PC", "192.168.1.10", "Low")
d2 = ThreatDetector("Server", "192.168.1.20", "High")

d1.scan()
d2.scan()
