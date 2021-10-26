from Game import *
import chess
from copy import deepcopy
class chessGame (Game):



    def __init__(self,state=None):
        self.turn = 1
        self.player1 = "BLACK"                  # Ordinateur
        self.player2 = "WHITE"                  # joueur
        self.winner = None
        self.state = state  # état du jeu ( les cases restantes)
        self.Score = 0
        self.board = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"


        '''        
    
         CurrentGameState de type : {Board:  
        r n b q k b n r
        p p p p p p p p
        . . . . . . . .
        . . . . . . . .
        . . . . . . . .
        . . . . . . . .
        P P P P P P P P
        R N B Q K B N R,
                     nextPlayer: " Black", 'value':''
                }
        
            '''


    def possibleMoves(self, board=None):
        '''
        function that returns the possible moves from a given game state
        :return: list of possible moves
        '''

        if board == None:
            ChessInstance = chess.Board(self.board)
            moves = list(ChessInstance.legal_moves)
            moves = [str(i) for i in moves]
            return moves
        else:
            ChessInstance = chess.Board(board)
            moves = list(ChessInstance.legal_moves)
            moves = [str(i) for i in moves]
            return moves


    def change_player(self):
        pass



    def display_state(self,board):
        '''
        diplaying state of the game (for debug)
        :param board:
        :return:
        '''
        print(chess.Board(board))



    def UpdateBoard(self, move, state, nextPlayer):
        '''
        for updating the board from a given state
        :param move:
        :param state:
        :param nextPlayer:
        :return:
        '''
        ChessInstance = chess.Board(state['board'])
        childboard = deepcopy(ChessInstance)
        childboard.push(chess.Move.from_uci(move))
        newstate = {'board': childboard.fen(), 'nextPlayer': nextPlayer, 'value': move}
        return newstate



    def play(self, currentGameState, Coup=None, Rollout=None):
        '''
        function that play chess game from a game state
        :param currentGameState:
        :param Coup:
        :param Rollout:
        :return: the new state of the game
        '''
        GameTurn = currentGameState['nextPlayer']
        chessInstance = chess.Board(currentGameState['board'])
        if Rollout == None:
            if (GameTurn == "WHITE"):  # tour du joueur

                chessInstance.push(chess.Move.from_uci(Coup))
                # next_player = self.Nextplayer(board)
                self.display_state(chessInstance.fen())  # interface
                self.HasWon(chessInstance.fen())
                return {'board': chessInstance.fen(), 'nextPlayer': "BLACK", 'value': Coup}

            else:  # tour de l'ordinateur
                chessInstance.push(chess.Move.from_uci(Coup))
                self.display_state(chessInstance.fen())  # interface
                self.HasWon(chessInstance.fen())
                return {'board': chessInstance.fen(), 'nextPlayer': "WHITE", 'value': Coup}

        else:  # rollout
            chessInstance = chess.Board(currentGameState['board'])
            chessInstance.push(chess.Move.from_uci(Coup))
            next_player = self.Nextplayer(chessInstance.fen())
            return {'board': chessInstance.fen(), 'nextPlayer': next_player, 'value': Coup}

    def Nextplayer(self, board):
        '''
                function that check the next player
        :param board:

        :return:  "black" ou "White"
        '''
        chessInstance = chess.Board(board)
        if chessInstance.turn == chess.BLACK:
            return "BLACK"
        else:
            return "WHITE"



    def HasWon(self, board=None):
        '''
        function to check the winner by giving a game state
        :param board:
        :return:
        '''
        if board == None:
            chessInstance = chess.Board(self.board)
            resultat = chessInstance.outcome()
            if resultat == None:
                return None                 # pas encore de vainqueur
            elif resultat.winner == True:  # white won
                self.winner = 2
                return -1
            elif resultat.winner == False:      #  black won
                self.winner = 1
                return +1  # black won
            elif resultat ==None:
                self.winner = 0
                return 0                        # draw

        else:
            chessInstance = chess.Board(board)
            resultat = chessInstance.outcome()
            if resultat == None:
                return None  # pas encore de vainqueur
            elif resultat.winner == True:  # white won
                self.winner = 1
                return +1
            elif resultat.winner == False:  # black won
                self.winner = 2
                return -1  # black won
            else:
                self.winner = 0
                return 0  # draw














