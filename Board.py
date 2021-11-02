from random import randrange
from abc import ABC, abstractmethod

from Creatures import *


#class Cell:
    
class Map(ABC):
    x_range: int
    y_range: int
    cells: dict
    @abstractmethod
    def __init__(self):
        pass


class Environment(Map):
    x_range: int
    y_range: int
    cells: dict
    cellrange: int
    visibility: int 
    adversaries: list
    def __init__(self, environment: dict):
        self.cells = environment
        self.x_range = 2*self.visibility+1
        self.y_range = 2*self.visibility+1
        self.cellrange = self.x_range * self.y_range

    def find_x(self, cellkey) -> int:
        if cellkey in range(self.cellrange):
            x = cellkey%(self.x_range) - 3
            return x
        else: raise 'not within boundaries'
    
    def find_y(self, cellkey):
        if cellkey in range(self.cellrange):
            y = int(cellkey/self.x_range) - 3
            return y
        else: raise 'not within boundaries'
    
    

class Board(Map):
    x_range: int = 80
    y_range: int = 24
    cellrange: int = x_range*y_range
    cells: dict

    def __init__(self) -> None:
        self.cells = {list: [] for list in range(self.cellrange)}

    def populate(self, Creatures):
        for Creature in Creatures:
            self.cells[randrange(self.cellrange)].append(Creature)

    def board_tick(self):
        for i in range(len(self.cells)):
            if self.cells[i] != None:
                for creature in self.cells[i]:
                    creature.tick()
#                    if creature.alive == False:
#                        print('{} has died'.format(creature.name))

    def in_bounds(self, x,y) -> bool:
        if 1 <= x <= self.x_range and 1 <= y <= self.y_range:
            return True
        else: return False

    def find_cell(self, x_coord, y_coord):
        if self.in_bounds(x_coord, y_coord):
    	    return (y_coord-1) * (self.x_range) + x_coord - 1
        else: raise 'not within boundaries'

    def find_x(self, cellkey):
        if cellkey in range(self.cellrange):
            x = cellkey%(self.x_range) +1
            return x
        else: raise 'not within boundaries'

    def find_y(self, cellkey):
        if cellkey in range(self.cellrange):
            y = int(cellkey/self.x_range) + 1
            return y
        else: raise 'not within boundaries'
    

    
def compute_environment(location: int, world: Board) -> dict:
    current_x = world.find_x(location)
    current_y = world.find_y(location)
    environment: dict = {}
    cellcounter: int = 0
    visibility_range: int = 2
    for y in range(current_y - visibility_range, current_y + visibility_range+1):
        for x in range(current_x - visibility_range, current_x + visibility_range+1):
            if world.in_bounds(x,y): 
                cellkey = (world.find_cell(x,y))
                environment[(x - current_x, y - current_y)] = world.cells[cellkey]
            cellcounter += 1 #artefact, left for testing and debugging
    return environment
            