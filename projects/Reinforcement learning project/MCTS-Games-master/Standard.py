from Game import *

class standard(Game):


    def __init__(self):
        '''
        this is the constructor of the game, here you put all the input param of your game instance
        '''



    def possibleMoves(self, board):
        '''
        the function that gives you the possibles moves from a given state
        :param board: the board of the game, must be a String
        :return: a list of all possible moves
        '''
        pass


    def display_state(self):
        '''
        the function that display the game state after a move of the player or the computer
        this function is not necessary if you have a GUI
        :return: the board of the game
        '''
        pass

    def change_player(self):
        '''
        the function that changes the player turn.
        You may not need this function in case of using a game library that manage the change of the players turn
        :param: you may need the actual player turn
        :return: the next player turn
        '''
        pass


    def UpdateBoard(self, move, state, nextPlayer):
        '''
        the function that update the game board in function of the last game board.
        :param move: the next player move
        :param state: the dictionnary of the last game state
        :param nextPlayer: the next player turn's
        :return: a dictionnary of the new game state
        '''
        pass

    def play(self, currentstate, coup=None, Rollout=None):
        '''
        the function for playing a move for each player.
        :param currentstate: the game state before playing the move
        :param coup: the move that will be played
        :param Rollout: a param that identify if the call of the function is for a rollout( rollout =1) or for a game play (rollout =None)
        :return: the gamestate after the move has been played
        '''
        pass


    def HasWon(self,board = None)-> int:
        '''
        the function that check if there is a winner after a move.
        :param board: the actual board of the game.
        :return: +1 if computer win, -1 if player win, 0 if draw
        '''
        pass