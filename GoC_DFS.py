#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 09:58:39 2022

@author: bushra
"""

"""

Adapted from Geeks for Geeks DFS code + Game of Cycles code

"""

from GameOfCycles_2 import *

test = GameofCycles(8)

test.addEdge(4,1)

test.addEdge(2,6)

test.addEdge(0,7)

test.addEdge(5,3)

test.addEdge(0,5)

test.addEdge(6,1)

test.addEdge(7,2)

test.addEdge(6,4)

test.addEdge(3,7)

n = 100 #setting a max number of cycles and reusing it for markers and parents
cycles = [[] for i in range(n)]


def GOC_DFS (COG, v1, v2, marker, parent): #u,p,color,par
    
    global cycleNumber #numbering each cycle found 
    
    def addEdge(u, v):
        graph[u].append(v)
        graph[v].append(u)
        
    graph = [[] for i in range(100)]
    for edge in COG.edgeList:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    
    if marker[v1] == 2: 
    #vertex is completely visited
        return
    
    if marker[v1] == 1: 
    #vertex is not completely visited - backtrack through parents & find cycle
    
        v = []
        cur = v2
        v.append(cur)
        
        #backtrack the vertex in the current cycle found
        while cur != v1:
            cur = parent[cur]
            v.append(cur)
        
        cycles[cycleNumber] = v #appending that cycle
        cycleNumber += 1 #incrementing cycle number
        
        return
    
    parent[v1] = v2 #making parent of v1 v2
    
    #partially visited marker = 1
    marker[v1] = 1
    
    #simple dfs (recursive)
    for v in graph[v1]:
        
        #not previously visited
        if v == parent[v1]:
            continue
        GOC_DFS(COG, v, v1, marker, parent)
        
    #completely visted marker = 2
    marker[v1] = 2

# Function to print the cycles
def print_GOC_Cycles():
 
    # print all the vertex with same cycle
    for i in range(0, cycleNumber):
 
        # Print the i-th cycle
        print("Cycle Number %d:" % (i+1), end = " ")
        for x in cycles[i]:
            print(x, end = " ")
        print()    


marker = [0] * n
parent = [0] * n
cycleNumber = 0

GOC_DFS(test, 0, 1, marker, parent)
print_GOC_Cycles()


"""
# 4 - graph with 6 vertices and 4 cycles (DFS can't handle this one)

test = GameofCycles(6)

test.addEdge(0,1)

test.addEdge(0,2)

test.addEdge(1,2)

test.addEdge(1,3)

test.addEdge(1,4)

test.addEdge(2,3)

test.addEdge(2,5)

test.addEdge(3,4)

test.addEdge(3,5)
"""
















