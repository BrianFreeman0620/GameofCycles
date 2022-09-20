#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 09:55:18 2022

@author: bushra
"""

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
    
   
    # Tries to add a direction to the game and returns True if the move is legal
    def addDirection(self, pointOne, pointTwo):
        if self.matrix[pointOne][pointTwo] == 1:
            self.matrix[pointOne][pointTwo] = 2
            self.matrix[pointTwo][pointOne] = 3
            
            sourceORsink = True
            edgeStatus = 1
            
            for i in range(self.size):
                if self.matrix[i][pointOne] == 1:
                    sourceORsink = False
                    break
                
                if self.matrix[i][pointOne] == 2:
                    if edgeStatus == 1:
                        edgeStatus = 2
                    if edgeStatus == 3:
                        sourceORsink = False
                        break
                    
                if self.matrix[i][pointOne] == 3:
                    if edgeStatus == 1:
                        edgeStatus = 3
                    if edgeStatus == 2:
                        sourceORsink = False
                        break
                    
            edgeStatus = 1
            
            for i in range(self.size):
                if self.matrix[i][pointTwo] == 1:
                    sourceORsink = False
                    break
                
                if self.matrix[i][pointTwo] == 2:
                    if edgeStatus == 1:
                        edgeStatus = 2
                    if edgeStatus == 3:
                        sourceORsink = False
                        break
                    
                if self.matrix[i][pointTwo] == 3:
                    if edgeStatus == 1:
                        edgeStatus = 3
                    if edgeStatus == 2:
                        sourceORsink = False
                        break
                
            if sourceORsink:
                print("That move creates a source or a sink.")
                self.matrix[pointOne][pointTwo] = 1
                self.matrix[pointTwo][pointOne] = 1
                return False
            else:
                return True
        else:
            print("This is an illegal move.")
            return False
        
    def checkUnmarkable(self, pointOne, pointTwo):
        pointOneFlavor = 1
        theOne = 1
        theOne2 = 1
        leafValueRow = 0
        
        for i in range(self.size):
            if self.matrix[i][pointOne] == 1 and theOne == 1:
                theOne = 0
            elif self.matrix[i][pointOne] == 1 and theOne == 0:
                return False
            elif pointOneFlavor == 1 and not self.matrix[i][pointOne] == 0:
                pointOneFlavor = self.matrix[i][pointOne]
            elif not pointOneFlavor == self.matrix[i][pointOne] and not self.matrix[i][pointOne] == 0:
                return False
            
        for j in range(self.size):
            if self.matrix[pointTwo][j] == 1 and theOne2 == 1:
                theOne2 = 0
            elif self.matrix[pointTwo][j] == 1 and theOne2 == 0:
                return False
            elif self.matrix[pointTwo][j] == pointOneFlavor:
                return False
            
        return True
  
#testing the code with a board with 11 vertices
#based on the graph I made up last Friday 

test = GameofCycles(11)

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

test.showMatrix()

print()

test2 = GameofCycles(6)

test2.addEdge(0,1)

test2.addEdge(2,1)

test2.addEdge(2,3)

test2.addEdge(2,4)

test2.addEdge(2,5)

test2.showMatrix()

print()

test2.addDirection(2, 1)

test2.addDirection(3, 2)

test2.addDirection(2, 4)

test2.addDirection(5, 2)

test2.showMatrix()

print(test2.checkUnmarkable(1, 0))

