from random import randrange
from Creatures import *
from Board import *


def place_cows(cells, number_of_cows):
    for i in range(number_of_cows):
        cow = Cow()
        cells[randrange(len(cells))].append(cow)
    return cells
def place_wolfes(cells, number_of_wolfes):
    for i in range(number_of_wolfes):
        wolf = Wolf()
        cells[randrange(len(cells))].append(wolf)
    return cells
def place_grass(cells, number_of_grasses):
    for i in range(number_of_grasses):
        grass = Grass()
        cells[randrange(len(cells))].append(grass)
    return cells


def board_tick(board):
    for i in range(len(board)):
        if board[i] != None:
            for creature in board[i]:
                #print(creature.name)

                creature.tick()
                if creature.alive == False:
                    print('{} has died'.format(creature.name))



