#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 09:28:04 2022

@author: bushra
"""

# 1 - graph with 7 vertices and 3 cycles

test = GameofCycles(7)
test.addEdge(5,4)
test.addEdge(4,0)
test.addEdge(0,5)
test.addEdge(1,3)
test.addEdge(4,1)
test.addEdge(2,3)
test.addEdge(1,6)
test.addEdge(1,6)
test.addEdge(3,0)
test.addEdge(6,2)

# 2 - tree with 11 vertices

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

# 3 - graph with 8 verticies and 2 cycles

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

# 5 - graph with 9 vertices with 3 cycles

test = GameofCycles(9)
test.addEdge(0,3)
test.addEdge(0,2)
test.addEdge(2,3)
test.addEdge(1,3)
test.addEdge(1,2)
test.addEdge(5,4)
test.addEdge(6,4)
test.addEdge(7,8)
test.addEdge(1,6)
test.addEdge(1,7)
test.addEdge(8,6)

# 6 - graph with 10 vertices and 7 cycles (DFS struggling)

test = GameofCycles(10)
test.addEdge(0,1)
test.addEdge(0,4)
test.addEdge(1,2)
test.addEdge(2,3)
test.addEdge(3,6)
test.addEdge(6,8)
test.addEdge(8,9)
test.addEdge(9,7)
test.addEdge(7,4)
test.addEdge(4,1)
test.addEdge(7,8)
test.addEdge(2,5)
test.addEdge(5,1)
test.addEdge(8,5)
test.addEdge(7,5)
test.addEdge(2,6)

# 7 - graph with 10 vertices and 5 cycles

test = GameofCycles(10)

test.addEdge(4,0)
test.addEdge(7,1)
test.addEdge(3,8)
test.addEdge(2,7)
test.addEdge(9,1)
test.addEdge(6,3)
test.addEdge(1,8)
test.addEdge(4,2)
test.addEdge(7,4)
test.addEdge(6,1)
test.addEdge(7,5)
test.addEdge(9,7)
test.addEdge(5,1)
test.addEdge(0,7)

# 8 - graph with 6 vertices and 1 cycle 

test.addEdge(0,1)
test.addEdge(0,3)
test.addEdge(1,2)
test.addEdge(3,2)
test.addEdge(5,4)
test.addEdge(3,4)

# 9 - graph with 15 vertices and 4 cycles (edited for testing later)

test = GameofCycles(15)

test.addEdge(0,4)
test.addEdge(0,11)
test.addEdge(4,5)
test.addEdge(4,7)
test.addEdge(7,10)
test.addEdge(10,12)
test.addEdge(11,14)
test.addEdge(14,2)
test.addEdge(2,1)
test.addEdge(1,11)
test.addEdge(5,14)
test.addEdge(12,9)
test.addEdge(9,3)
test.addEdge(3,6)
test.addEdge(6,12)
test.addEdge(6,13)
test.addEdge(13,8)
test.addEdge(8,14)

# 10 - graph with 5 vertices and 3 cycles (DFS can't handle)

test = GameofCycles(5)

test.addEdge(0,3)
test.addEdge(4,1)
test.addEdge(0,4)
test.addEdge(2,3)
test.addEdge(0,2)
test.addEdge(4,2)
test.addEdge(2,1)

# 11 - graph with 4 vertices and 2 cycles (DFS can't handle - smallest instance?)

test = GameofCycles(5) #it can handle it in this order, but not a different order

test.addEdge(0,1)
test.addEdge(0,2)
test.addEdge(0,3)
test.addEdge(1,2)
test.addEdge(3,2)

# 12 - graph with 6 vertices and 3 cycles (DFS handles in this order)

test = GameofCycles(6)

test.addEdge(0,1)
test.addEdge(0,4)
test.addEdge(0,5)
test.addEdge(1,2)
test.addEdge(1,3)
test.addEdge(2,3)
test.addEdge(3,4)
test.addEdge(4,5)

# 13 - graph with 4 verices and 3 cycles (K4) (DFS can't handle)

test = GameofCycles(4)

test.addEdge(0,1)
test.addEdge(0,2)
test.addEdge(0,3)
test.addEdge(1,3)
test.addEdge(1,2)
test.addEdge(2,3)

# 14 - graph with 3 vertices and 1 cycle (a triangle)

test = GameofCycles(3)

test.addEdge(0,1)
test.addEdge(0,2)
test.addEdge(2,1)

# 15 - graph with 4 vertices and 1 cycle (a square)

test = GameofCycles(4)

test.addEdge(0,2)
test.addEdge(1,3)
test.addEdge(3,0)
test.addEdge(1,2)

# 16 - graph with 5 vertices and 2 cycles (a house)

test = GameofCycles(5)

test.addEdge(4,3)
test.addEdge(2,1)
test.addEdge(3,0)
test.addEdge(1,4)
test.addEdge(0,2)

