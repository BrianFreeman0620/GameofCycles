class GameofCycle:
    
    def __init__(self, size):
        self.matrix = []
        self.size = size
        for pointOne in range(self.size):
            self.matrix.append([])
            for pointTwo in range(self.size):
                self.matrix[pointOne].append(0)
                
    def showMatrix(self):
        for column in self.matrix:
            print(column)
            
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
                print("That move creates a source/sink")
                self.matrix[pointOne][pointTwo] = 1
                self.matrix[pointTwo][pointOne] = 1

test = GameofCycle(6)