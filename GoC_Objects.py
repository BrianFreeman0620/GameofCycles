#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 09:28:04 2022

@author: bushra

This is a non-exhaustive library of graphs we have entered
in the GoC form, to be reused so that we don't have to retype
certain graphs that we already have typed.

For graphs with cycles - a Y means it worked with the DFS
                         a N means it did not
"""
# 1 - graph with 7 vertices and 3 cycles - Y
#     (a triangle, and 2 quadrilaterals attached)

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

# 3 - graph with 8 verticies and 2 cycles - Y
#     (stick with triangle, stick with square)

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

# 4 - graph with 6 vertices and 4 cycles - N
#     (4 triangles within triangle)

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

# 5 - graph with 9 vertices with 3 cycles - Y
#     (square with diagonal, a quad attached to 1 vertex, and extra branch)

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

# 6 - graph with 10 vertices and 7 cycles - N
#     (larger stacked triangle, 5 3-cycles, 2 4-cycles)

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

# 7 - graph with 10 vertices and 5 cycles - N
#     (3 squares, 2 with diagonals, one without)

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

# 8 - graph with 6 vertices and 1 cycle - Y
#     (square with extra branch)

test.addEdge(0,1)
test.addEdge(0,3)
test.addEdge(1,2)
test.addEdge(3,2)
test.addEdge(5,4)
test.addEdge(3,4)

# 9 - graph with 15 vertices and 4 cycles - Y
#    (house with chimney and door)

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

# 10 - graph with 5 vertices and 3 cycles - N
#      (rectangle with triangle in it)

test = GameofCycles(5)

test.addEdge(0,3)
test.addEdge(4,1)
test.addEdge(0,4)
test.addEdge(2,3)
test.addEdge(0,2)
test.addEdge(4,2)
test.addEdge(2,1)

# 11 - graph with 4 vertices and 2 cycles - N*
#      (square with diagonal)

test = GameofCycles(5) 
#* except in this order
test.addEdge(0,1)
test.addEdge(0,2)
test.addEdge(0,3)
test.addEdge(1,2)
test.addEdge(3,2)

# 12 - graph with 6 vertices and 3 cycles - Y
#      (trapezoid with 1 triangle on each side)

test = GameofCycles(6)

test.addEdge(0,1)
test.addEdge(0,4)
test.addEdge(0,5)
test.addEdge(1,2)
test.addEdge(1,3)
test.addEdge(2,3)
test.addEdge(3,4)
test.addEdge(4,5)

# 13 - graph with 4 verices and 3 cycles - N
#      (K4, square with diagonal and external swoop)

test = GameofCycles(4)

test.addEdge(0,1)
test.addEdge(0,2)
test.addEdge(0,3)
test.addEdge(1,3)
test.addEdge(1,2)
test.addEdge(2,3)

# 14 - graph with 3 vertices and 1 cycle - Y
#      (a triangle)

test = GameofCycles(3)

test.addEdge(0,1)
test.addEdge(0,2)
test.addEdge(2,1)

# 15 - graph with 4 vertices and 1 cycle - Y
#      (a square)

test = GameofCycles(4)

test.addEdge(0,2)
test.addEdge(1,3)
test.addEdge(3,0)
test.addEdge(1,2)

# 16 - graph with 5 vertices and 2 cycles - N
#      (a house)

test = GameofCycles(5)

test.addEdge(4,3)
test.addEdge(2,1)
test.addEdge(3,0)
test.addEdge(1,4)
test.addEdge(0,2)

# 17 - graph with 8 vertices and 5 cycles - N
#      (square with a triangle on each side)

test = GameofCycles(8)

test.addEdge(0,1)
test.addEdge(1,2)
test.addEdge(2,3)
test.addEdge(3,4)
test.addEdge(4,5)
test.addEdge(5,6)
test.addEdge(6,7)
test.addEdge(7,0)
test.addEdge(1,3)
test.addEdge(3,5)
test.addEdge(5,7)
test.addEdge(7,1)
