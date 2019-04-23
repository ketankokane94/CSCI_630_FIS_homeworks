import numpy

world = numpy.zeros((3,4))
world[0,3] = 1
world[1,3] = -1
exploring = []


def neighbors_of(row,col):
    if row == 0 and col == 3:
        return []
    if row == 1 and col == 3:
        return []
    result = []
    # for up action
    if row - 1 >= 0:
        result.append((row-1,col))
    # for down action
    if row + 1 < 3:
        result.append((row+1,col))
    # for left action
    if col - 1 >= 0:
        result.append((row,col-1))
    # for down action
    if col + 1 < 4:
        result.append((row,col+1))
    return result


def value(row,col):
    if (row,col) in exploring:
        return world[row,col]
    exploring.append((row,col))
    neighbors = neighbors_of(row,col)
    result = []
    for neighbor in neighbors:
        result.append(value(neighbor[0],neighbor[1]))
    exploring.remove((row,col))
    if len(result) > 0:
        return world[row,col] + 0.9 * numpy.max(result)
    return world[row,col]

print(value(0,0))


Reward = numpy.zeros((3,4))
for row in range(len(world)):
    for col in range(len(world[row])):
        exploring = []
        Reward[row,col] = value(row,col)
print(Reward)
