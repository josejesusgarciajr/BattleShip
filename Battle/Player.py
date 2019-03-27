'''
Created on Mar 23, 2019

@author: areva
'''


class Player:

        def __init__(self, name, status, wins):
            self.name = name
            self.status = status
            self.wins = wins
        
        def get_Name(self):
            return self.__name
    
        def get_Status(self):
            return self.__status
        
        def get_Wins(self):
            return self.__wins
        
        def set_Name(self,name):
            self.name = name
    
        def set_Status(self,status):
            self.status = status
        
        def set_Wins(self,wins):
            self.wins = wins
        
        def get_Info(self):
            print("Name: " +  str(self.name) + ", status: " + str(self.status) + ", wins: " +  str(self.wins))
