import pygame
from pygame.locals import *

from Agent import Agent
from Grid import Grid

NB_AGENT = 20
NB_A = 200
NB_B = 200
MEMORY_SIZE = 50
ERROR = 0.1

WIDTH = 9
HEIGHT = 9
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

g = Grid(50, NB_A, NB_B)
agents = list()
for i in range(NB_AGENT):
    a = Agent(MEMORY_SIZE, 0.1, 0.3, 1, g, ERROR)
    g.place_agent(a)
    agents.append(a)
print(g.object_grid)

pygame.init()

fenetre = pygame.display.set_mode((501, 501))
continuer = 1
WIDTH = 9
HEIGHT = 9
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the margin between each cell
MARGIN = 1

pas = 0

while continuer:
    pas += 1
    for event in pygame.event.get():   # On parcours la liste de tous les événements reçus
        if event.type == QUIT:     # Si un de ces événements est de type QUIT
            continuer = 0
    for a in agents:
        a.act_with_error()
    if pas % 10 == 0:
        for row in range(50):
            for column in range(50):
                color = WHITE
                if g.object_grid[row][column][0] == 'A':
                    color = GREEN
                elif g.object_grid[row][column][0] == 'B':
                    color = RED
                pygame.draw.rect(fenetre,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
        pygame.display.flip()
    if pas % 1000 == 0:
        print("Etape {}".format(pas))
