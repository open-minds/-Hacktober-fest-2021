from copy import deepcopy
from random import random

from keras.models import Sequential
from keras.layers import Dense

from Game import Game
from Node import TNode


def string_hashcode(s):
    h = 0
    for c in s:
        h = (31 * h + ord(c)) & 0xFFFFFFFF
    return ((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000

#hashedGameState = string_hashcode("")  # hashage pour génericité


model = Sequential()
model.add(Dense(100, input_dim=64, activation='sigmoid'))
model.add(Dense(3, activation='sigmoid'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# history = model.fit(X_train, y_train, epochs=100, batch_size=64)




def RolloutTuned(self, game: Game, leaf: TNode):
    state = deepcopy(leaf.currentGameState)
    board = deepcopy(leaf.currentGameState['board'])

    while game.HasWon(board) == None:
        probability = self.ANN(board)
        if probability >= 70:
            return game.HasWon(board)
        else:
            move = random.choice(game.possibleMoves(board))
            Rollout = 1  # pour dire que c'est un rollout
            state = game.play(state, move, Rollout)
            board = deepcopy(state['board'])

    return game.HasWon(board)  # si on atteint pas le seuil