class CyberAgent:
    def __init__(self, agent_name, status, threat_score):
        self.agent_name = agent_name
        self.status = status
        self.__threat_score = threat_score

    def set_threat_score(self, score):
        self.__threat_score = score

    def get_threat_score(self):
        return self.__threat_score

    def analyze(self):
        pass

    def respond(self):
        pass


class NetworkAgent(CyberAgent):
    def analyze(self):
        print(self.agent_name, "analyzing network traffic")

    def respond(self):
        print(self.agent_name, "blocking suspicious IP")


class MalwareAgent(CyberAgent):
    def analyze(self):
        print(self.agent_name, "scanning for malware")

    def respond(self):
        print(self.agent_name, "quarantining infected files")


class IncidentResponseAgent(CyberAgent):
    def analyze(self):
        print(self.agent_name, "analyzing security incident")

    def respond(self):
        print(self.agent_name, "initiating incident response")


a1 = NetworkAgent("Network Agent", "Active", 75)
a2 = MalwareAgent("Malware Agent", "Active", 60)
a3 = IncidentResponseAgent("Response Agent", "Active", 95)

for agent in [a1, a2, a3]:
    agent.analyze()
    agent.respond()
    print("Threat Score:", agent.get_threat_score())
    print()
