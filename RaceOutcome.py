randomCarList = ["Alfa Romeo 8C","BMW 525d","Bugatti Veyron","Cadillac CTS Coupe","Camaro SS",
                 "Ferrari F430","Mazda RX-8","Nissan Sentra","Shelby GT500","Subaru Outback",
                 "Suzuki Hayabusa","Toyota Camry"]
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

    def getWinner(self,carName,bet):
        racers = Race.Race(carName,bet)
        racerList1 = racers.getRacer1(carName)
        racer2 = randomCarList[random.randint(0,11)]
        racer3 = randomCarList[random.randint(0,11)]
        racer4 = randomCarList[random.randint(0,11)]
        racerList2 = racers.getRacer2(racer2)
        racerList3 = racers.getRacer3(racer3)
        racerList4 = racers.getRacer4(racer4)
        result = racers.getRacerWinner(racerList1,racerList2,racerList3,racerList4)
        if result == 1:
            print("You Win!")
        elif result == -1:
            print("You Lose!")
        elif result == 2:
            self.win_window= Toplevel()
            self.img6 = PhotoImage(file = 'data/cars/' + str(racer2) + '.gif')
            ht = self.img6.height()
            wd = self.img6.width()
            canvas5 = Canvas(self.win_window, \
                            height = ht, \
                            width = wd)      
            canvas5.create_image(0, 0, \
                                image = self.img6, \
                                anchor = NW \
                                )
            
            canvas5.pack()
            self.cost = bet
            self.label= Label(self.win_window, \
                              text= 'You have been beaten by a random racer with the ' + str(racer2)) 
            
            self.ok_button= Button(self.win_window, \
                                   text= 'Ok', \
                                   command = self.quit_result)
        
            self.label.pack()
            self.ok_button.pack()
        elif result == 3:
            self.win_window1= Toplevel()
            self.img7 = PhotoImage(file = 'data/cars/' + str(racer3) + '.gif')
            ht = self.img7.height()
            wd = self.img7.width()
            canvas7 = Canvas(self.win_window1, \
                            height = ht, \
                            width = wd)      
            canvas7.create_image(0, 0, \
                                image = self.img7, \
                                anchor = NW \
                                )
            
            canvas7.pack()
            self.cost = bet
            self.label= Label(self.win_window1, \
                              text= 'You have been beaten by a random racer with the ' + str(racer3)) 
            
            self.ok_button= Button(self.win_window1, \
                                   text= 'Ok', \
                                   command = self.quit_result1)
        
            self.label.pack()
            self.ok_button.pack()
        elif result == 4:
            self.win_window2= Toplevel()
            self.img8 = PhotoImage(file = 'data/cars/' + str(racer4) + '.gif')
            ht = self.img8.height()
            wd = self.img8.width()
            canvas8 = Canvas(self.win_window2, \
                            height = ht, \
                            width = wd)      
            canvas8.create_image(0, 0, \
                                image = self.img8, \
                                anchor = NW \
                                )
            
            canvas8.pack()

            self.label= Label(self.win_window2, \
                              text= 'You have been beaten by a random racer with the ' + str(racer4)) 
            
            self.ok_button= Button(self.win_window2, \
                                   text= 'Ok', \
                                   command = self.quit_result2)
        
            self.label.pack()
            self.ok_button.pack()
        return result

    def quit_result(self):
        self.win_window.destroy()

    def quit_result1(self):
        self.win_window1.destroy()

    def quit_result2(self):
        self.win_window2.destroy()

    def moneyWon(self,carName,bet,result):
        racers = Race.Race(self.__carName,bet)
        if result == 1:
            car = readCarDatabase.readCarDatabase(carName)
            moneyWon = racers.moneyEarned(carName,bet)*random.uniform(1,2)
        else:
            car = readCarDatabase.readCarDatabase(carName)
            moneyWon = racers.moneyEarned(carName,bet)*-1
        return moneyWon
