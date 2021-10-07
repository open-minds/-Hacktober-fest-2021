from tkinter import *
from tkinter import messagebox
from Node import *
from TicTacToe import *
from TPlayer import *
from MCTS import *
from database import *


tictac = TicTacToe()
currentGameState = {'board': [" ", " ", " ", " ", " ", " ", " ", " ", " "], 'nextPlayer': "X", 'value': None}
player1 = Tplayer()
mcts = Mcts(tictac, 1)
mcts.CurrentGameNode = mcts.initialize(tictac, currentGameState, "tictactoe")  # créer la racine et les fils de la racine

def button(frame):
    '''
    function to define a button
    :param frame:
    :return:
    '''
    b= Button(frame,padx=1,bg="papaya whip",width=3,text="   ",font=('arial',60,'bold'),relief="sunken",bd=10)
    return b


def change_a():
    '''
    Function to change the operand for the next player
    :return:
    '''
    global a
    for i in ['O','X']:
        if not(i==a):
            a=i
            break


def reset():
    '''
    function to reset the game
    :return:
    '''
    mcts.CurrentGameNode = mcts.root
    global currentGameState
    currentGameState = deepcopy(mcts.root.currentGameState)
    #Resets the game
    global a
    for i in range(3):
        for j in range(3):
                b[i][j]["text"] = " "
                b[i][j]["state"] = NORMAL
    a = 'X'



def check(board):
    '''
                    Checks for victory , Draw or lose
    :param board:
    :return:
    '''
    if tictac.HasWon(board) == -1:
        messagebox.showinfo("Congrats!!, X has won")
        data = connection("tictactoe")
        deleteTree(data)
        updateTreesearch(data, mcts.root)
        reset()
    elif tictac.HasWon(board) == 1:
        messagebox.showinfo("Congrats!!, O has won")
        data = connection("tictactoe")
        deleteTree(data)
        updateTreesearch(data, mcts.root)
        reset()
    elif tictac.HasWon(board) == 0:
        messagebox.showinfo(" It's a draw")
        data = connection("tictactoe")
        deleteTree(data)
        updateTreesearch(data, mcts.root)
        reset()





def getBoardIndex(i: int,j: int):
    '''
    function that render the move index from the board matrix  and adapt it to the list index
    :param i:
    :param j:
    :return:
    '''
    coup =0
    if i == 0 and j == 0:
        coup = 1
    elif i == 0 and j == 1:
        coup = 2
    elif i == 0 and j == 2:
        coup = 3
    elif i == 1 and j == 0:
        coup = 4
    elif i == 1 and j == 1:
        coup = 5
    elif i == 1 and j == 2:
        coup = 6
    elif i == 2 and j == 0:
        coup = 7
    elif i == 2 and j == 1:
        coup = 8
    elif i == 2 and j == 2:
        coup = 9
    return coup

def getCoupIndex(coup: int):

    '''
    function that get the move to be played and adapt it to the index of the matrix board
    :param coup:
    :return:
    '''

    i=0
    j=0
    if coup == 1:
        i = 0
        j = 0
        return {'row': i, 'col': j}
    elif coup == 2:
        i =0
        j = 1
        return {'row': i, 'col': j}
    elif coup == 3:
        i = 0
        j = 2
        return {'row': i, 'col': j}
    elif coup == 4:
        i = 1
        j = 0
        return {'row': i, 'col': j}
    elif coup == 5:
        i = 1
        j = 1
        return {'row': i, 'col': j}
    elif coup == 6:
        i = 1
        j = 2
        return {'row': i, 'col': j}
    elif coup == 7:
        i = 2
        j = 0
        return {'row': i, 'col': j}
    elif coup == 8:
        i = 2
        j = 1
        return {'row': i, 'col': j}
    elif coup == 9:
        i = 2
        j = 2
        return {'row': i, 'col': j}

def click(row, col, currentGameState):
        '''
        event of clocking on the borad buttons
        :param row:
        :param col:
        :param currentGameState:
        :return:
        '''
        b[row][col].config(text=a, state=DISABLED, disabledforeground=colour[a])
        coup = getBoardIndex(row, col)

        if (tictac.HasWon(currentGameState['board']) == None):
            # demander au joueur 1 de jouer
            currentGameState = player1.Playerinterface(tictac, currentGameState, coup)
            check(currentGameState['board'])


        if(tictac.HasWon(currentGameState['board']) == None):
            label.config(text="O's Chance")
            currentGameState = mcts.ComputerPlay(tictac, currentGameState, mcts.CurrentGameNode, NBrollout=30, NbIteration=2000, c=2)
            lastMCTSState = deepcopy(currentGameState)
            result = getCoupIndex(currentGameState['value'])
            i = result['row']
            j = result['col']
            b[i][j]['text'] = "O"
            check(currentGameState['board'])
            label.config(text="X's Chance")



#########---   Main   ---##########


root=Tk()                   #Window defined
root.title("Tic-Tac-Toe PFE MASTER 2")   #Title given
a='X'                                         #Two operators defined
colour={'O':"deep sky blue",'X':"lawn green"}
b=[[],[],[]]
for i in range(3):
        for j in range(3):
                b[i].append(button(root))
                b[i][j].config(command= lambda row=i, col=j: click(row, col, currentGameState))
                b[i][j].grid(row=i, column=j)

label=Label(text=a+"'s Chance",font=('arial',20,'bold'))
label.grid(row=3,column=0,columnspan=3)




root.mainloop()

