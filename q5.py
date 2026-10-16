class Agent:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def perform_task(self):
        pass


class SecurityAgent(Agent):
    def perform_task(self):
        print(self.name, "-> Detecting cyber threat")


class MonitoringAgent(Agent):
    def perform_task(self):
        print(self.name, "-> Monitoring system activity")


class RecoveryAgent(Agent):
    def perform_task(self):
        print(self.name, "-> Recovering system services")


agents = [
    SecurityAgent("Agent-1", "Running"),
    MonitoringAgent("Agent-2", "Running"),
    RecoveryAgent("Agent-3", "Running")
]

for a in agents:
    a.perform_task()
