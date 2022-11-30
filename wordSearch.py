import random

directions = []
for i in range(-1, 2):
    for j in range(-1, 2):
        if i != 0 or j != 0:
            directions.append((i, j))

def createGrid(words):
    for i in range(10):
        grid = [['_']*9 for i in range(9)]
        worked = True
        for word in words:
            if not addWord(grid, word):
                print("Failed this attempt... trying again.")
                worked = False
                break
        if worked:
            return fillGrid(grid)
    return [['_']*9 for i in range(9)]


def addWord(grid, word):
    newDirections = directions[:]
    random.shuffle(newDirections)
    for dx, dy in newDirections:
        validStartPoints = []
        for i in range(9):
            for j in range(9):
                if i+len(word)*dx in range(9) and j+len(word)*dy in range(9):
                    validStartPoints.append((i, j))
        random.shuffle(validStartPoints)
        for startPoint in validStartPoints:
            p, q = startPoint[0], startPoint[1]
            if all([grid[p+dx*i][q+dy*i] == '_' or grid[p+dx*i][q+dy*i] == word[i] for i in range(len(word))]):
                for i in range(len(word)):
                    grid[p+dx*i][q+dy*i] = word[i]
                return True
    return False


def printGrid(grid):
    for row in grid:
        s = str(row[0])
        for i in range(1, len(row)):
            s += " " + str(row[i])
        print(s)


alphabet = [chr(i) for i in range (65, 91)]

def fillGrid(grid):
    for i in range (9):
        for j in range (9):
            if grid[i][j] == "_":
                grid[i][j] = random.choice(alphabet)

    return grid

def runGame(words):
    grid = createGrid(words)
    printGrid(grid)
    print()
    s = ""
    for word in words:
        s += word + " "
    print(s)

#can be used to find any word in the puzzle!! in the form (row, col) starting from 0
def findWord(word, grid):
    for i in range (9):
        for j in range (9):
            x, y = i, j
            wordIndex = 0
            letter = word[wordIndex]
            if letter == grid[x][y]:
                for dx, dy in directions:
                    x, y = i, j
                    wordIndex = 0
                    while wordIndex < len(word)-1:
                        x, y = x+dx, y+dy
                        wordIndex += 1
                        if not x in range(9) or not y in range(9):
                            break
                        if word[wordIndex] != grid[x][y]:
                            break
                        elif wordIndex == len(word)-1: 
                            return (i, j)

def getGridInput():
    print("Type in the grid as a list of 9-letter words: ")
    s = input()
    words = s.split()
    grid = [list(word) for word in words]
    return grid

#input your words here!
grid = createGrid(['THIS', 'IS', 'A', 'TEST', 'RUN'])
printGrid(grid)
print(findWord("TEST", grid))
