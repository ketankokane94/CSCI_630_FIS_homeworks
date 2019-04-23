import numpy

NUMBER_OF_ROWS = 10
NUMBER_OF_COLS = 10
world = numpy.zeros((NUMBER_OF_ROWS,NUMBER_OF_COLS))
#world[0,3] = 1
#world[1,3] = -1
world[9,9] = 1
world[NUMBER_OF_ROWS-1,NUMBER_OF_COLS-1]
exploring = []


def neighbors_of(row,col):
    if row == 9 and col == 9:
        return []
    result = []
    # for up action
    if row - 1 >= 0:
        result.append((row-1,col))
    # for down action
    if row + 1 < NUMBER_OF_ROWS:
        result.append((row+1,col))
    # for left action
    if col - 1 >= 0:
        result.append((row,col-1))
    # for down action
    if col + 1 < NUMBER_OF_COLS:
        result.append((row,col+1))
    return result


Reward = numpy.zeros((NUMBER_OF_ROWS,NUMBER_OF_COLS))

def value(row,col):
    if (row,col) in exploring:
        return world[row,col]
    if Reward[row,col] != 0:
        return Reward[row, col]
    exploring.append((row,col))
    neighbors = neighbors_of(row,col)
    result = []
    for neighbor in neighbors:
        result.append(value(neighbor[0],neighbor[1]))
    exploring.remove((row,col))
    if len(result) > 0:
        return world[row,col] + 0.9 * numpy.max(result)
    return world[row,col]


exploring = []
print(value(9,8))
exploring = []
print(value(0,1))



for row in range(len(world)):
    for col in range(len(world[row])):
        exploring = []
        Reward[row,col] = value(row,col)
print(Reward)
