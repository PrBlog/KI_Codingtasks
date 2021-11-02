from Board import *

def print_gui(cell, x_range, y_range):
    board_string: str = f''
    for row in range(y_range):    
        row_string: str = ''
        for column in range(x_range):
            cell_number: int = row*x_range + column
            creature_names = []
            for creature in cell[cell_number]:
                creature_names.append(creature.name)
            if 'Cow' in creature_names:
                row_string += '\x1b[0;30;47m' + 'C' + '\x1b[0m'
            elif 'Wolf' in creature_names:
                row_string += '\x1b[1;37;41m' + 'W' + '\x1b[0m'
            elif 'Grass' in creature_names:
                row_string += '\x1b[1;33;42m' + 'G' + '\x1b[0m'
            else: row_string += 'O'
        board_string += row_string
        board_string += '\n'

        #print(row_string)
    print(board_string)

                    