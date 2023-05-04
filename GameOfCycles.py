"""
Created on Tue Nov 15 10:40:05 2022
@author: Bushra Ibrahim and Brian Feeeman
"""

from itertools import combinations, permutations
import random
import copy

# 2 is out
# 3 is in 
# on a path

class GameofCycles:
    
    # Creates the Game of Cycles of given size
    def __init__(self, size):
        self.matrix = [] # Adjacency matrix for edes
        self.size = size
        for pointOne in range(self.size):
            self.matrix.append([])
            for pointTwo in range(self.size):
                self.matrix[pointOne].append(0)
        self.cycle = False
        self.path = False
        self.edgeList = [] # List of edges in graph
        self.cellList = [] # List of valid cells
    
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
            # Fails if the edge would make the graph nonplanar
            if not self.isPlanar():
                self.matrix[pointOne][pointTwo] = 0
                self.matrix[pointTwo][pointOne] = 0
                print("That edge would make the graph nonplanar")
        # Fails if the edge is already in the graph
        elif not self.matrix[pointOne][pointTwo] == 0:
            print("That edge is already in the matrix")
        # Fails if the edge points a vertex to itself
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
    # printError being True returns error, which is only used for player games
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
                # Checks if pointOne is a leaf vertex
                if not self.matrix[i][pointOne] == 0:
                    leafOne += 1
                
                # Checks if pointOne has unmarked edges
                if self.matrix[i][pointOne] == 1:
                    sourceORsinkOne = False
                    break
                
                # Checks if pointOne has two edges pointing opposite directions
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
                # Checks if pointTwo is a leaf vertex
                if not self.matrix[i][pointTwo] == 0:
                    leafTwo += 1
                    
                 # Checks if pointTwo has unmarked edges
                if self.matrix[i][pointTwo] == 1:
                    sourceORsinkTwo = False
                    break
                
                # Checks if pointTwo has two edges pointing opposite directions
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
            
            # Fails if making the move creates a source or sink
            if sourceORsinkOne or sourceORsinkTwo:
                if printError:
                    print("That move creates a source or a sink.")
                self.matrix[pointOne][pointTwo] = 1
                self.matrix[pointTwo][pointOne] = 1
                return False
            else:
                return True
        # Fails if the edge is not in the edge list or is already marked
        else:
            if printError:
                print("This is an illegal move.")
            return False
        
    # Checks if the edge between two points is unmarkable
    def checkUnmarkable(self, pointOne, pointTwo):
        pointOneDirection = 1
        rowOne = 1
        columnOne = 1
        leafValueRow = 0
        leafValueColumn = 0
        
        # Fails if both points are the same
        if pointOne == pointTwo:
            print("This is an illegal move.")
        
        for i in range(self.size):
            # Checks if pointOne is a leaf
            if not self.matrix[i][pointOne] == 0:
                leafValueRow += 1
            
            # Checks if every edge pointing to pointOne going the same way
            # and has only one edge marked
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
        
        # Checks if every edge pointing to pointTwo going the same way
        # and has only one edge marked
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
        # If playing an edge in either direction causes a source or a sink, 
        # returns the edge is unmarkable
        else:
            return True
    
    # Checks if there is a winner
    def checkWin(self):
        used = 0
        
        # Checks if every edge is either unmarkable or already marked
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
                        
                
        
        if used == len(self.edgeList):
            return True
        # Checks if any cells have been completed
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
                    print("That is not a legal move")
                    source = int(input("\nChoose a point to start from "))
                    destination = int(input("Choose a point to go to "))
                if self.checkWin():
                    self.showMatrix()
                    print("\nPlayer", playerTurn, "wins!")
                    winner = True
                    break
    
    # Plays the game against a computer player
    def playComputer(self):
        winner = False
        print("Would you like to be player 1 or player 2?")
        humanTurn = int(input("Type 1 for player 1 and 2 for player 2 "))
        while not winner:
            for playerTurn in range(1, 3):
                if playerTurn == humanTurn:
                    print("\nPlayer", str(playerTurn) + "'s turn\n")
                    self.showMatrix()
                    source = int(input("\nChoose a point to start from "))
                    destination = int(input("Choose a point to go to "))
                    while not self.addDirection(source, destination):
                        self.showMatrix()
                        print("That is not a legal move")
                        source = int(input("\nChoose a point to start from "))
                        destination = int(input("Choose a point to go to "))
                else:
                    possibleMoves = []
                    for row in range(self.size):
                        for column in range(self.size):
                            if self.matrix[row][column] == 1 and self.addDirection(row, column, False):
                                possibleMoves.append([row, column])
                                self.matrix[row][column] = 1
                                self.matrix[column][row] = 1
                    playWinning = False
                    edgeWinning = []
                    # Finds all moves that allow the computer to win
                    for moves in possibleMoves:
                        self.addDirection(moves[0], moves[1], False)
                        if self.checkWin():
                            playWinning = True
                            edgeWinning.append(moves)
                        self.matrix[moves[0]][moves[1]] = 1
                        self.matrix[moves[1]][moves[0]] = 1
                    # Runs if no move cause the computer to win
                    if not playWinning:
                        edgeNotLosing = {}
                        for moves in possibleMoves:
                            playLosing = False
                            unmarkables = 0
                            self.addDirection(moves[0], moves[1], False)
                            possibleMoves2 = []
                            for row in range(self.size):
                                for column in range(self.size):
                                    if self.matrix[row][column] == 1 and self.addDirection(row, column, False):
                                        possibleMoves2.append([row, column])
                                        self.matrix[row][column] = 1
                                        self.matrix[column][row] = 1
                            # Finds all moves that would allow the player to play a winning move
                            for moves2 in possibleMoves2:
                                if self.checkUnmarkable(moves2[0], moves2[1]):
                                    unmarkables += 100
                                self.addDirection(moves2[0], moves2[1], False)
                                # Finds how many unmarkable edges come from the player
                                # playing any of the remaining edges
                                for moves3 in possibleMoves2:
                                    if self.checkUnmarkable(moves3[0], moves3[1]):
                                        unmarkables += 1
                                if self.checkWin():
                                    playLosing = True
                                self.matrix[moves2[0]][moves2[1]] = 1
                                self.matrix[moves2[1]][moves2[0]] = 1
                            if not playLosing:
                                edgeNotLosing[str(moves)] = unmarkables
                            self.matrix[moves[0]][moves[1]] = 1
                            self.matrix[moves[1]][moves[0]] = 1
                        # Runs if there exists an edge that would not cause the computer to lose
                        if len(edgeNotLosing) > 0:
                            unmarkablesValue = self.size ** 2
                            unmarkablesList = []
                            # Finds the edge that creates the fewest number of unmarkable edges
                            for remainingEdges in edgeNotLosing:
                                if unmarkablesValue > edgeNotLosing[remainingEdges]:
                                    unmarkablesValue = edgeNotLosing[remainingEdges]
                                    unmarkablesList = [remainingEdges]
                                elif unmarkablesValue == edgeNotLosing[remainingEdges]:
                                    unmarkablesList.append(remainingEdges)
                            # Converts the move's string into a list
                            compChoice = random.choice(unmarkablesList)
                            compPsuedoList = compChoice.split(", ")
                            compMove = [int(compPsuedoList[0][1:]), int(compPsuedoList[1][:-1])]
                        # Runs if all moves cause the computer to lose
                        else:
                            compMove = random.choice(possibleMoves)
                    # Runs if a move exists where the computer wins
                    else:
                        compMove = edgeWinning[0]
                    print("The computer played: " + str(compMove))
                    self.addDirection(compMove[0], compMove[1])
                if self.checkWin():
                    self.showMatrix()
                    print("\nPlayer", playerTurn, "wins!")
                    winner = True
                    break
                    
    
    # Simulates a board at a given state to see winners on different end states
    # Only turn on thorough to see every end state as it is very slow
    def simulateGame(self, player_number, thorough = False):
        startingBoard = copy.deepcopy(self.matrix)
        markedStart = False
        startingPlayer = 0
        
        # Checks who should play first, as a marked board can be inserted
        for row in range(self.size):
            for column in range(self.size):
                if self.matrix[row][column] > 1:
                    markedStart = True
                    startingPlayer += 1
                    
        startingPlayer = int(startingPlayer/2)
        
        # Finds all possible moves in one direction
        possibleMoves = []
        for row in range(self.size):
            for column in range(self.size):
                if self.matrix[row][column] == 1 and row < column:
                    possibleMoves.append([row, column])
        
        # Creates a list of numbers from 0 to number of playable moves
        positionList = []
        for number in range(len(possibleMoves)):
            positionList.append(number)
        
        # Creates a list of all combination of numbers in the positionList
        combList = []
        for number in range(len(possibleMoves) + 1):
            dummyList = list(combinations(positionList, number))
            for element in dummyList:
                combList.append(element)
        
        # Creates a list that flips the direction of certain moves to get all combinations
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
        
        # Randomly picks played move orders if not thorough
        if not thorough:
            for perm in permList:
                randomPositions = []
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
        # Finds every played move order if thorough
        else:
            for perm in permList:
                newPermutations = list(permutations((perm), len(perm)))
                for newPerm in newPermutations:
                    if newPerm[0][0] < newPerm[0][1] or markedStart:
                        newPermList.append(newPerm)
        
        # Prints the number of orders of moves that will be simulated
        print(len(newPermList))
        permDict = {}
        movesMadeDict = {}
        winningSet = []
        winningMatrices = []
        correspondingWinner = []
        game = 0
        
        for player in range(player_number):
            permDict[player] = 0
        
        firstMovesPlayer1 = {}
        firstMovesPlayer2 = {}
        
        # Was going to find first two moves, gave up since lost interest
        '''firstTwoMovesPlayer1 = {}
        firstTwoMovesPlayer2 = {}'''
        
        # Looks at every permutation
        for perm in newPermList:
            alreadyPlayed = False
            # Checks if the beginning part of a sequence of moves has already been played
            for gamesPlayed in winningSet:
                alreadyPlayed = True
                for movePlayed in range(len(gamesPlayed)):
                    if not gamesPlayed[movePlayed] == perm[movePlayed]:
                        alreadyPlayed = False
                        break
                if alreadyPlayed:
                    break
            
            # Will run if not already played or all games are being simulated
            if not alreadyPlayed or thorough:
                currentPlayer = startingPlayer
                movesMade = []
                # Plays until an illegal move is played, all moves are played,
                # or a winner was found
                for move in perm:
                    if self.checkWin():
                        winningSet.append(movesMade)
                        break 
                    elif self.addDirection(move[0], move[1], False):
                        currentPlayer += 1
                    else:
                        break
                    movesMade.append(move)
                # Checks if a winner is found
                if self.checkWin():
                    if str(movesMade) not in movesMadeDict and thorough:
                        movesMadeDict[str(movesMade)] = str(movesMade)
                        newMovesMade = True
                    else:
                        newMovesMade = False
                    if self.matrix in winningMatrices and (not thorough or not newMovesMade):
                        game -= 1
                        permDict[currentPlayer%player_number] -= 1
                    else:
                        # Adds the end state to the winningMatrices list if it is a new win
                        if not self.matrix in winningMatrices:
                            correspondingWinner.append(currentPlayer%player_number)
                        if thorough:
                            if self.matrix in winningMatrices:
                                game -= 1
                                permDict[currentPlayer%player_number] -= 1
                            # Prints number of completed games to show the program's progress
                            else:
                                print("Current game: " + str(game))
                                winningMatrices.append(copy.deepcopy(self.matrix))
                        else:
                            winningMatrices.append(copy.deepcopy(self.matrix))
                        # Finds the first move played on a board for player 1's win
                        if currentPlayer%player_number == 0:
                            if str([movesMade[0][1], movesMade[0][0]]) in firstMovesPlayer2:
                                if str([movesMade[0][1], movesMade[0][0]]) not in firstMovesPlayer1:
                                    firstMovesPlayer1[str([movesMade[0][1], movesMade[0][0]])] = 1
                                else:
                                    firstMovesPlayer1[str([movesMade[0][1], movesMade[0][0]])] += 1
                            elif str(movesMade[0]) in firstMovesPlayer2:
                                if str(movesMade[0]) in firstMovesPlayer1:
                                    firstMovesPlayer1[str(movesMade[0])] += 1
                                else:
                                    firstMovesPlayer1[str(movesMade[0])] = 1
                            else:
                                if str(movesMade[0]) in firstMovesPlayer1:
                                    firstMovesPlayer1[str(movesMade[0])] += 1
                                elif str([movesMade[0][1], movesMade[0][0]]) in firstMovesPlayer1:
                                    firstMovesPlayer1[str([movesMade[0][1], movesMade[0][0]])] += 1
                                else:
                                    firstMovesPlayer1[str(movesMade[0])] = 1
                        
                        # Finds the first move played on a board for player 2's win
                        else:
                            if str([movesMade[0][1], movesMade[0][0]]) in firstMovesPlayer1:
                                if str([movesMade[0][1], movesMade[0][0]]) not in firstMovesPlayer2:
                                    firstMovesPlayer2[str([movesMade[0][1], movesMade[0][0]])] = 1
                                else:
                                    firstMovesPlayer2[str([movesMade[0][1], movesMade[0][0]])] += 1
                            elif str(movesMade[0]) in firstMovesPlayer1:
                                if str(movesMade[0]) in firstMovesPlayer2:
                                    firstMovesPlayer2[str(movesMade[0])] += 1
                                else:
                                    firstMovesPlayer2[str(movesMade[0])] = 1
                            else:
                                if str(movesMade[0]) in firstMovesPlayer2:
                                    firstMovesPlayer2[str(movesMade[0])] += 1
                                elif str([movesMade[0][1], movesMade[0][0]]) in firstMovesPlayer2:
                                    firstMovesPlayer2[str([movesMade[0][1], movesMade[0][0]])] += 1
                                else:
                                    firstMovesPlayer2[str(movesMade[0])] = 1
                
                    permDict[currentPlayer%player_number] += 1
                    game += 1
                # Deep copies the matrix to prevent writing over the original
                # startingBoard object
                self.matrix = copy.deepcopy(startingBoard)
        
        bestMoveValue = 0
        worstMoveValue = 1
        bestMove = "none"
        worstMove = "none"
        
        # Finds which move had the best winrate and worst winrate for player 1
        for move in firstMovesPlayer2:
            if move not in firstMovesPlayer1:
                winrate = 1
            else:
                winrate = firstMovesPlayer2[move]/ (firstMovesPlayer1[move] + firstMovesPlayer2[move])
            if bestMoveValue <= winrate:
                bestMoveValue = winrate
                bestMove = move
            if worstMoveValue >= winrate:
                worstMoveValue = winrate
                worstMove = move
        
        # Runs if player 1 cannot win on a given board
        for move in firstMovesPlayer1:
            if move not in firstMovesPlayer2:
                worstMoveValue = 0
                worstMove = move
        
        # Writes out the data onto a text file called Current_Game.txt
        outfile = open("Current_Game.txt", "w")
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
        outfile.write("Player 1's best first move is "  + bestMove + " with a winrate of " + str(round(bestMoveValue, 3)) + "\n")
        outfile.write("Player 1's worst first move is "  + worstMove + " with a winrate of " + str(round(worstMoveValue, 3)) + "\n")
            
        outfile.close()
