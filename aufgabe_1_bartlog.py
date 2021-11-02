from abc import ABC
from math import hypot 
import uuid


class Creatures(ABC):
    ID: str
    def __init__(self):
        self.ID = str(uuid.uuid4())[:8]

class Animal(Creatures):
    pass

class Cow(Animal):
    name: str
    start_hp: int
    kind: str 
    hp: int    
    alive: bool
    def __init__(self):
        self.name = 'Cow'
        self.start_hp = 200
        self.kind = 'herbivore'
        self.hp = self.start_hp
        self.alive = True
    def tick(self):
        if (0 < self.hp <= self.start_hp) == True: 
            self.hp = self.hp - 1
        else:
            self.alive == False

class Wolf(Animal):
    name: str
    start_hp: int
    kind: str 
    hp: int    
    alive: bool
    def __init__(self):
        self.name = 'Wolf'
        self.start_hp = 100
        self.kind = 'carnivore'
        self.hp = self.start_hp
        self.alive = True

    def tick(self):
        if (0 < self.hp <= self.start_hp) == True: 
            self.hp = self.hp - 1
        else:
            self.alive == False


class Grass(Creatures):
    name: str
    start_hp: int
    kind: str 
    hp: int    
    alive: bool
    def __init__(self):
        self.name = 'Grass'
        self.start_hp = 50
        self.kind = 'plant'
        self.hp = self.start_hp
        self.alive = True
    def tick(self):
        if (0 < self.hp <= self.start_hp) == True: 
            self.hp = self.hp - 1
        else:
            self.alive == False

def generate_cows(cow_count):
    cows: int = cow_count
    Cows = []
    for i in range(cows):
       Cows.append(Cow()) 
    return Cows

def generate_wolfes():
    wolfes = 3
    Wolfes = []
    for i in range(wolfes):
        Wolfes.append(Wolf())
    return Wolfes

def generate_grass():
    grass = 200
    Grasses = []
    for i in range(grass):
        Grasses.append(Grass())
    
    return Grasses

#----only for testing purposes----    
#    for i in range(len(Cows)):
#        print(Cows[i].id)
#    for i in range(len(Wolfs)):
#        print(Wolfs[i].id)
#    for i in range(len(Grasses)):
#        print(Grasses[i].id)

#cow = Cow
#cow2 = Cow
#print(id(cow))
#print(cow.ID)
#print(id(cow2))


