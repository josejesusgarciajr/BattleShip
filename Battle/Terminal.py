'''
Created on Mar 23, 2019

@author: areva
'''

from Battle.Player import Player
from Battle.GameBoard import GameBoard

# create the players
#input("Enter name: ")
player1 = Player("p1",False,0)
player2 = Player("p2",False,0)

#prints info
player1.get_Info()
player2.get_Info()

# size of basic game board
'''
#used for coordinates
letters = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
}
'''

xBoard = 10
yBoard = 10

# creating the game board
game = GameBoard(xBoard, yBoard)
game.get_Map()
# place them
'''
all types of boats
type of boat            size    amount
Destroyer                2        4
Cruiser                  3        3
Submarine                3        2
Battleship               4        2
Aircraft Carrier         5        1
'''
game.placeShips()
game.get_Map()
# attack

# check for game changes

# announce winner


'''
#placing

#attacking checking for game difference
'''
