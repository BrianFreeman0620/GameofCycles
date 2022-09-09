# 2 is left
# 3 is right 

class GameofCycle:
    
    def __init__(self, size):
        self.matrix = []
        self.size = size
        for pointOne in range(self.size):
            self.matrix.append([])
            for pointTwo in range(self.size):
                self.matrix[pointOne].append(0)
                
    def showMatrix(self):
        for row in self.matrix:
            print(row)
            
    def addEdge(self, pointOne, pointTwo):
        self.matrix[pointOne][pointTwo] = 1
        self.matrix[pointTwo][pointOne] = 1
        
    def makeCycle(self):
        for point in range(self.size):
            self.addEdge(point, point - 1)
            
    def makePath(self):
        for point in range(self.size - 1):
            self.addEdge(point, point + 1)
            
    def addDirection(self, pointOne, pointTwo):
        if self.matrix[pointOne][pointTwo] == 1:
            if pointOne < pointTwo or (pointOne == self.size - 1 and pointTwo == 0):
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
        else:
            print("This is an illegal move.")
            
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
        
    def checkWin(self):
        used = 0
        
        for pointOne in range(1,self.size):
            if self.matrix[pointOne][pointOne-1] == 1:
                if self.checkUnmarkable(pointOne,pointOne-1) == True:
                    used += 1
            else:
                used += 1
        
        if used == (self.size-1):
            return True
        else:
            return False   

    #def playGame(self, player_number):

#testing with a 7 path 
#i also tested with a 3,4,5,and 6 paths to make sure 
#checkUnmarkable and checkWin worked

test = GameofCycle(7)
test.makePath()
test.addDirection(2,3)
test.addDirection(3,4)
test.addDirection(6,5)

test.showMatrix()
