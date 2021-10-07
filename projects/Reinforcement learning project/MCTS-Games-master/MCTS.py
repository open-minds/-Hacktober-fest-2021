from copy import deepcopy
import math
import random
import pymongo
from pymongo import MongoClient
from Node import *
from TicTacToe import *
from database import *
        
class Mcts:

    LeafList = []       #global var
    
    def __init__(self, game, number_rollout):
        self.game = game
        self.NbrParties = 0
        self.Score = 0
        self.root = None         # pour l'instant a revoir
        self.runtime = 0
        self.rolloutDone = 0
        self.Number_Rollout = number_rollout
        self.PreviousGameNode = None
        self.CurrentGameNode = None

        '''
        GameState : {Board: ["X", "O", "X",
                      " ", "O", "O",
                      " ", " ", " "],
             Player: "O"
        }
        '''


    def initialize(self, game:Game, currentGameState, database):
        # creer la racine
        '''
        function to initialize the game at it beggining
        :param game:
        :param currentGameState:
        :param database:
        :return: the root of the tree search
        '''
        data = connection(database)
        collection = data['tree']
        NbrDocument= collection.find().count()
        if data != False and NbrDocument > 0:                   # si la base de donnée reponds
            root = getRoot(data)
            getTreesearch(data, root)
            self.root = root
            self.NbrParties = root.Visits
            self.Score = root.Score
            self.CurrentGameNode = root
            return self.CurrentGameNode

        else:                               # si la base de donnée ne reponds pas
            board = deepcopy(currentGameState['board'])
            root = TNode(None, board, None)
            root.currentGameState = deepcopy(currentGameState)
            self.root = root
            # Ajoute les premiers fils
            self.root.add_children(game, currentGameState)
            self.CurrentGameNode = root
            return self.CurrentGameNode





    def selectMove(self,actualNode: TNode):
        '''
        function that selects the next move of the computer, through the maximum number of visits
        :param actualNode: the actual game node
        :return: the max node
        '''
        NbrVisites = 0
        MaxNode = None
        if actualNode.children != []:
            for node in actualNode.children:
                if NbrVisites <= node.Visits:
                    NbrVisites = deepcopy(node.Visits)
                    MaxNode = node

            return MaxNode
        else:
            print(" exception dans selectMove()")



    def selectMoveTuned(self,actualNode: TNode):
        '''
        select move tuned for self play that select randomly a node from the 3 best moves
        :param actualNode:
        :return:
        '''
        MaxNode = None
        if actualNode.children != []:
            numberValues= len(actualNode.children)
            if numberValues <= 3:
                print("list inferieure a 3")
                MaxNode = random.choice(actualNode.children)
            else:
                print("list superieure a 3")
                sortedList = sorted(actualNode.children, key=lambda x: x.Visits, reverse=True)
                #actualNode.children.sort(key=lambda x: x.Visits, reverse=True)
                bestChilds = sortedList[:3]
                MaxNode = random.choice(bestChilds)

            return MaxNode
        else:
            print(" exception dans selectMove()")



    def Select_Node(self, root: TNode, c):
        '''
            MCTS selection step
        '''
                            # condition si le noeud a un fils is leaf

        if root != None:
            if root.children == []:
                return root
            else:
                UTC = float('-inf')
                MaxNode = None
                for node in root.children:
                    if (self.UCT(node, c) >= UTC):
                        UTC = self.UCT(node, c)
                        MaxNode = node
                return self.Select_Node(MaxNode, c)









    def find_Node(self, node:TNode, valeur):
        '''
        fonction to detect if a node has a children with a given value
        :param node:
        :param valeur:
        :return: the children
        '''
        if(node.children != []):
            for node in node.children:
                if node.currentGameState['value'] == valeur:
                    return node
            print("on es hors de la boucle")
            return node
        else:
            print("find node , node:", node.currentGameState['board'])
            print("find node , node.children:", node.children)
            return node




    def expand_Node(self, game: Game, node: TNode):
        '''
                expension step in MCTS

        '''
        state = deepcopy(node.currentGameState)
        board = deepcopy(node.currentGameState['board'])
        if(node.is_terminal(game, board) == False):
            if node.is_leaf():
                node.add_children(game, state)
        else:
            return None


    def rollout(self, game: Game, leaf: TNode, NumberRollout=1):
        '''
           MCTS rollout step
        :param game: the game played
        :param leaf: the leaf from where begining the rollout
        :param NumberRollout: the number of rollout to be made
        :return: the score of the rollout (s)
        '''
        Scorefinal = 0
        for i in range(NumberRollout):
            state = deepcopy(leaf.currentGameState)
            board = deepcopy(leaf.currentGameState['board'])
            while game.HasWon(board) == None:
                move = random.choice(game.possibleMoves(board))
                Rollout = 1
                state = game.play(state, move, Rollout)
                board = deepcopy(state['board'])
            Scorefinal += game.HasWon(board)
        return Scorefinal


    def UCT(self, node: TNode,c) -> float:
        
        '''
        UCB formula made for MCTS function
        '''
        if node.Visits == 0:
            return float('inf')
        else:
            return (node.Score / node.Visits) + c * (math.sqrt(math.log(self.NbrParties)/node.Visits) )      # 1.41 || 2



    def BackPropagation(self, rolloutnode: TNode, score):
        
        ''' 
        backprobagation MCTS phase
 
        '''

        if rolloutnode.parent == None:
            rolloutnode.Visits += 1
            rolloutnode.Score += score
            self.Score += score
            self.NbrParties += 1
        else:
            rolloutnode.Visits += 1
            rolloutnode.Score += score
            self.BackPropagation(rolloutnode.parent, score)



    def ApplyMCTS(self,game: Game, currentNode: TNode, NbrIterations: int , Nbrollout : int, c ):
        '''
        function that apply MCTS steps
        :param game:
        :param currentNode:
        :param NbrIterations:
        :param Nbrollout:
        :param c:
        :return:
        '''

        iteration = 0
        while iteration < NbrIterations:
            if currentNode.children == []:
                currentNode.add_children(game, currentNode.currentGameState)

            SelectedNode = self.Select_Node(currentNode, c)        # phase de selection
            if SelectedNode.Visits == 0:
                Score = self.rollout(game, SelectedNode, Nbrollout)        # phase de rollout

                self.BackPropagation(SelectedNode, Score)       #phase de backpropagation

            else:
                self.expand_Node(game, SelectedNode)        #phase d'expension
            iteration += 1


    def ComputerPlay(self, game: Game,currentMctsState ,currentNode: TNode, NBrollout:int, NbIteration: int, c):

        '''
        function that allow the computer to play
        :param game:
        :param currentMctsState:
        :param currentNode:
        :param NBrollout:
        :param NbIteration:
        :param c:
        :return:
        '''
             #condition si on es deja dans le noeud dans find node
        self.CurrentGameNode = self.find_Node(currentNode, currentMctsState['value'])
        self.ApplyMCTS(game, self.CurrentGameNode, NbIteration, NBrollout, c)

        ComputerMove = self.selectMove(self.CurrentGameNode)
        currentMctsState = game.play(currentMctsState, ComputerMove.currentGameState['value'])

        self.CurrentGameNode = self.find_Node(self.CurrentGameNode, currentMctsState['value'])

        return currentMctsState

    def ComputerVsComputer(self, game: Game,currentMctsState, NbrIterations=1000,Nbrollout=10,c=1.41 ):
        '''
        function that allows the computer to play in the case of training (self-play)
        :param game:
        :param currentMctsState:
        :param NbrIterations:
        :param Nbrollout:
        :param c:
        :return:
        '''

             #condition si on es deja dans le noeud dans find node


        self.ApplyMCTS(game, self.CurrentGameNode, NbrIterations, Nbrollout, c)

        ComputerMove = self.selectMoveTuned(self.CurrentGameNode)

        currentMctsState = game.play(currentMctsState, ComputerMove.currentGameState['value'])

        self.CurrentGameNode = self.find_Node(self.CurrentGameNode, currentMctsState['value'])

        return currentMctsState
