from Game import Game


class Tplayer:

    def __init__(self):



        '''
        {'board': [" ", " ", " ", " ", " ", " ", " ", " ", " "], 'nextPlayer' : "X",'value': '1:9'}
        '''


    def Playerinterface(self, game: Game, currentGameState, coup):
        '''
            function that allow the player to make a move
        :param game: to specify the game played
        :param currentGameState:
        :param coup:
        :return: a result of the state played by the player
        '''
        result = game.play(currentGameState, coup)

        return result