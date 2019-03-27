'''
Created on Mar 23, 2019

@author: areva
'''


class GameBoard:

        def __init__(self, xBoard, yBoard):
            self.xBoard = xBoard
            self.yBoard = yBoard
            self.grid = self.makeMap()
        
        def makeMap(self):
            return  [['#' for x in range(self.xBoard)] for y in range(self.yBoard)]
        
        def get_Map(self):
            m = ""
            for i in range(self.yBoard):
                 for j in range(self.xBoard):
                    m += self.grid[i][j]+" "
                    #print(i)
                    #print(j)
                    #print(self.xBoard)
                    if j+1 == self.xBoard:
                        m += "\n"
            print(m)
        
        def placeShips(self):
            #place aircraft carrier
            #getting x1 y1 x2 y2 respectively for each boat
            
            #AirCraft Carrier char "5"
            x1 = input("x1: ")
            y1 = input("y1: ")
            pos = input("position: ")
            '''x2 = input("x2: ")
            y2 = input("y2: ")'''
            
            #for size 5
            if self.check(x1,y1,5,pos):
                self.setChar("5",x1,y1)
            
            #print(self.check(x1,y1,x2,y2))
            #print(type(self.grid[0][0]))
        
        #set the char of that bot  
        def setChar(self,cha,x1,y1,x2,y2):
            if x1 == x2:
                tof = False
                for y in range(int(y2)):
                    #print(self.grid[int(x1)][y])
                    self.grid[int(x1)][y]="5"
        
        #check the placement of the boat
        def check(self,x1,y1):
            if self.checkInBound(x1,y1):
                print("in the board")
                '''if x1 == x2:
                    tof = False
                    for y in range(int(y2)):
                        #print(self.grid[int(x1)][y])
                        if self.grid[int(x1)][y] == "#":
                            tof = True
                        else:
                            return False
                return tof
                '''
                
        
        def checkInBound(self,x1,y1,x2,y2):
            tof1 = False
            tof2 = False
            tof3 = False
            tof4 = False
            if int(x1) >= 0 and int(x1) <= 9:
                tof1 = True
            else:
                tof1 = False
            
            if int(y1) >= 0 and int(y1) <= 9:
                tof2 = True
            else:
                tof2 = False
            
            if int(x2) >= 0 and int(x2) <= 9:
                tof3 = True
            else:
                tof3 = False
            
            if int(y2) >= 0 and int(y2) <= 9:
                tof4 = True
            else:
                tof4 = False
        
            return tof1 and tof2 and tof3 and tof4