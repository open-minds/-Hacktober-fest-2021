from Game import *
from copy import deepcopy
class TicTacToe (Game):



    def __init__(self,state=['1','2','3','4','5','6','7','8','9']):
        self.turn = 1
        self.player1 = "X"
        self.player2 = "O"
        self.winner = None
        self.state = state  # état du jeu ( les cases restantes)
        self.Score = 0
        self.board = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]


        '''
        self.board ={["X", "O", "X",
                      " ", "O", "O",
                      " ", " ", " "],
                      Qui va jouer ? O
        }
        
            '''

    def possibleMoves(self, board=None):
        '''
        fonction a utiliser lors du rollout, prends en parametre l'etat actuel du noeud ainsi que le noeud
        :return: une liste de mouvements possibles
        '''

        if board == None:
            return self.state
        else:
            possibleMove=[]
            for i in range(len(board)):
                if board[i] ==" ":
                    possibleMove.append(i+1)
            return possibleMove


    def UpdateBoard(self, move, state, nextPlayer):
        '''
        function that allows to update the state board with the attributes that are specific to the game played
        :param move:
        :param state:
        :param nextPlayer:
        :return: the new state of the updated board
        '''
        board = state['board']
        childboard = deepcopy(board)
        childboard[move - 1] = state['nextPlayer']
        newstate = {'board': childboard, 'nextPlayer': nextPlayer, 'value': move}
        return newstate



    def display_state(self,board):
        '''
        function that display states of the game in console
        (used for debug)
        :param board:
        :return:
        '''
        print(board[0] + " | " + board[1] + " | " + board[2])
        print(board[3] + " | " + board[4] + " | " + board[5])
        print(board[6] + " | " + board[7] + " | " + board[8])

    def change_player(self):
        '''
        function of tictactoe that changes the player turn in the game
        :return:
        '''
        if self.turn == 1:
            self.turn = 2
        elif self.turn == 2:
            self.turn = 1




    def play(self, currentGameState, Coup=None, Rollout=None):
        '''
        function of playing a move in tictactoe, and also used for rollout
        :param currentGameState:
        :param Coup:
        :param Rollout:
        :return: the new game state after playing the move
        '''

        GameTurn = currentGameState['nextPlayer']
        board = currentGameState['board']
        if Rollout == None:
            if (GameTurn == "X"):                                               # tour du joueur
                index = self.state.index(str(Coup))
                position = int(Coup) - 1
                if board[position] != " ":
                    raise RuntimeError("Mouvement incorrecte")

                board[position] = "X"
                currentGameState['board'] = board

                self.display_state(board)
                self.HasWon(board)
                return {'board': board, 'nextPlayer': "O", 'value': Coup}
            else:                                                                               # tour de l'ordinateur

                index = self.state.index(str(Coup))
                #            self.state.pop(index)
                position = int(Coup) - 1
                if board[position] != " ":
                    raise RuntimeError("Mouvement incorrecte")

                board[position] = "O"
                currentGameState['board'] = board

                self.display_state(board)
                self.HasWon(board)
                return {'board': board, 'nextPlayer': "X", 'value': Coup}
        else:
            if (GameTurn == "X"):
                index = self.state.index(str(Coup))
                #            self.state.pop(index)
                position = int(Coup) - 1
                if board[position] != " ":
                    raise RuntimeError("Mouvement incorrecte")

                board[position] = "X"
                currentGameState['board'] = board
                self.HasWon(board)
                return {'board': board, 'nextPlayer': "O", 'value': Coup}
            else:

                index = self.state.index(str(Coup))
                #            self.state.pop(index)
                position = int(Coup) - 1
                if board[position] != " ":
                    raise RuntimeError("Mouvement incorrecte")

                board[position] = "O"
                currentGameState['board'] = board
                self.HasWon(board)
                return {'board': board, 'nextPlayer': "X", 'value': Coup}



    def HasWon(self, board = None) -> int:
        '''
        function that check the game result at a T instant
        :param board:
        :return: +1 if computer win
                  -1 if computer lose
                  0 if draw
        '''
        if board == None:
            # rows
            if self.board[0] == self.board[1] == self.board[2] != " ":
                if self.board[0] == "X":
                    self.winner = 1
                elif self.board[0] == "O":
                    self.winner = 2
            if self.board[3] == self.board[4] == self.board[5] != " ":
                if self.board[3] == "X":
                    self.winner = 1
                elif self.board[3] == "O":
                    self.winner = 2
            if self.board[6] == self.board[7] == self.board[8] != " ":
                if self.board[6] == "X":
                    self.winner = 1
                elif self.board[6] == "O":
                    self.winner = 2

            # columns
            if self.board[0] == self.board[3] == self.board[6] != " ":
                if self.board[0] == "X":
                    self.winner = 1
                elif self.board[0] == "O":
                    self.winner = 2
            if self.board[1] == self.board[4] == self.board[7] != " ":
                if self.board[1] == "X":
                    self.winner = 1
                elif self.board[1] == "O":
                    self.winner = 2
            if self.board[2] == self.board[5] == self.board[8] != " ":
                if self.board[2] == "X":
                    self.winner = 1
                elif self.board[2] == "O":
                    self.winner = 2

            # diagonals
            if self.board[0] == self.board[4] == self.board[8] != " ":
                if self.board[0] == "X":
                    self.winner = 1
                elif self.board[0] == "O":
                    self.winner = 2
            if self.board[2] == self.board[4] == self.board[6] != " ":
                if self.board[2] == "X":
                    self.winner = 1
                elif self.board[2] == "O":
                    self.winner = 2

            if " " not in self.board and self.winner is None:
                self.winner = 0

            if (self.winner == 1):
                self.Score = -1  # utilisateur gagne

            elif self.winner == 2:
                self.Score = 1  # computer gagne

            else:
                self.Score = 0

            return self.winner
        else:                                   # cas de simulation on introduis un paramettre board
            # rows
            if board[0] == board[1] == board[2] != " ":
                if board[0] == "X":
                    self.winner = 1
                    return -1
                elif board[0] == "O":
                    self.winner = 2
                    return 1
            if board[3] == board[4] == board[5] != " ":
                if board[3] == "X":
                    self.winner = 1
                    return -1
                elif board[3] == "O":
                    self.winner = 2
                    return 1
            if board[6] == board[7] == board[8] != " ":
                if board[6] == "X":
                    self.winner = 1
                    return -1
                elif board[6] == "O":
                    self.winner = 2
                    return 1

            # columns
            if board[0] == board[3] == board[6] != " ":
                if board[0] == "X":
                    self.winner = 1
                    return -1
                elif board[0] == "O":
                    self.winner = 2
                    return 1
            if board[1] == board[4] == board[7] != " ":
                if board[1] == "X":
                    self.winner = 1
                    return -1
                elif board[1] == "O":
                    self.winner = 2
                    return 1
            if board[2] == board[5] == board[8] != " ":
                if board[2] == "X":
                    self.winner = 1
                    return -1
                elif board[2] == "O":
                    self.winner = 2
                    return 1

            # diagonals
            if board[0] == board[4] == board[8] != " ":
                if board[0] == "X":
                    self.winner = 1
                    return -1
                elif board[0] == "O":
                    self.winner = 2
                    return 1
            if board[2] == board[4] == board[6] != " ":
                if board[2] == "X":
                    self.winner = 1
                    return -1
                elif board[2] == "O":
                    self.winner = 2
                    return 1

            if " " not in board:                #and self. winner is none
                self.winner = 0
                return 0        # match nul














