class SecuritySystem:
    def respond(self):
        print("Responding to security event")


class Firewall(SecuritySystem):
    def respond(self):
        print("Firewall -> Block suspicious network traffic")


class Antivirus(SecuritySystem):
    def respond(self):
        print("Antivirus -> Isolate malicious files")


class IntrusionDetectionSystem(SecuritySystem):
    def respond(self):
        print("Intrusion Detection System -> Generate security alert")


systems = [
    Firewall(),
    Antivirus(),
    IntrusionDetectionSystem()
]

for s in systems:
    s.respond()
