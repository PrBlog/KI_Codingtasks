import time
import os

from Creatures import *
from Board import *
#from populate import *
from Gui import *

def main():

    world = Board()
    creatures = []
    creatures.extend(generate_cows(50))
    creatures.extend(generate_wolfes(50))
    creatures.extend(generate_grass(200))
    world.populate(creatures)
    frame_counter: int = 100
    for i in range(frame_counter):
        """locate Creatures"""
        world.compute_smell()
        for key in world.cells:
            if world.cells[key] != None:
                for creature in world.cells[key]:
                    creature.where_am_i(key)
                    if isinstance(creature, Animal):
                        creature.analyse(world)
                        creature.move_request(world)
                        creature.consume(world.cells[key])

        #os.system('cls' if os.name == 'nt' else 'clear')
        print('Frame: {}'.format(i))
        print_gui(world.cells, 80, 24)

        world.board_tick()


main()