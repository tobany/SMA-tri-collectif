import numpy as np

from Agent import Agent


class Grid:

    def __init__(self, size, nbA, nbB):
        self.size = size
        self.nbA = nbA
        self.nbB = nbB
        self.object_grid = [[[0, 0] for i in range(size)] for k in range(size)]
        self.add_element("A", nbA)
        self.add_element("B", nbB)

    def add_element(self, type, nb):
        for i in range(nb):
            r = np.random.randint(self.size, size=2)
            while self.object_grid[r[0]][r[1]][0] != 0:
                r = np.random.randint(self.size, size=2)
            self.object_grid[r[0]][r[1]][0] = type

    def place_agent(self, agent):
        r = np.random.randint(self.size, size=2)
        while self.object_grid[r[0]][r[1]][1] != 0:
            r = np.random.randint(self.size, size=2)
        self.object_grid[r[0]][r[1]][1] = 'agent'

    def move_agent(self, last_pos, next_pos):
        if 0 <= next_pos[0] < self.size and 0 <= next_pos[1] < self.size and self.object_grid[next_pos[0]][next_pos[1]][1] == 0:
            self.object_grid[next_pos[0]][next_pos[1]][1] = self.object_grid[last_pos[0]][last_pos[1]][1]
            self.object_grid[last_pos[0]][last_pos[1]][1] = 0
            return True
        else:
            return False

    def get_perception(self, pos_agent):
        percept = dict()
        if pos_agent[0] < self.size - 1:
            percept["N"] = self.object_grid[pos_agent[0] + 1][pos_agent[1]][0]
        if pos_agent[0] > 0:
            percept["S"] = self.object_grid[pos_agent[0] - 1][pos_agent[1]][0]
        if pos_agent[1] > 0:
            percept["O"] = self.object_grid[pos_agent[0]][pos_agent[1] - 1][0]
        if pos_agent[1] < self.size - 1:
            percept["E"] = self.object_grid[pos_agent[0]][pos_agent[1] + 1][0]
        percept["H"] = self.object_grid[pos_agent[0]][pos_agent[1]][0]
        return percept

    def take_object(self, pos):
        obj = self.object_grid[pos[0]][pos[1]][0]
        self.object_grid[pos[0]][pos[1]][0] = 0
        return obj

    def let_object(self, pos, obj):
        if self.object_grid[pos[0]][pos[1]][0] == 0:
            self.object_grid[pos[0]][pos[1]][0] = obj
            return True
        else:
            return False


if __name__ ==  "__main__":
    g = Grid(50, 200, 200)
    agents = list()
    for i in range(20):
        a = Agent(10, 0.1, 0.3, 1, g)
        g.place_agent(a)
        agents.append(a)
    # print(g.object_grid)
    for k in range(500):
        for a in agents:
            a.act()
        # print(g.object_grid)

