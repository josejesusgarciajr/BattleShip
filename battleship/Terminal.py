'''
Created on Mar 22, 2019
@author: jginvincible
'''

from Player import Player

jose = Player("Jose", True, 0)
leslie = Player("Leslie", False, 0)

while (True):
    if jose.status == True:
        x = input("What Column " + jose.name + "?") - 1
        y = input("What Row " + jose.name + "?") - 1
        leslie.attackIncoming(x, y)  # fire at enemy
        jose.status = False
        leslie.status = True
        print("This is leslie's map after Jose attacked: ------")
        leslie.printMap()
    else:
        x = input("What Column " + leslie.name + "?") - 1
        y = input("What Row " + leslie.name + "?") - 1
        jose.attackIncoming(x, y)  # fire at enemy
        leslie.status = False
        jose.status = True
        print("This is Jose's map after Jose attacked: ------")
        jose.printMap()


