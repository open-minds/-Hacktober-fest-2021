from graphviz import Digraph
from graphviz import Graph
from graphviz import render
from graphviz import Source
from database import *
import pymongo
from pymongo import MongoClient
import chess
from chessGame import *
from TPlayer import *


class Visualize:

    def __init__(self):
        self.dot = Digraph(comment='MCTS tree search', format='svg')
        self.iteration = 0



    def VisualizeTreetictactoe(self,root: TNode, iteration =0):
        '''
        function that visualize the tree search of tictactoe
        the tree may not be displayable, in case of beign too large for an SVG format

        :param root: the root of the tree
        :param iteration:  the number of iteration in depth
        :return: SVG image
        '''
        if iteration < 3:
            if (root.parent == None):
                self.dot.node(str(root.id), str([" ", " ", " ", " ", " ", " ", " ", " ", " "]))

            if root.children != []:
                for child in root.children:
                    #self.dot.attr(rank='')
                    self.dot.node(str(child.id), label=str(child.currentGameState['board']))
                    self.dot.edge(str(root.id), str(child.id))
                    self.VisualizeTreetictactoe(child, iteration + 1)


    def VisualizeTreetictactoetuned(self,root: TNode, iteration =0):
        '''
        function that diplay a small part of the tree search of tictactoe in order to visualize it in an SVG format
        :param root: root of the tree search
        :param iteration:  the number of iteration in depth
        :return:  an SVG image
        '''
        if iteration < 2:
            if (root.parent == None):
                self.dot.node(str(root.id), str([" ", " ", " ", " ", " ", " ", " ", " ", " "]))

            if root.children != []:
                self.dot.node(str(root.children[0].id), label=str(root.children[0].currentGameState['board']))
                self.dot.edge(str(root.id), str(root.children[0].id))
                self.VisualizeTreetictactoe(root.children[0], iteration + 1)

                self.dot.node(str(root.children[1].id), label=str(root.children[1].currentGameState['board']))
                self.dot.edge(str(root.id), str(root.children[1].id))
                self.VisualizeTreetictactoe(root.children[1], iteration + 1)

                self.dot.node(str(root.children[2].id), label=str(root.children[2].currentGameState['board']))
                self.dot.edge(str(root.id), str(root.children[2].id))
                self.VisualizeTreetictactoe(root.children[2], iteration + 1)




    def VisualizeTreechess(self, root: TNode, iteration = 0):
        '''
                function that visualize the tree search of chess
                the tree may not be displayable, in case of beign too large for an SVG format

                :param root: the root of the tree
                :param iteration:  the number of iteration in depth
                :return: SVG image
                '''
        if iteration <= 3:
            if (root.parent == None):
                self.dot.node(str(root.id), str(chess.Board(root.currentGameState['board'])))

            if root.children != []:
                for child in root.children:
                    self.dot.node(str(child.id), label=str(chess.Board(child.currentGameState['board'])))
                    self.dot.edge(str(root.id), str(child.id))
                    self.VisualizeTreechess(child, iteration + 1)
        else:
            print("stop")


    def VisualizeTreechesstuned(self, root: TNode, iteration = 0):

        '''
               function that diplay a small part of the tree search of chess in order to visualize it in an SVG format
               :param root: root of the tree search
               :param iteration:  the number of iteration in depth
               :return:  an SVG image
               '''
        if iteration <= 2:
            if (root.parent == None):
                self.dot.node(str(root.id), str(chess.Board(root.currentGameState['board'])))

            if root.children != []:
                    self.dot.node(str(root.children[0].id), label=str(chess.Board(root.children[0].currentGameState['board'])))
                    self.dot.edge(str(root.id), str(root.children[0].id))
                    self.VisualizeTreechess(root.children[0], iteration + 1)

                    self.dot.node(str(root.children[1].id),
                                  label=str(chess.Board(root.children[1].currentGameState['board'])))
                    self.dot.edge(str(root.id), str(root.children[1].id))
                    self.VisualizeTreechess(root.children[1], iteration + 1)

                    self.dot.node(str(root.children[5].id),
                                  label=str(chess.Board(root.children[5].currentGameState['board'])))
                    self.dot.edge(str(root.id), str(root.children[5].id))
                    self.VisualizeTreechess(root.children[5], iteration + 1)

        else:
            print("stop")










#########---   Main   ---##########
if __name__ == '__main__':

    # visualizing dot document
    graph = Visualize()
    s = Source.from_file('TreeSearch-output/chess.gv')
    s.view()


    '''# TICTACTOE GRAPH
    root = TNode(parent=None,
                 GameState={'board': [" ", " ", " ", " ", " ", " ", " ", " ", " "], 'nextPlayer': "X", 'value': None},
                 value=None)
    data = connection("tictactoe")
    collection = data['tree']
    getTreesearch(data, root)
    print("tree OK")

    graph= Visualize()
    graph.VisualizeTreetictactoetuned(root, 0)
    graph.dot.graph_attr['rankdir'] = 'TB'

    graph.dot.render('TreeSearch-output/tictactoe.gv', view=True)

'''
    '''# CHESS GRAPH

    root = TNode(parent=None,
                 GameState={'board': "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", 'nextPlayer': "WHITE",
                            'value': None}, value=None)
    data = connection("chess")
    collection = data['tree']
    getTreesearch(data, root)

    print("tree OK")


    graph.VisualizeTreechesstuned(root)
    graph.dot.render('TreeSearch-output/chess.gv', view=True)'''

