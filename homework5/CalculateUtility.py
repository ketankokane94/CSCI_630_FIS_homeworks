import numpy


class Something:
    __slots__ = 'NUMBER_OF_ROWS','NUMBER_OF_COLS','exploring','world','Reward'

    def __init__(self):
        self.NUMBER_OF_ROWS = 10
        self.NUMBER_OF_COLS = 10
        self.Reward = numpy.zeros((self.NUMBER_OF_ROWS, self.NUMBER_OF_COLS))
        self.Reward[9, 9] = 1
        self.exploring = []


    def neighbors_of(self,row,col):
        if row == 9 and col == 9:
            return []
        result = []
        # for right action
        if col + 1 < self.NUMBER_OF_COLS:
            result.append((row, col + 1))
        # for left action
        if col - 1 >= 0:
            result.append((row, col - 1))
        # for up action
        if row - 1 >= 0:
            result.append((row-1,col))
        # for down action
        if row + 1 < self.NUMBER_OF_ROWS:
            result.append((row+1,col))
        return result


    def value(self,row,col):
        if (row,col) in self.exploring:
            return self.Reward[row,col]
        if self.Reward[row,col] != 0:
            return self.Reward[row, col]
        self.exploring.append((row,col))
        #print(row, col)
        neighbors = self.neighbors_of(row,col)
        result = []
        for neighbor in neighbors:
            if neighbor  not in self.exploring:
                result.append(self.value(neighbor[0],neighbor[1]))
        self.exploring.remove((row,col))
        if len(result) > 0:
            self.Reward[row,col] = self.Reward[row,col]+ 0.9 * numpy.max(result)
            #return self.Reward[row,col] + 0.9 * numpy.max(result)
        return self.Reward[row,col]

if __name__ == '__main__':
    something = Something()
    #print(something.value(0, 0))
    for row in range(something.NUMBER_OF_ROWS):
        for col in range(something.NUMBER_OF_COLS):
            something.exploring = []
            something.Reward[row, col] = something.value(row, col)
    print(something.Reward)

