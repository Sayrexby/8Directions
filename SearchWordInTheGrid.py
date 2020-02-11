import random

    # This function search the word in all 8-direction  
def SearchWordInMatrix(grid, row, col, word, xRow, xCol, directions): 
          
    # If first character of the word not equal of the first character given starting point in grid
    if grid[row][col] != word[0]: 
        return False
            
    # Search word in all 8 directions  
    for x, y in directions: 
            
        # Initialize starting point for current direction 
        rowDir, colDir = row + x, col + y 
        flag = True
            
        # First character is already checked start from second one
        for k in range(1, len(word)): 
            if (0 <= rowDir <xRow and 
                0 <= colDir <xCol and 
                word[k] == grid[rowDir][colDir]): 
                    
                # Moving in particular direction 
                rowDir += x 
                colDir += y 
            else: 
                flag = False
                break
        if flag: 
            return True
    return False

    
    # Create emptry grid
def CreateGrid(row, col):
    newMatrix = []
    for itemR in range(0,row):
        newMatrix.append([])
        for itemC in range(0,col):
            newMatrix[itemR].append("+")
    return newMatrix

    # Fill already created grid random characters
def FillRandomChars(row, col):
    emptyMatrix = CreateGrid(row, col)
    alphabet="abcdefghijklmnopqrstuvwxyz"

    for itemR in range(0,row):
        for itemC in range(0,col):
            if emptyMatrix[itemR][itemC]=="+":
                randomChar = random.choice(alphabet)
                emptyMatrix[itemR][itemC]=randomChar
    return emptyMatrix



# Search given word in given grid 
def StartSearch(): 
    
    # Initialize size of grid
    x=15
    y=15

    # Initialize directions of grid
    directions = [[-1, 0], [1, 0], [1, 1], [1, -1], [-1, -1], [0, 1], [0, -1]]
    
    # Fill grid random characters
    grid = FillRandomChars(x,y)
    
    # Display on screen the grid
    print(" ")
    print(" ")
    for row in range(0,x):
        line=" "
        for col in range(0,y):
            line = line + grid[row][col] + " "
        line = line + " "
        print(line)
    print(" ")

    ####################################################################
    ### ----------- Start searching the word in the grid ----------- ###
    ####################################################################

    # Rows and columns in given grid
    xRow = len(grid) 
    xCol = len(grid[0]) 
    
    # Open file with words
    fh = open('../8Directions/words.txt')
    words = fh.read().split('\n')
    fh.close()

    # Find every word from the list of words
    for word in words:
        if word == '': break
        else: 
            for row in range(xRow): 
                for col in range(xCol):
                    if SearchWordInMatrix(grid, row, col, word, xRow, xCol, directions): 
                        print("[ "+ word + " ] found. Points: " + str(row) + ', ' + str(col))



StartSearch()