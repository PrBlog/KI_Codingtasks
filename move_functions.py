import operator
from random import randrange


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



def get_neighbours(x_coord: int, y_coord: int, step_size: int = 1) -> dict:
    neighbours = {}
    for x_coord in range(-1, 2, 1):
        for y_coord in range(-1, 2, 1):
            neighbours[(x_coord,y_coord)] = working_fnc(x_coord,y_coord)
    return neighbours


def local_max(x_coord: int, y_coord: int, smellscape: list) -> tuple:
    neighbours = get_neighbours(x_coord,y_coord)
    (new_x, new_y) = max(neighbours.items(), key=operator.itemgetter(1))[0]
    if smellscape[new_x][new_y] > smellscape[x][y]:
        x = new_x
        y = new_y
    return ((x,y),neighbours[(x,y)]) 


def climb(fieldfunction, bounds: int = 500) -> tuple:
    odor: float = 0.0
    tests: int = 200
    local_maximas: dict
    for _ in range(tests):
        x: int = randrange(2*bounds) - bounds
        y: int = randrange(2*bounds) - bounds
        (maxima_key, odor) = local_max(x,y,fieldfunction)
        local_maximas[maxima_key] = odor
    return max(local_maximas.items(), key=operator.itemgetter(1))[0]

