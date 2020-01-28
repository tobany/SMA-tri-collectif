import numpy as np

class Grid:

    def __init__(self, size, nbA, nbB):
        self.size = size
        self.nbA = nbA
        self.nbB = nbB
        self.object_grid = [[0 for i in range(size)] for k in range(size)]
        self.add_element("A", nbA)
        self.add_element("B", nbB)

    def add_element(self, type, nb):
        for i in range(nb):
            r = np.random.randint(self.size, size=2)
            while self.object_grid[r[0]][r[1]] != 0:
                r = np.random.randint(self.size, size=2)
            self.object_grid[r[0]][r[1]] = type

    def place_agent(self, agent, pos):
        self.object_grid[pos[0]][pos[1]] = agent

