import collections
import random
import copy


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
        if self.carry != 0 and percept["H"] == 0:
            prop = self.memory.count(self.carry) / 10
            p = (prop / (self.k_moins + prop)) ** 2
            if random.uniform(0, 1) < p:
                self.env.let_object(self.position, self.carry)
        elif percept["H"] != 0:
            prop = self.memory.count(percept["H"]) / 10
            p = (self.k_plus / (self.k_plus + prop)) ** 2
            if random.uniform(0, 1) < p:
                self.carry = self.env.take_object(self.position)
        self.memory.append(percept["H"])
        self.move()

    def move(self):
        direction = list()
        if self.position[0] < self.env.size - 1:
            direction.append(0)
        if self.position[0] > 0:
            direction.append(1)
        if self.position[1] < self.env.size - 1:
            direction.append(2)
        if self.position[1] > 0:
            direction.append(3)
        direction = random.choice(direction)
        pos = copy.deepcopy(self.position)
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

