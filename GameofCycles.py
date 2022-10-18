#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 09:55:18 2022

@authors: bushra and brian
"""

from itertools import combinations
import copy

# 2 is out
# 3 is in 
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
        self.edges = 0
    
    # Shows the adjacency matrix            
    def showMatrix(self):
        for row in self.matrix:
            print(row)
    
    # Checks if the graph is planar and states reason if it isn't
    def isPlanar(self):
        if self.size <= 4:
            return True
        else:
            # Checks if the matrix can be reduced to K 3,3
            if self.size > 5:
                for vertex1 in range(self.size):
                    for vertex2 in range(self.size):
                        if not vertex1 == vertex2:
                            for vertex3 in range(self.size):
                                if not (vertex1 == vertex3 or vertex2 == vertex3):
                                    for vertex4 in range(self.size):
                                        if not (vertex1 == vertex4 or vertex2 == vertex4 or vertex3 == vertex4):
                                            for vertex5 in range(self.size):
                                                if not (vertex1 == vertex5 or vertex2 == vertex5 or vertex3 == vertex5 or vertex4 == vertex5):
                                                    for vertex6 in range(self.size):
                                                        if not (vertex1 == vertex6 or vertex2 == vertex6 or vertex3 == vertex6 or vertex4 == vertex6 or vertex5 == vertex6):
                                                            if not self.matrix[vertex1][vertex2] == 0 and not self.matrix[vertex1][vertex3] == 0 and not self.matrix[vertex1][vertex4] == 0:
                                                                if not self.matrix[vertex5][vertex2] == 0 and not self.matrix[vertex5][vertex3] == 0 and not self.matrix[vertex5][vertex4] == 0:
                                                                   if not self.matrix[vertex6][vertex2] == 0 and not self.matrix[vertex6][vertex3] == 0 and not self.matrix[vertex6][vertex4] == 0:
                                                                       print("K 3,3")
                                                                       return False
            # Checks if the matrix can be reduced to K 5
            for vertex1 in range(self.size):
                for vertex2 in range(self.size):
                    if not vertex1 == vertex2:
                        for vertex3 in range(self.size):
                            if not (vertex1 == vertex3 or vertex2 == vertex3):
                                for vertex4 in range(self.size):
                                    if not (vertex1 == vertex4 or vertex2 == vertex4 or vertex3 == vertex4):
                                        for vertex5 in range(self.size):
                                            if not (vertex1 == vertex5 or vertex2 == vertex5 or vertex3 == vertex5 or vertex4 == vertex5):
                                                if not self.matrix[vertex1][vertex2] == 0 and not self.matrix[vertex1][vertex3] == 0 and not self.matrix[vertex1][vertex4] == 0 and not self.matrix[vertex1][vertex5] == 0:
                                                    if not self.matrix[vertex2][vertex3] == 0 and not self.matrix[vertex2][vertex4] == 0 and not self.matrix[vertex2][vertex5] == 0:
                                                        if not self.matrix[vertex3][vertex4] == 0 and not self.matrix[vertex3][vertex5] == 0:
                                                            if not self.matrix[vertex4][vertex5] == 0:
                                                                print("K 5")
                                                                return False
                                                            
            return True
    
    # Adds edge to adjacency matrix starting at pointOne and going to pointTwo        
    def addEdge(self, pointOne, pointTwo):
        if not pointOne == pointTwo and self.matrix[pointOne][pointTwo] == 0:
            self.matrix[pointOne][pointTwo] = 1
            self.matrix[pointTwo][pointOne] = 1
            self.edges += 1
            #remove when planar is back in town
            '''if self.isPlanar():
                self.edges += 1
            else:
                self.matrix[pointOne][pointTwo] = 0
                self.matrix[pointTwo][pointOne] = 0
                print("That edge would make the graph nonplanar")'''
        elif not self.matrix[pointOne][pointTwo] == 0:
            print("That edge is already in the matrix")
        else:
            print("A vertix cannot point to itself")
    
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
    
   
    # Tries to add a direction to the game and returns True if the move is legal
    def addDirection(self, pointOne, pointTwo, printError = True):
        if self.matrix[pointOne][pointTwo] == 1:
            self.matrix[pointOne][pointTwo] = 2
            self.matrix[pointTwo][pointOne] = 3
            
            sourceORsinkOne = True
            sourceORsinkTwo = True
            edgeStatus = 1
            leafOne = 0
            leafTwo = 0
            
            for i in range(self.size):
                if not self.matrix[i][pointOne] == 0:
                    leafOne += 1
                
                if self.matrix[i][pointOne] == 1:
                    sourceORsinkOne = False
                    break
                
                if self.matrix[i][pointOne] == 2:
                    if edgeStatus == 1:
                        edgeStatus = 2
                    if edgeStatus == 3:
                        sourceORsinkOne = False
                        break
                    
                if self.matrix[i][pointOne] == 3:
                    if edgeStatus == 1:
                        edgeStatus = 3
                    if edgeStatus == 2:
                        sourceORsinkOne = False
                        break
            
            if leafOne == 1:
                sourceORsinkOne = False
            edgeStatus = 1
            
            for i in range(self.size):
                if not self.matrix[i][pointTwo] == 0:
                    leafTwo += 1
                    
                if self.matrix[i][pointTwo] == 1:
                    sourceORsinkTwo = False
                    break
                
                if self.matrix[i][pointTwo] == 2:
                    if edgeStatus == 1:
                        edgeStatus = 2
                    if edgeStatus == 3:
                        sourceORsinkTwo = False
                        break
                    
                if self.matrix[i][pointTwo] == 3:
                    if edgeStatus == 1:
                        edgeStatus = 3
                    if edgeStatus == 2:
                        sourceORsinkTwo = False
                        break
            if leafTwo == 1:
                sourceORsinkTwo = False
                
            if sourceORsinkOne or sourceORsinkTwo:
                if printError:
                    print("That move creates a source or a sink.")
                self.matrix[pointOne][pointTwo] = 1
                self.matrix[pointTwo][pointOne] = 1
                return False
            else:
                return True
        else:
            if printError:
                print("This is an illegal move.")
            return False
        
    def checkUnmarkable(self, pointOne, pointTwo):
        pointOneDirection = 1
        rowOne = 1
        columnOne = 1
        leafValueRow = 0
        leafValueColumn = 0
        
        if pointOne == pointTwo:
            print("This is an illegal move.")
        
        for i in range(self.size):
            if not self.matrix[i][pointOne] == 0:
                leafValueRow += 1
            
            if self.matrix[i][pointOne] == 1 and rowOne == 1:
                rowOne = 0
            elif self.matrix[i][pointOne] == 1 and rowOne == 0:
                return False
            elif pointOneDirection == 1 and not self.matrix[i][pointOne] == 0:
                pointOneDirection = self.matrix[i][pointOne]
            elif not pointOneDirection == self.matrix[i][pointOne] and not self.matrix[i][pointOne] == 0:
                return False
        
        if leafValueRow == 1:
            return False
        
        for j in range(self.size):
            if not self.matrix[pointTwo][j] == 0:
                leafValueColumn += 1
            
            if self.matrix[pointTwo][j] == 1 and columnOne == 1:
                columnOne = 0
            elif self.matrix[pointTwo][j] == 1 and columnOne == 0:
                return False
            elif self.matrix[pointTwo][j] == pointOneDirection:
                return False
        
            
        if leafValueColumn == 1:
            return False
        else:
            return True
    
    def checkWin(self):
        used = 0
        
        for i in range(self.size):
            for j in range(self.size):
                if i > j:
                    if self.matrix[i][j] == 0:
                        pass
                    elif self.matrix[i][j] == 1:
                        if self.checkUnmarkable(i,j):
                            used += 1
                    else:
                        used += 1
        
        if used == self.edges:
            return True
        else:
            return False 
        
        # Plays the game with given number of players
    def playGame(self, player_number):
        winner = False
        while not winner:
            for playerTurn in range(1, player_number + 1):
                print("\nPlayer", str(playerTurn) + "'s turn\n")
                self.showMatrix()
                source = int(input("\nChoose a point to start from "))
                destination = int(input("Choose a point to go to "))
                while not self.addDirection(source, destination):
                    self.showMatrix()
                    source = int(input("\nChoose a point to start from "))
                    destination = int(input("Choose a point to go to "))
                if self.checkWin():
                    self.showMatrix()
                    print("\nPlayer", playerTurn, "wins!")
                    winner = True
                    break
                
    def simulateGame(self, player_number):
        possibleMoves = []
        for row in range(self.size):
            for column in range(self.size):
                if self.matrix[row][column] == 1 and row < column:
                    possibleMoves.append([row, column])
        
        positionList = []
        for number in range(len(possibleMoves)):
            positionList.append(number)
        
        combList = []
        for number in range(len(possibleMoves) + 1):
            dummyList = list(combinations(positionList, number))
            for element in dummyList:
                combList.append(element)
                
        newPermList = []
        for comb in combList:
            dummyPerm = []
            for moveNumber in range(len(possibleMoves)):
                if moveNumber in comb:
                    newElement = [possibleMoves[moveNumber][1], possibleMoves[moveNumber][0]]
                else:
                    newElement = [possibleMoves[moveNumber][0], possibleMoves[moveNumber][1]]
                dummyPerm.append(newElement)
            newPermList.append(dummyPerm)
        
        permDict = {}
        winningSet = []
        winningMatrices = []
        game = 0
        
        for player in range(player_number):
            permDict[player] = 0
        
        for perm in newPermList:
            alreadyPlayed = False
            for gamesPlayed in winningSet:
                alreadyPlayed = True
                for movePlayed in range(len(gamesPlayed)):
                    if not gamesPlayed[movePlayed] == perm[movePlayed]:
                        alreadyPlayed = False
                        break
                if alreadyPlayed:
                    break
            
            if not alreadyPlayed:
                currentPlayer = 0
                movesMade = []
                for move in perm:
                    if self.addDirection(move[0], move[1], False):
                        currentPlayer += 1
                    else:
                        if self.checkWin():
                            winningSet.append(movesMade)
                            break
                        elif self.checkUnmarkable(move[0], move[1]):
                            break
                    movesMade.append(move)
                if self.checkWin():
                    if self.matrix in winningMatrices:
                        game -= 1
                        permDict[currentPlayer%player_number] -= 1
                    else:
                        winningMatrices.append(copy.deepcopy(self.matrix))
                    permDict[currentPlayer%player_number] += 1
                    game += 1
                for row in range(self.size):
                    for column in range(self.size):
                        if self.matrix[row][column] > 1:
                            self.matrix[row][column] = 1
       
        print("")
        for matrix in winningMatrices:
            for row in matrix:
                print(row)
            print("")
        print("Games played: " + str(game))
        for player in permDict:
            if player == 0:
                print("Player " + str(player_number) + " won " + str(round(permDict[player]/game * 100, 2)) + "% of games")
            else:
                print("Player " + str(player) + " won " + str(round(permDict[player]/game * 100, 2)) + "% of games")
                
                    
                    
'''test3 = GameofCycles(6)

test3.addEdge(0,1)

test3.addEdge(0,2)

test3.addEdge(1,2)

test3.addEdge(2,3)

test3.addEdge(3,4)

test3.addEdge(3,5)

test3.addEdge(4,5)

print()

test3.playGame(2)'''



'''test = GameofCycles(11)

test.addEdge(1,0)

test.addEdge(2,1)

test.addEdge(3,1)

test.addEdge(4,3)

test.addEdge(5,4)

test.addEdge(6,4)

test.addEdge(7,6)

test.addEdge(8,6)

test.addEdge(9,6)

test.addEdge(10,6)

print()

'''

'''test.addDirection(7, 6)
test.addDirection(8, 6)
test.addDirection(9, 6)
test.addDirection(4, 6)
#test.addDirection(10, 6)
test.addDirection(5, 4)
test.addDirection(3, 4)
test.addDirection(1, 3)
test.addDirection(2, 1)
test.addDirection(0, 1)'''

#test.playGame(2)

#test.showMatrix()

#print(test.checkWin())

#print(test.checkUnmarkable(10,6))


"""
test2 = GameofCycles(6)

