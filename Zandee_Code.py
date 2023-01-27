#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 13:39:54 2023

@author: bushra
"""

from copy import deepcopy

class Graph():
    def __init__(self, graph_dict = None, cycles = None):
        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict
        self.keys = self.graph_dict.keys()
        self.moves = []
        self.cycles = cycles
        for i in self.keys:
            keys = self.graph_dict[i].keys()
            for j in keys:
                self.moves.append(i+j)
        self.startNumOfMoves = len(self.moves)
    
    def direct(self, move):
        origin = move[0]
        destination = move[1]
        self.graph_dict[origin][destination] = 1
        self.graph_dict[destination][origin] = -1
        self.moves.remove(move)
        if destination+origin in self.moves:
            self.moves.remove(destination+origin)
        if sum(self.graph_dict[origin].values()) == len(self.graph_dict[origin]) - 1:
            for i in self.moves:
                if i[0] == origin:
                    self.moves.remove(i)
        if sum(self.graph_dict[destination].values()) == 1 - len(self.graph_dict[destination]):
            for i in self.moves:
                if i[1] == destination:
                    self.moves.remove(i)
        
    def check_cycles(self, move):
        for cycle in self.cycles:
            if move in cycle:
                tot = 0
                for i in range(len(cycle) -1):
                    tot += self.graph_dict[cycle[i]][cycle[i+1]]
                if tot == len(cycle) -1:
                    return True
        return False
    
memory = []
memory2 = {}
index = -1

def mex(lst):
    ordinal = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    for i in ordinal:
        if i in lst:
            pass
        else:
            return i

def is_legal(graph, move):
    for cycle in graph.cycles:
        if move in cycle:
            tot = 0
            for i in range(len(cycle)-1):
                tot += graph.graph_dict[cycle[i]][cycle[i+1]]
            if tot == len(cycle) -2:
                return False
    return True

def brute_force(g, c):
    test = Graph(g, c)
    memory.append([deepcopy(test.graph_dict), deepcopy(test.moves), 0, None, []])
    makemove(test)

def makemove(graph):
    while True:
        if graph.moves != [] and memory[-1][2] < len(memory[-1][1]):
            nextmove = memory[-1][1][memory[-1][2]]
            graph.direct(nextmove)
            memory[-1][2] += 1
            
            if is_legal(graph, nextmove):
                memory.append([deepcopy(graph.graph_dict), deepcopy(graph.moves), 0, None, []])
                if str(memory[-1][0]) in memory2.keys():
                    memory[-1][3] = memory2[str(memory[-1][0])]
                    graph.moves = []
                    
                elif graph.check_cycles(nextmove):
                    graph.moves = []
                    memory[-1][3] = 0
                    
            else:
                graph.graph_dict = deepcopy(memory[-1][0])
                graph.moves = deepcopy(memory[-1][1])
        
        elif len(memory) == 1:
            memory[-1][3] = mex(deepcopy(memory[-1][4]))
            print(memory)
            return
        
        else:
            if memory[-1][3] == None:
                memory[-1][3] = mex(deepcopy(memory[-1][4]))
                
            if memory[-2][3] == None:
                memory[-2][4].append(deepcopy(memory[-1][3]))
                
            memory2[str(memory[-1][0])] = memory[-1][3]
            
            #if len(memory) == 3 and memory[-1][3] == 0:
                # print(memory[-1])
                
            memory.remove(memory[-1])
            graph.graph_dict = deepcopy(memory[-1][0])
            graph.moves = deepcopy(memory[-1][1])


brute_force(gcounter2, ccounter2)
































