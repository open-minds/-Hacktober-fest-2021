from abc import ABC, abstractmethod
class Game(ABC):

    @abstractmethod
    def __init__(self):
        pass



    @abstractmethod
    def possibleMoves(self, board):
        pass

    @abstractmethod
    def display_state(self):
        pass

    @abstractmethod
    def change_player(self):
        pass

    @abstractmethod
    def UpdateBoard(self, move, state, nextPlayer):
        pass

    @abstractmethod
    def play(self, currentstate, coup=None, Rollout=None):

        pass

    @abstractmethod
    def HasWon(self,board = None)-> int:
       pass

        