test2.addEdge(0,1)

test2.addEdge(2,1)

test2.addEdge(2,3)

test2.addEdge(2,4)

test2.addEdge(2,5)

print()

test2.addDirection(2, 1)

test2.addDirection(3, 2)

test2.addDirection(2, 4)

test2.addDirection(5, 2)

test2.showMatrix()

print(test2.checkUnmarkable(0, 1))
"""
"""
test3 = GameofCycles(6)

test3.addEdge(0,1)

test3.addEdge(0,2)

test3.addEdge(1,2)

test3.addEdge(2,3)

test3.addEdge(3,4)

test3.addEdge(3,5)

test3.addEdge(4,5)

print()

test3.addDirection(0,2)

test3.addDirection(1,2)

test3.addDirection(4,3)

test3.addDirection(5,3)

print()

test3.showMatrix()

print(test3.checkWin())
"""


'''test4 = GameofCycles(5)

for i in range(5):
    for j in range(5):
        if i < j:
            test4.addEdge(i, j)
        
print(test4.isPlanar())
test4.showMatrix()

test5 = GameofCycles(6)

test5.addEdge(0, 3)

test5.addEdge(0, 4)

test5.addEdge(0, 5)

test5.addEdge(1, 3)

test5.addEdge(1, 4)

test5.addEdge(1, 5)

test5.addEdge(2, 3)

test5.addEdge(2, 4)

test5.addEdge(2, 5)

print(test5.isPlanar())
test5.showMatrix()'''

test6 = GameofCycles(7)

test6.addEdge(0, 1)

test6.addEdge(1, 2)

test6.addEdge(2, 3)

test6.addEdge(3, 4)

test6.addEdge(4, 5)

test6.addEdge(4, 6)

test6.showMatrix()

test6.simulateGame(2)

'''
test7 = GameofCycles(6)

test7.makePath()

test7.showMatrix()

test7.simulateGame(2)

#test7.simulateGame(3)
'''
