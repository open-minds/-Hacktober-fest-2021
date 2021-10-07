import database
from Node import *
from TicTacToe import *
from chessGame import *
from TPlayer import *
from MCTS import *
from database import *


class main:

    def tictacTraining(self, Nbrpartie:int):
        '''
        function of tictactoe self-paly for training
        :param Nbrpartie: param that limit the number of game training
        :return: nothing
        '''
        tictac = TicTacToe()
        currentGameState = {'board': [" ", " ", " ", " ", " ", " ", " ", " ", " "], 'nextPlayer': "X", 'value': None}
        mcts = Mcts(tictac, 1)
        mcts.CurrentGameNode = mcts.initialize(tictac, currentGameState,
                                               "tictactoe")  # créer la racine et les fils de la racine

        for i in range(Nbrpartie):
            while tictac.HasWon(currentGameState['board']) == None:
                # jeux joueur 1

               # premier joueur MCTS

                currentGameState= mcts.ComputerVsComputer(tictac, currentGameState)

                if (tictac.HasWon(currentGameState['board']) == None):

                    currentGameState = mcts.ComputerVsComputer(tictac, currentGameState)
                    lastMCTSState = deepcopy(currentGameState)
                    tictac.HasWon(currentGameState['board'])

            print("the winner is the player", tictac.HasWon(currentGameState['board']))
            print("\n the final board", currentGameState['board'])
            currentGameState = {'board': [" ", " ", " ", " ", " ", " ", " ", " ", " "], 'nextPlayer': "X",
                                'value': None}
            mcts.CurrentGameNode = mcts.root

        data = connection("tictactoe")
        deleteTree(data)
        updateTreesearch(data, mcts.root)








    def chessTraining(self, Nbrpartie):
        '''
        function of chess self-paly for training
        (may need a powerfull computer to be tested)
        :param Nbrpartie:
        :return: nothing
        '''
        jeu = chessGame()
        currentGameState = {'board': deepcopy(jeu.board), 'nextPlayer': "WHITE", 'value': None}
        mcts = Mcts(jeu, 1)
        mcts.CurrentGameNode = mcts.initialize(jeu, currentGameState,
                                               "chess")  # créer la racine et les fils de la racine

        for i in range(Nbrpartie):
            while jeu.HasWon(currentGameState['board']) == None:
                # jeux joueur 1

                # premier joueur MCTS

                currentGameState = mcts.ComputerVsComputer(jeu, currentGameState)

                if (jeu.HasWon(currentGameState['board']) == None):
                    currentGameState = mcts.ComputerVsComputer(jeu, currentGameState)
                    lastMCTSState = deepcopy(currentGameState)
                    tictac.HasWon(currentGameState['board'])

            print("the winner is the player", jeu.HasWon(currentGameState['board']))
            print("\n the final board", currentGameState['board'])
            currentGameState = {'board': [" ", " ", " ", " ", " ", " ", " ", " ", " "], 'nextPlayer': "X",
                                'value': None}
            mcts.CurrentGameNode = mcts.root
            data = connection("chess")
            deleteTree(data)
            updateTreesearch(data, mcts.root)





main= main()


tictac = TicTacToe()
main.tictacTraining(5)




'''
# jeu chess

jeu = chessGame()
main.chessTraining(10)
'''




