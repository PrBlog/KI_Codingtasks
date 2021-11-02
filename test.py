from dataclasses import dataclass
from dataclass_csv import DataclassWriter
import timeit

from Creatures import *
from Board import *

@dataclass
class Testrun():
    run_ID: int
    number_of_wolfes: int
    number_of_cows: int

def run() -> tuple:
    world = Board()
    creatures = []
    creatures.extend(generate_cows(50))
    creatures.extend(generate_wolfes(50))
    creatures.extend(generate_grass(200))
    world.populate(creatures)
    frame_counter: int = 100
    for i in range(frame_counter):
        for key in world.cells:
            if world.cells[key] != None:
                for creature in world.cells[key]:
                    creature.where_am_i(key)
                    if isinstance(creature, Animal):
                        creature.analyse(world)
                        creature.move_request(world)
                        creature.consume(world.cells[key])
    list_of_creatures = [creature for key in world.cells for creature in world.cells[key]]
    list_of_wolfes = [creature for creature in list_of_creatures if creature.name == 'Wolf' and creature.alive]
    list_of_Cows = [creature for creature in list_of_creatures if creature.name == 'Cow' and creature.alive]
    return (len(list_of_wolfes), len(list_of_Cows))


def main():
    list_of_runs: list = []
    number_of_runs: int = 100
    start = timeit.timeit()
    for _ in range(number_of_runs):
        (x,y) = run()
        list_of_runs.append(Testrun(_,x,y))
    end = timeit.timeit()
    print(end - start)
    with open("runs_with_random_move.csv", "w") as f:
        w = DataclassWriter(f, list_of_runs, Testrun)
        w.write()



main()

def optimization_test():
    
    start = timeit.timeit()
    (x,y) = run()
    end = timeit.timeit()
    print(end - start)
    print('Wolfes: {} | Cows: {}'.format(x,y))

#optimization_test()