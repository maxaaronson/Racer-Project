
import Race
import readCarDatabase
import random
import tkinter
from tkinter import *
from tkinter import messagebox

class RaceOutcome:
    def __init__(self,carName,bet):
        self.__carName = carName
        self.__bet = bet





    def moneyWon(self,carName,bet,result):
        racers = Race.Race(self.__carName,bet)
        if result == 1:
            money = racers.moneyEarned(carName,bet)*random.uniform(1,2)
        else:
            money = bet
        return float(money)
