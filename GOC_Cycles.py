from GameofCycles import *
from itertools import combinations, permutations

def adjacentEdges(GoC):
    adjacentList = []
    
    for edge in range(GoC.size):
        adjacentList.append([])
    
    for edge in GoC.edgeList:
        adjacentList[edge[0]].append(edge[1])
        adjacentList[edge[1]].append(edge[0])
        
    return adjacentList
        
def findAllCycles(GoC, adjacentList):
    if GoC.size > 2:
        cyclesList = []
        verticesList = []
        combList = []
        
        for vertex in range(GoC.size):
            verticesList.append(vertex)
        
        for number in range(3, GoC.size + 1):
            dummyList = list(combinations(verticesList, number))
            for element in dummyList:
                combList.append(element)
                
        for combination in combList:
            cycle = True
            numAdjacency = [0] * GoC.size
            
            for vertex in combination:
                for vertex2 in combination:
                    if vertex == vertex2:
                        pass
                    else:
                        if vertex2 in adjacentList[vertex]:
                            numAdjacency[vertex2] += 1
            
            for adjacencies in range(GoC.size):
                if adjacencies in combination and numAdjacency[adjacencies] < 2:
                    cycle = False
            
            if cycle:
                cyclesList.append(combination)
        
        if len(cyclesList) > 0:
            return cyclesList
        else:
            return None
        
    else:
        return None
    
def orderCycles(adjacentList, cyclesList):
    ordCyclesList = []
    for cycle in cyclesList:
        permList = list(permutations(cycle, len(cycle)))
        for permutation in permList:
            isCycle = True
            for vertex in range(len(cycle) - 1):
                if permutation[vertex] not in adjacentList[permutation[vertex + 1]]:
                    isCycle = False
            if isCycle:
                ordCyclesList.append(permutation)
                break
    return ordCyclesList

def findCells(cyclesList):
    stringList = []
    cellList = []
    
    for cycle in cyclesList:
        currString = ""
        for vertex in cycle:
            currString += str(vertex)
        
        cell = True
        for string in stringList:
            if string in currString:
                cell = False
            
        if cell:
            permList = list(permutations(cycle, len(cycle)))
            for permutation in permList:
                currString = ""
                for vertex in permutation:
                    currString += str(vertex)
                stringList.append(currString)
            cellList.append(cycle)
            
    return cellList
    
    

def main():
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

    print("edges:")
    print(test.edgeList)
    print()
    
    adjacentList = adjacentEdges(test)
    
    print("adjacencies:")
    print(adjacentList)
    print()
    
    cyclesList = findAllCycles(test, adjacentList)
    
    print("vertices in a cycle:")
    print(cyclesList)
    print()
    
    ordCyclesList = orderCycles(adjacentList, cyclesList)
    
    print("all cycles:")
    print(ordCyclesList)
    print()
    
    cellList = findCells(ordCyclesList)
    
    print("cells:")
    print(cellList)
    print()
    
main()