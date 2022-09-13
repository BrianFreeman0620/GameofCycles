# 2 is left
# 3 is right 
# on a path

class GameofCycles:
    
    # Creates the Game of Cycles of given size
    def __init__(self, size):
        self.matrix = []
        self.size = size
        for pointOne in range(self.size):
            self.matrix.append([])
            for pointTwo in range(self.size):
                self.matrix[pointOne].append(0)
        self.cycle = False
        self.path = False
    
    # Shows the adjacency matrix            
    def showMatrix(self):
        for row in self.matrix:
            print(row)
    
    # Adds edge to adjacency matrix starting at pointOne and going to pointTwo        
    def addEdge(self, pointOne, pointTwo):
        self.matrix[pointOne][pointTwo] = 1
        self.matrix[pointTwo][pointOne] = 1
    
    # Makes the current game a cycle
    def makeCycle(self):
        for point in range(self.size):
            self.addEdge(point, point - 1)
        self.cycle = True
        self.path = False
    
    # Makes the current game a path
    def makePath(self):
        for point in range(self.size - 1):
            self.addEdge(point, point + 1)
        self.cycle = False
        self.path = True
    
    # Shows the matrix as a cycle with point labels
    def showCycle(self):
        if self.cycle:
            if self.size%2 == 0:
                if self.matrix[0][1] == 1:
                    print("0 o---o 1")
                elif self.matrix[0][1] == 2:
                    print("0 o-<-o 1")
                else:
                    print("0 o->-o 1")
                for row in range(1, int(self.size/2)):
                    print("  |   |")
                    if self.matrix[self.size - row][0 - row + 1] == 1:
                        leftRow = "|"
                    elif self.matrix[self.size - row][0 - row + 1] == 2:
                        leftRow = "v"
                    else:
                        leftRow = "^"
                    if self.matrix[row][row + 1] == 1:
                        rightRow = "|"
                    elif self.matrix[row][row + 1] == 2:
                        rightRow = "^"
                    else:
                        rightRow = "v"
                    print("  " + leftRow + "   " + rightRow)
                    print("  |   |")
                    if not row == int(self.size/2) - 1:
                        print(str(self.size - row), "o   o", str(row + 1))
                    else:
                        if self.matrix[self.size - row][row + 1] == 1:
                            print(str(self.size - row), "o---o", str(row + 1))
                        elif self.matrix[self.size - row][row + 1] == 2:
                            print(str(self.size - row), "o->-o", str(row + 1))
                        else:
                            print(str(self.size - row), "o-<-o", str(row + 1))
            else:
                print("     0")
                print("     o")
                print("    / \\")
                if self.matrix[0][self.size - 1] == 1:
                    leftRow = "/"
                elif self.matrix[0][self.size - 1] == 2:
                    leftRow = "v"
                else:
                    leftRow = "^"
                if self.matrix[0][1] == 1:
                    rightRow = "\\"
                elif self.matrix[0][1] == 2:
                    rightRow = "^"
                else:
                    rightRow = "v"
                print("  ", leftRow, " ", rightRow)
                print(str(self.size - 1), "o     o 1")
                for row in range(1, int((self.size-1)/2)):
                    print("  |     |")
                    if self.matrix[self.size - row - 1][0 - row] == 1:
                        leftRow = "|"
                    elif self.matrix[self.size - row - 1][0 - row] == 2:
                        leftRow = "v"
                    else:
                        leftRow = "^"
                    if self.matrix[row][row + 1] == 1:
                        rightRow = "|"
                    elif self.matrix[row][row + 1] == 2:
                        rightRow = "^"
                    else:
                        rightRow = "v"
                    print("  " + leftRow + "     " + rightRow)
                    print("  |     |")
                    if not row == int(self.size/2) - 1:
                        print(str(self.size - row - 1), "o     o", str(row + 1))
                    else:
                        if self.matrix[self.size - row - 1][row + 1] == 1:
                            print(str(self.size - row - 1), "o-----o", str(row + 1))
                        elif self.matrix[self.size - row - 1][row + 1] == 2:
                            print(str(self.size - row - 1), "o-->--o", str(row + 1))
                        else:
                            print(str(self.size - row - 1), "o--<--o", str(row + 1))
                
    
    # Shows the matrix as a path with point labels
    def showPath(self):
        if self.path:
            pathString = "o"
            numberString = "0"
            for edge in range(self.size - 1):
                numberString += "   " + str(edge + 1)
                pathString += "-"
                if self.matrix[edge][edge + 1] == 1:
                    pathString += "--o"
                elif self.matrix[edge][edge + 1] == 2:
                    pathString += "<-o"
                else:
                    pathString += ">-o"
            print(numberString)
            print(pathString)
    
    # Shows the matrix as a graph with point labels        
    def showGraph(self):
        if self.cycle:
            self.showCycle()
        elif self.path:
            self.showPath()
    
    # Tries to add a direction to the game and returns True if the move is legal
    def addDirection(self, pointOne, pointTwo):
        if self.matrix[pointOne][pointTwo] == 1:
            if (pointOne < pointTwo and not (pointTwo == self.size - 1 and pointOne == 0)) or (pointOne == self.size - 1 and pointTwo == 0):
                self.matrix[pointOne][pointTwo] = 3
                self.matrix[pointTwo][pointOne] = 3
            else:
                self.matrix[pointOne][pointTwo] = 2
                self.matrix[pointTwo][pointOne] = 2
            
            pointOneSum = 0
            pointTwoSum = 0
            for value in self.matrix[pointOne]:
                pointOneSum += value
            for value in self.matrix[pointTwo]:
                pointTwoSum += value
                
            if pointOneSum == 5 or pointTwoSum == 5:
                print("That move creates a source or a sink.")
                self.matrix[pointOne][pointTwo] = 1
                self.matrix[pointTwo][pointOne] = 1
                return False
            else:
                return True
        else:
            print("This is an illegal move.")
            return False
    
    # Checks if an edge can be marked and returns false if it can't        
    def checkUnmarkable (self, pointOne, pointTwo):
        if self.matrix[pointOne][pointTwo] == 2 or self.matrix[pointOne][pointTwo] == 3:
            #print("This edge is already marked.")
            return False
        
        if pointOne == 0 or pointTwo == 0:
            return False
        
        if pointOne == (self.size-1) or pointTwo == (self.size-1):
            return False
        if self.matrix[pointOne-1][pointTwo-1] == 1 or self.matrix[pointOne-1][pointTwo-1] == 1:
            return False
        if self.matrix[pointOne-1][pointTwo-1] != 1 and self.matrix[pointOne+1][pointTwo+1] != 1:
            if self.matrix[pointOne-1][pointTwo-1] != self.matrix[pointOne+1][pointTwo+1]:
                #print("This edge is unmarkable.")
                return True
            else:
                return False
    
    # Checks if there are any legal moves left and returns true if there aren't
    def checkWin(self):
        used = 0
        
        for pointOne in range(self.size):
            if self.matrix[pointOne][pointOne-1] == 1:
                if self.checkUnmarkable(pointOne,pointOne-1) == True:
                    used += 1
            else:
                used += 1
        
        if used == self.size:
            return True
        else:
            return False   
    
    # Plays the game with given number of players
    def playGame(self, player_number):
        winner = False
        while not winner:
            for playerTurn in range(1, player_number + 1):
                print("\nPlayer", str(playerTurn) + "'s turn\n")
                self.showGraph()
                source = int(input("\nChoose a point to start from "))
                destination = int(input("Choose a point to go to "))
                while not self.addDirection(source, destination):
                    self.showGraph()
                    source = int(input("\nChoose a point to start from "))
                    destination = int(input("Choose a point to go to "))
                if self.checkWin():
                    self.showGraph()
                    print("\nPlayer", playerTurn, "wins!")
                    winner = True
                    break
                    
#testing the code with a board with 7 vertices
test = GameofCycles(7)
test.makePath()
test.playGame(2)
