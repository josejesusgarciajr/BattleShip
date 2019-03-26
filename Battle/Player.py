'''
Created on Mar 22, 2019

@author: jginvincible
'''

from Ship import Ship

class Player:
    def __init__(self, name, status, wins):
        self.name = name        # Every player has a NAME
        self.status = status  # STATUS is a boolean (True if its players Turn, False if enemys turn)
        self.wins = wins    # Number of wins player has
        self.grid = self.makeMap()      # Makes empty grid
        self.ships = [] # List of SHIPS
    
    def makeMap(self):  ## generates a 9 by 8 matrix as the grid
        return [['#' for x in range(10)] for y in range(10)]
    
    def step(self, x, i, y, j):     # Step returns a Tuple: (Start, Stop, how many to move)
        if x == i:      # if x == i, then we know the ship is VERTICAL
            if y < j:       
                return (y, j, 1) 
            return (y, j, -1)
        if x < i:   # since x != i, we know the ship is HORIZONTAL
            return (x, i, 1)        
        return (x, i, -1)
    
    def placeShip(self, idd, x, i, y, j): # Assume that x and y are valid
        
        ship = Ship(idd, x, i, y, j)   # create ship
        
        self.ships.append(ship)     # adds ship to ship list
                               
        (start, stop, jump) = self.step(x, i, y, j)
        for v in range(start - 1, stop, jump):  # Adds ship to the Grid
            if x == i:
                self.grid[v][x] = "s"
            else:
                self.grid[y][v] = "s"
        
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