from random import randrange
from abc import ABC, abstractmethod
import uuid
from Board import Board, Environment, compute_environment




"""movement functions for Animal Classes. reference strategy pattern"""

def random_move(current_location: int, world: Board) -> int:
    x_pos: int = world.find_x(current_location)
    y_pos: int = world.find_y(current_location)
    new_x_pos: int = (x_pos + randrange(3) - 1)
    new_y_pos: int = (y_pos + randrange(3) - 1)
    if world.in_bounds(new_x_pos, new_y_pos): new_location = world.find_cell(new_x_pos, new_y_pos)
    else: new_location = current_location
    return new_location

def cow_escape_move(current_location: int, world: Board) -> int:
    x_weight: float = 0.0
    y_weight: float = 0.0
    surroundings = compute_environment(current_location, world)
    positions_of_adversaries = [cell for cell in surroundings for creature in surroundings[cell] if creature.kind == 'carnivore' and creature.alive]
    for cell in positions_of_adversaries:
        (x,y) = cell
        if x != 0: x_weight += 1/x
        if y != 0: y_weight += 1/y
    if x_weight < 0: x_move: int = 1
    elif x_weight == 0: x_move: int = 0
    elif x_weight > 0: x_move: int = -1
    if y_weight < 0: y_move: int = 1
    elif y_weight == 0: y_move: int = 0
    elif y_weight > 0: y_move: int = -1
    new_x_pos = world.find_x(current_location) + x_move
    new_y_pos = world.find_y(current_location) + y_move
    if world.in_bounds(new_x_pos, new_y_pos): return world.find_cell(new_x_pos, new_y_pos)
    else: return current_location

#def cow_hungry_move(current_location: int, world: Board) -> int:

#def wolf_hunt_move(current_location: int, world: Board) -> int:


#def flight()
#def hunt()

class Creatures(ABC):
    ID: str
    location: int = None
    def __init__(self):
        self.ID = str(uuid.uuid4())[:8]
    def where_am_i(self, current_position):
        self.location = current_position
#    def with_you(self, cellcontent: list):
#        pass
    @abstractmethod
    def eaten(self) -> None:
        pass


class Animal(Creatures):   
    @abstractmethod
    def moving(self, world: Board, movefunction) -> None:
        pass
    @abstractmethod
    def move_request(self, world: Board) -> None:
        pass
    @abstractmethod
    def consume(self, cellcontent: list) -> None:
        pass
    @abstractmethod
    def analyse(self, world: Board) -> None:
        pass



class Cow(Animal):
    name: str
    start_hp: int
    kind: str 
    hp: int    
    alive: bool
    board_alias: str
    surroundings: dict
    adversaries: list
    def __init__(self):
        self.name = 'Cow'
        self.start_hp = 200
        self.kind = 'herbivore'
        self.hp = self.start_hp
        self.alive = True
        self.board_alias = "C"

    def tick(self):
        if (0 < self.hp) == True: 
            self.hp = self.hp - 1
        else:
            self.alive == False
            self.board_alias = "D"

    def moving(self, world: Board, movefunction) -> None:
        if self.alive == True:
            new_location = movefunction(self.location, world)
            if new_location != self.location:
                del world.cells[self.location][world.cells[self.location].index(self)]
                self.location = movefunction(self.location, world)
                world.cells[self.location].append(self)

    def move_request(self, world: Board) -> None:
        surroundings = compute_environment(self.location, world)
        adversaries = [creature for cell in surroundings for creature in surroundings[cell] if creature.kind == 'carnivore' and creature.alive]       
        if len(adversaries) > 0: 
            self.moving(world, random_move)
        else: 
            self.moving(world, random_move)

    def consume(self, cellcontent: list) -> None:
        if self.alive:
            plantlist = [creature for creature in cellcontent if creature.kind == 'plant']
            if plantlist != None:
                for plant in plantlist:
                    if plant.alive:
                        plant.eaten()
                        self.hp += 20
                        break
                if self.hp > 2*self.start_hp:
                    self.hp = 2*self.start_hp

    def eaten(self) -> None:
        if self.alive:
            self.alive = False
            self.hp = 0

    def analyse(self, world: Board) -> None:
        self.surroundings = compute_environment(self.location, world)
        self.adversaries = [cell for cell in self.surroundings for creature in self.surroundings[cell] if creature.kind == 'carnivore' and creature.alive]
        self.foodsources = [cell for cell in self.surroundings for creature in self.surroundings[cell] if creature.kind == 'plant' and creature.alive]

class Wolf(Animal):
    name: str
    start_hp: int
    kind: str 
    hp: int    
    alive: bool
    board_alias: str

    def __init__(self):
        self.name = 'Wolf'
        self.start_hp = 100
        self.kind = 'carnivore'
        self.hp = self.start_hp
        self.alive = True
        self.board_alias = "W"
    
    def tick(self) -> None:
        if (0 < self.hp) == True: 
            self.hp = self.hp - 1
        else:
            self.alive == False
            self.board_alias = "D"
    
    def moving(self, world: Board, movefunction) -> None:
        if self.alive == True:
            del world.cells[self.location][world.cells[self.location].index(self)]
            self.location = movefunction(self.location, world)
            world.cells[self.location].append(self)

    def move_request(self, world: Board) -> None:
        self.moving(world, random_move)

    def consume(self, cellcontent: list) -> None:
        if self.alive:
            herbivorelist = [creature for creature in cellcontent if creature.kind == 'herbivore']
            if herbivorelist != None: 
                for herbivore in herbivorelist:
                    if herbivore.alive:
                        herbivore.eaten()
                        self.hp += 50
                        break
                if self.hp > 2*self.start_hp:
                    self.hp = 2*self.start_hp
    
    def eaten(self) -> None:
        pass
    
    def analyse(self, world: Board) -> None:
        pass

class Grass(Creatures):
    name: str
    start_hp: int
    kind: str 
    hp: int    
    alive: bool
    board_alias: str
    def __init__(self):
        self.name = 'Grass'
        self.start_hp = 50
        self.kind = 'plant'
        self.hp = self.start_hp
        self.alive = True
        self.board_alias = "G"
    def tick(self):
        if (0 < self.hp <= self.start_hp) == True: 
            self.hp = self.hp - 1
        else:
            self.alive == False
            self.board_alias = "D"
    def eaten(self) -> None:
        if self.alive:
            self.hp -= 5
            if self.hp <= 0:
                self.alive == False

def generate_cows(cow_count):
    cows: int = cow_count
    Cows = []
    for i in range(cows):
       Cows.append(Cow()) 
    return Cows

def generate_wolfes(wolf_count):
    wolfes = wolf_count
    Wolfes = []
    for i in range(wolfes):
        Wolfes.append(Wolf())
    return Wolfes

def generate_grass(grass_count):
    grass = grass_count
    Grasses = []
    for i in range(grass):
        Grasses.append(Grass())    
    return Grasses




