import collections
import random


class Agent:
    def __init__(self, t, k_plus, k_moins, i, env):
        self.memory = collections.deque(maxlen=t)
        self.k_plus = k_plus
        self.k_moins = k_moins
        self.i = i
        self.env = env
        self.position = [0, 0]
        self.carry = 0


    def act(self):
        percept = self.env.get_perception(self.position)
        percept_val = list(percept.values())
        if self.carry != 0 and percept["H"] == 0:
            prop = percept_val.count(self.carry) / 4
            p = (prop / (self.k_moins + prop)) ** 2
            if random.uniform(0, 1) < p:
                self.env.let_object(self.position, self.carry)
        elif percept["H"] != 0:
            prop = percept_val.count(percept["H"]) / 4
            p = (self.k_plus / (self.k_plus + prop)) ** 2
            if random.uniform(0, 1) < p:
                self.carry = self.env.take_object(self.position)
        self.memory.append(percept["H"])
        self.move()

    def move(self):
        direction = random.randint(0, 3)
        pos = self.position
        if direction == 0:
            pos[0] += 1
        elif direction == 1:
            pos[0] -= 1
        elif direction == 2:
            pos[1] += 1
        else:
            pos[1] -= 1
        if self.env.move_agent(self.position, pos):
            self.position = pos

