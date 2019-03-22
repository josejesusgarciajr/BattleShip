'''
Created on Mar 22, 2019

@author: jginvincible
'''

from Ship import Ship

class Player:
    def __init__(self, name, status, wins):
        self.name = name
        self. status = status
        self.wins = wins
        self.grid = self.makeMap()
        self.ships = [Ship("Aircraft Carrier", 5),
                      Ship("Battleship", 4),
                      Ship("Submarine", 3),
                      Ship("Cruiser", 3),
                      Ship("Destroyer", 2)]
        self.placeShips()
    
    def makeMap(self):  ## generates a 9 by 8 matrix as the grid
        return [['#' for x in range(9)] for y in range(8)]
    
    def placeShips(self):
        for ship in self.ships:
            print("Implement this methon Brandon A.")
    
    def validCoordinates(self, x , y):      # checks whether or not coordinates are valid
        print("X: " + str(x))
        print("Y: " + str(y))
        if x >= 0 and x <= 8 and y >= 0 and y <= 7:
            return True
        return False
    
    def attackIncoming(self, x , y):    # Attacks Enemy
        if self.validCoordinates(x, y):   #confirms that coordinates are valid
            print("coordinates are valid")
            if self.grid[y][x] == "s":      # s means ship, (HIT)
                self.grid[y][x] = "*"
                return True
            if self.grid[y][x] == "#":      # '#' means empty (MISS)
                print(self.grid[y][x])     
                self.grid[y][x] ="m"
                print("MISSED")
                print(self.grid[y][x])
                return False
            if self.grid[y][x] == "*":      # * means alread been hit (DISAPPOINTMENT)
                return False
        else:
            while not self.validCoordinates(x, y):      # LOOP UNTIL VALID COORDINATES ARE ENTERED
                print("invalid coordinates (Column range 1 - 9), (Row range 1 - 8)")
                x = input("What column?") - 1
                y = input("What Row") - 1
                if self.validCoordinates(x, y):
                    if self.grid[y][x] == "s":      # s means ship, (HIT)
                        self.grid[y][x] = "*"
                        return True
                    if self.grid[y][x] == "#":      # '#' means empty (MISS)
                        self.grid[y][x] = "m"
                        return False
                    if self.grid[y][x] == "*":      # * means alread been hit (DISAPPOINTMENT)
                        return False

    def printMap(self):
        for row in self.grid:
            print(row)