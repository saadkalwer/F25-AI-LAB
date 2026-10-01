# AI Lab 2 - Saad Ahmed (009)

class ClassroomAgent:
    def __init__(self):
        self.previous_mode = None

    def decide_mode(self, temperature, occupied):
        if occupied == False:
            return "ECO"
        elif temperature > 26:
            return "COOL"
        elif temperature < 20:
            return "WARM"
        else:
            return "IDLE"

    def act(self, temperature, occupied):
        target_mode = self.decide_mode(temperature, occupied)
        previous = self.previous_mode

        if target_mode != self.previous_mode:
            command = "SEND"
        else:
            command = "NO COMMAND"

        self.previous_mode = target_mode
        return previous, target_mode, command

percepts = [
    (29, True),
    (29, True),
    (20, True),
    (26, True),
    (19, True),
    (29, False)
]

agent = ClassroomAgent()
print("Step | Previous | Percept | Target | Command")
for step in range(len(percepts)):
    temperature, occupied = percepts[step]
    previous, target, command = agent.act(temperature, occupied)
    print(step + 1, "|", previous, "|", percepts[step], "|", target, "|", command)

print("\nNoisy temperature test")
agent = ClassroomAgent()
for percept in [(25.9, True), (26.1, True), (25.9, True), (26.1, True)]:
    previous, target, command = agent.act(percept[0], percept[1])
    print(previous, percept, target, command)
