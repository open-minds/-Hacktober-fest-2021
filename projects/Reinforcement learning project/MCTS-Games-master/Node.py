import random
import pymongo
from pymongo import MongoClient
from copy import deepcopy

from Game import *
class TNode:

    ID = 0
    def __init__(self, parent: object, GameState, value=None ):
        self.id = TNode.ID+1
        TNode.ID += 1
        self.parent = parent
        self.children = []
        self.Visits = 0
        self.Score = 0
        self.value = value
        self.currentGameState = GameState


        '''CurrentGameState de type : {Board: ["X", "O", "X",
                              " ", "O", "O",
                              " ", " ", " "],
                     nextPlayer: "O", 'value':'1'
                }
        '''

    def is_leaf(self) -> bool:
        '''
        function that checks if a node is a leaf
        '''

        if(self.children == []):
            return True
        else:
            return False

    
    def is_terminal(self, game:Game, board) -> bool:
        '''

        function that checks if a node is terminal
        '''
        if game.HasWon(board) == None:
            return False
        else:
            return True


    def add_children(self, game: Game,currentState):
        '''
        function that add a children from a given game state
        :param game:
        :param currentState:
        :return:
        '''
        board = currentState['board']
        if currentState['nextPlayer'] == game.player1:
            nextPlayer = game.player2
        else:
            nextPlayer = game.player1
        for move in game.possibleMoves(board):
            newstate= game.UpdateBoard(move, currentState, nextPlayer)
            self.children.append(TNode(self, newstate, move))

