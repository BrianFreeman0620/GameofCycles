#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 10:40:05 2022
@author: bushra and brian
"""

from itertools import combinations
import random
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
        self.edgeList = []
        self.cellList = [] 
    
    # Shows the adjacency matrix            
    def showMatrix(self):
        for row in self.matrix:
            print(row)
            
    # Returns the adjaceny matrix
    def returnMatrix(self):
        matrixString = ""
        for row in self.matrix:
            matrixString += str(row) + "\n"
        return matrixString
    
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
            self.edgeList.append([pointOne, pointTwo])
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
    
    # Allows user to manually enter possible cycle cells
    def addCycle(self, cycleCell):
        self.cellList.append(cycleCell)
    
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
                    #elif self.matrix[i][j] == 
                    else:
                        used += 1
                        
                
        
        if used == len(self.edgeList):
            return True
        else:
            for cycle in self.cellList:
                completeCycle = True
                currentDirection = 4
                for vertex in range(len(cycle)):
                    if vertex == 0:
                        if self.matrix[cycle[vertex]] [cycle[vertex-1]] in [2,3]:
                            currentDirection = self.matrix[cycle[vertex]][cycle[vertex-1]]
                    else:
                        if not currentDirection == self.matrix[cycle[vertex]] [cycle[vertex-1]]:
                            completeCycle = False
                if completeCycle:
                    return True
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
                
    def simulateGame(self, player_number, hasCycles = False):
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
        
        permList = []
        for comb in combList:
            dummyPerm = []
            for moveNumber in range(len(possibleMoves)):
                if moveNumber in comb:
                    newElement = [possibleMoves[moveNumber][1], possibleMoves[moveNumber][0]]
                else:
                    newElement = [possibleMoves[moveNumber][0], possibleMoves[moveNumber][1]]
                dummyPerm.append(newElement)
            permList.append(dummyPerm)
        
        newPermList = []
        for perm in permList:
            randomPositions = []
            if not hasCycles:
                for position in range(len(perm)):
                    randomPositions.append([])
                    for position2 in range(len(perm)):
                        randomPositions[position].append(position2)
                    random.shuffle(randomPositions[position])
                
                newPerms = []
                
                for permutation in range(len(perm)):
                    newPerms.append([])
                    for move in range(len(perm)):
                        newPerms[permutation].append(perm[randomPositions[permutation][move]])
                    
                    newPermList.append(newPerms[permutation])
            else:
                for squarePosition in range(len(perm)):
                    for position in range(len(perm)):
                        randomPositions.append([])
                        for position2 in range(len(perm)):
                            randomPositions[(len(perm) * squarePosition) + position].append(position2)
                        random.shuffle(randomPositions[(len(perm) * squarePosition) + position])
            
                newPerms = []
                
                for squarePosition in range(len(perm)):
                    for permutation in range(len(perm)):
                        newPerms.append([])
                        for move in range(len(perm)):
                            newPerms[permutation].append(perm[randomPositions[(len(perm) * squarePosition) + position][move]])
                        
                        newPermList.append(newPerms[permutation])
        
        print(len(newPermList))
        
        permDict = {}
        winningSet = []
        winningMatrices = []
        correspondingWinner = []
        game = 0
        
        for player in range(player_number):
            permDict[player] = 0
        
        for perm in newPermList:
            alreadyPlayed = False
            if not hasCycles:
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
                if hasCycles:
                    random.shuffle(perm)
                for move in perm:
                    if self.checkWin():
                        winningSet.append(movesMade)
                        break 
                    elif self.addDirection(move[0], move[1], False):
                        currentPlayer += 1
                    else:
                        if self.checkWin():
                            winningSet.append(movesMade)
                            break
                        elif self.checkUnmarkable(move[0], move[1]):
                            if not hasCycles:
                                break
                    movesMade.append(move)
                if self.checkWin():
                    if self.matrix in winningMatrices:
                        game -= 1
                        permDict[currentPlayer%player_number] -= 1
                    else:
                        winningMatrices.append(copy.deepcopy(self.matrix))
                        if currentPlayer%player_number == 0:
                            correspondingWinner.append(player_number)
                        else:
                            correspondingWinner.append(currentPlayer%player_number)
                    permDict[currentPlayer%player_number] += 1
                    game += 1
                for row in range(self.size):
                    for column in range(self.size):
                        if self.matrix[row][column] > 1:
                            self.matrix[row][column] = 1

        if not hasCycles:
            outfile = open("Current_Trees.txt", "w")
        else:
            outfile = open("Current_Cycles.txt", "w")
        outfile.write(self.returnMatrix())
        for matrix in range(len(winningMatrices)):
            outfile.write("Game " + str(matrix + 1) + ": Player " + str(correspondingWinner[matrix]) + " win\n")
            for row in winningMatrices[matrix]:
                outfile.write(str(row) + "\n")
            outfile.write("\n")
        outfile.write("Games played: " + str(game) + "\n")
        for player in permDict:
            if player == 0:
                outfile.write("Player " + str(player_number) + " won " + str(round(permDict[player]/game * 100, 2)) + "% of games\n")
            else:
                outfile.write("Player " + str(player) + " won " + str(round(permDict[player]/game * 100, 2)) + "% of games\n")
                
        outfile.close()
                
                    
test = GameofCycles(7)
test.addEdge(5,4)
test.addEdge(4,0)
test.addEdge(0,5)
test.addEdge(1,3)
test.addEdge(4,1)
test.addEdge(2,3)
test.addEdge(1,6)
test.addEdge(3,0)
test.addEdge(6,2)

test.addCycle([0,4,5])
test.addCycle([1,3,0,4])
test.addCycle([1,6,2,3])

test.addDirection(1,6)
test.addDirection(6,2)
test.addDirection(3,1)
test.addDirection(2,3)
test.showMatrix()

test.simulateGame(2, True)
