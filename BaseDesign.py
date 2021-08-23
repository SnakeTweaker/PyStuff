'''
Title: Stealth Game Base Designer
Author: CJ Busca (MFSnake)
Date: 11/02/2020
Version: .01
'''
import random

#Introduction--Player inputs their name, and is greeted by the first soldier they will recruit.

SoldierNameList = ['Aaron', 'Chavez', 'Brown', 'White', 'Miller', 'Cicero']
ListSoldierRank = ['PVT.', 'SGT.']

print("Base Construction Python")
Username = input("What is your name, sir?")

print("Hello! " + Username + ", sir!")

FirstSoldierName = random.choice(SoldierNameList)
FirstSoldierRank = random.choice(ListSoldierRank)
print("My name is " + FirstSoldierRank + " " + FirstSoldierName)
print(' ')


#Soldier Assignments

FirstSoldier = FirstSoldierRank+" "+FirstSoldierName
print(FirstSoldier)


#######################DefiningCharacter######################################

class Character:
    def __init__(self, *, default=10, HP=None, lethal=None,
                 stamina=None, nonlethal=None, CQC=None,
                 speed=None, luck=None):
        """Initialize a character. Set attributes to "default" unless
        they are given explicitly.

        """
        self.HP = default if HP is None else HP
        self.lethal = default if lethal is None else lethal
        self.stamina = default if stamina is None else stamina
        self.nonlethal = default if nonlethal is None else nonlethal
        self.CQC = default if CQC is None else CQC
        self.speed = default if speed is None else speed
        self.luck = default if luck is None else luck

#######################DefiningSoldierClass###############################

soldier = Character(HP=50, stamina=50, letShal=2, nonlethal=2, speed=3, CQC=2, luck=0)

print(soldier)

