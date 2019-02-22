# !/usr/bin/python3

# this is the class for the outer interface
from tkinter import *
from tkinter import messagebox
from project_methods import *
import sys 
import createCarDatabase
import readCarDatabase
import createRacer
import copAlgorithm
import Character
import speedAlgorithm
import speedGenerator
import distanceTimeCalculator
import RaceOutcome
import sqlite3
import Race
import random
import pygame

# this is the outer interface as soon as the game starts
class Structure:
    def __init__(self):
        self.main_window= Tk()

        # gives the player 90,000 dollars to start with as a demonstration that the upgrades work
        # in the real game we would give the player 2000$
        self.moneyBook = float(20000.00)
        self.numRaces = 0

        # 1/odds = odds of winning. Decreases as the player gains experience 
        self.odds = 5
        
        # main interface only needs one Frame
        self.top_Frame= Frame(self.main_window, relief="raised", border=2)
        self.bottom_Frame= Frame(self.main_window, relief="raised", border=2)                           

        # top Frame needs four choices:
        #   - instruction
        #   - new game
        #   - credits
        #   - quit

        self.instructions_button= Button(self.top_Frame, \
             text= '               Instructions               ', \
             command= self.show_instructions)
        self.new_game_button= Button(self.top_Frame, \
            text= '               New Game               ', \
            command= self.new_game)
        self.credits_button= Button(self.top_Frame, \
            text= '               Credits               ', \
            command= self.show_credits)
        self.sound_button= Button(self.top_Frame, \
            text= '               Sound (On / Off)               ', \
            command= self.toggleSound)
        self.quit_button= Button(self.top_Frame, \
            text= '               Quit               ', \
            command= self.quit_main)
        # pack the widgets
        self.instructions_button.pack(side = 'left')
        self.new_game_button.pack(side = 'left')
        self.sound_button.pack(side = 'left')
        self.credits_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        self.img = PhotoImage(file = 'data/cars/intro_pic.gif')
        ht = self.img.height()
        wd = self.img.width()
        canvas = Canvas(self.bottom_Frame, height = ht, width = wd)      
        canvas.create_image(0, 0, image = self.img, anchor = NW)

        canvas.pack(side = 'bottom')
        # pack the Frame
        self.top_Frame.pack()
        self.bottom_Frame.pack()

        mainloop()

#--------------------------------------------------------------------------------
# quit button
#--------------------------------------------------------------------------------    
    def quit_main(self):
        self.main_window.destroy()

#--------------------------------------------------------------------------------
# Instuctions Button
#--------------------------------------------------------------------------------
    def show_instructions(self):
        message= 'How To Play:\n\n The first thing you will need to do to be a good racer is to choose a character.\n\n' + \
                 'Each character starts with a different car and the races are randomly generated.\n\n' + \
                 "The races are determined by the car's actual performance, but the fastest car doesn't always win!\n\n" + \
                 'Before every race, You will be able to bet your money. You can wager as much money as you have in your bank account.\n\n' + \
                 'As you gain experience racing, you increase your odds of winning.  Upgrade to every car to win the game!\n\n' + \
                 ''
        messagebox.showinfo('Instruction', message)

#--------------------------------------------------------------------------------
# Called with 'New Game' button
# Shows buttons:
#   - character info
#   - select
#--------------------------------------------------------------------------------
    def new_game(self):
        
        self.newgame_window= Toplevel()

        self.top_Frame= Frame(self.newgame_window)
        self.left_Frame= Frame(self.newgame_window)
        self.right_Frame= Frame(self.newgame_window)
        self.bottom_Frame= Frame(self.newgame_window)

        self.heading= Label(self.top_Frame, text= 'Please select your character!')
        self.heading.pack()

        self.radio_var= IntVar()
        self.radio_var.set(1)
        self.rb1= Radiobutton(self.left_Frame, text= '   Antierre Deboutim', variable= self.radio_var, value= 1,)
        self.rb2= Radiobutton(self.left_Frame, text= '    Jennifer Tompson', variable= self.radio_var, value= 2)
        self.rb3= Radiobutton(self.left_Frame, text= "        Tommy O'Reilly", variable= self.radio_var, value= 3)
        self.rb1.pack()        
        self.rb2.pack()        
        self.rb3.pack()        

        self.antierre= Button(self.right_Frame, text= 'Background Information', command= self.antierre_info)
        self.jennifer= Button(self.right_Frame, text= 'Background Information', command= self.jennifer_info)
        self.tommy= Button(self.right_Frame, text= 'Background Information', command= self.tommy_info)
        self.antierre.pack()
        self.jennifer.pack()
        self.tommy.pack()

        # botton Frame
        self.ok_button= Button(self.bottom_Frame, \
            text= '\n                 SELECT                 \n', \
            command= self.create_character)
        self.ok_button.pack()

        # pack Frames
        self.top_Frame.pack()
        self.bottom_Frame.pack(side= 'bottom')
        self.left_Frame.pack(side= 'left')
        self.right_Frame.pack(side= 'left')

#--------------------------------------------------------------------------------
# Character information window
#--------------------------------------------------------------------------------
    # wrapper function
    def antierre_info(self):
        path = 'data/Characters/Antierre Deboutim/Antierre Deboutim.txt'
        image = 'data/Characters/Antierre Deboutim/Antierre Deboutim.gif'
        self.character_info(path, image)

    # wrapper function
    def jennifer_info(self):
        path = 'data/Characters/Jennifer Tompson/Jennifer Tompson.txt'
        image = 'data/Characters/Jennifer Tompson/Jennifer Tompson.gif'
        self.character_info(path, image)
    
    # wrapper function
    def tommy_info(self):
        path = "data/Characters/Tommy O'Reilly/Tommy O'Reilly.txt"
        image = "data/Characters/Tommy O'Reilly/Tommy O'Reilly.gif"
        self.character_info(path, image)


    def character_info(self, path, image):
        infile= open(path, 'r')
        
        self.info_window= Toplevel()
        self.top_Frame= Frame(self.info_window)
        self.bottom_Frame= Frame(self.info_window)

        self.message= "".join(infile.readlines())
        self.label= Label(self.top_Frame, text= self.message)

        self.img = PhotoImage(file = image)
        ht = self.img.height()
        wd = self.img.width()
        canvas = Canvas(self.bottom_Frame, height = ht, width = wd)      
        canvas.create_image(0, 0, image = self.img, anchor = NW)
        
        canvas.pack()
        self.label.pack()
        self.top_Frame.pack()
        self.bottom_Frame.pack()

#--------------------------------------------------------------------------------
# creates user's choice of character as a character object
#--------------------------------------------------------------------------------
    def create_character(self):
        self.newgame_window.destroy()
        value= self.radio_var.get()
        if value== 1:
            character= 'Antierre Deboutim'
            car = 4
        if value== 2:
            character= 'Jennifer Tompson'
            car = 6
        if value== 3:
            character= "Tommy O'Reilly"
            car = 3

        self.character= character
        self.carNum= car       
        my_car = Character.Character(self.character, self.carNum)
        self.carName = my_car.get_car()
        self.show_stats()

#--------------------------------------------------------------------------------
# Called with 'SELECT' button
# Shows character and current car
# Buttons:
#   - Race
#   - Car Specs
#   - Upgrade
#   - Quit (exits game completely)
#--------------------------------------------------------------------------------
    def show_stats(self):
        connection = sqlite3.connect('car')
        cursor = connection.cursor()
        carName = cursor.execute('Select carName from car where carNum = ?',(1,))
        carName = cursor.fetchall()
        carName = carName[self.carNum]
        carName = str(carName[-1])

        # hide the main window
        self.main_window.withdraw()
        self.ingame_screen= Toplevel()

        self.top_Frame= (self.ingame_screen)
        self.mid_Frame= (self.ingame_screen)
        self.bottom_Frame= (self.ingame_screen)
       
        # top Frame
        self.character_label1= Label(self.top_Frame, text= 'Welcome ' + self.character)
        self.characterVar= StringVar()
        self.character_label2= Label(self.top_Frame, textvariable= self.characterVar)

        
        # mid Frame
        self.img = PhotoImage(file = 'data/cars/' + carName + '.gif')
        ht = self.img.height()
        wd = self.img.width()
        self.ingame_canvas = Canvas(self.ingame_screen, height = ht, width = wd)      
        self.ingame_canvas.create_image(0, 0, image = self.img, anchor = NW)

        self.img2 = PhotoImage(file = 'data/Characters/' + self.character + '/' + self.character + '.gif')
        ht = self.img2.height()
        wd = self.img2.width()
        self.ingame_canvas2 = Canvas(self.ingame_screen, height = ht, width = wd)      
        self.ingame_canvas2.create_image(0, 0, image = self.img2, anchor = NW)

        self.race_button= Button(self.ingame_screen, \
                                 text= '                             \nRace\n                        ', \
                                 command= self.place_bet)
        self.stats_button = Button(self.ingame_screen, \
                                      text= '                    \nCar Specifications\n             ', \
                                      command= self.currentStats)
        self.upgrade_button= Button(self.ingame_screen, \
                                    text=   '                        \nUpgrade!\n                     ', \
                                    command = self.upgrade)
        self.back_button= Button(self.ingame_screen, \
                                 text=      '                        \nQuit\n                             ', \
                                 command= self.ingame_quit)
        self.character_label1.pack()
        self.character_label2.pack()
        self.ingame_canvas2.pack()
        self.ingame_canvas.pack()
        self.race_button.pack(side = 'left')
        self.stats_button.pack(side = 'left')
        self.upgrade_button.pack(side = 'left')
        self.back_button.pack(side = 'left')

#--------------------------------------------------------------------------------
# display the stats of the current car in new window
#--------------------------------------------------------------------------------
    def currentStats(self):
        self.car_window= Toplevel()

        self.top_Frame= Frame(self.car_window)
        self.bottom_Frame= Frame(self.car_window)
        connection = sqlite3.connect('car')
        cursor = connection.cursor()
        carName = cursor.execute('Select carName from car where carNum = ?',(1,))
        carName = cursor.fetchall()
        carName = carName[self.carNum]
        carName = str(carName[-1])
        car = readCarDatabase.readCarDatabase(carName)
        horsepower = car.getHorsepower(carName)
        horsepower_string  = 'Horsepower: ' + str(horsepower)
        acceleration= car.getAcceleration(carName)
        acceleration_string= 'Acceleration (0-60 MPH): ' + str(acceleration) + ' sec'
        topspeed= car.getTopSpeed(carName)
        topspeed_string    = 'Top Speed: ' + str(topspeed) + 'MPH'
        torque= car.getTorque(carName)
        rpm = car.getRPM(carName)
        torque_string      = 'Torque @ '+ str(rpm)+': ' + str(torque) + ' Ft-lbs'
        rpm_string         = 'RPM: ' + str(rpm)
        cost= car.getCost(carName)
        cost_string        = 'Cost: ' + str(cost) + ' Dollars'
        crashFactor= car.getCrashFactor(carName)
        crashFactor_string = 'Crash Factor: ' + str(crashFactor)

        # canvas
        self.carImage = PhotoImage(file = 'data/cars/' + carName + '.gif')
        ht = self.img.height()
        wd = self.img.width()
        self.stats_canvas = Canvas(self.car_window, \
                        height = ht, \
                        width = wd)      
        self.stats_canvas.create_image(0, 0, \
                            image = self.img, \
                            anchor = NW \
                            )
        self.stats_canvas.pack()

        # labels
        self.label1= Label(self.bottom_Frame, text= horsepower_string)
        self.label2= Label(self.bottom_Frame, text= acceleration_string)
        self.label3= Label(self.bottom_Frame, text= topspeed_string)
        self.label4= Label(self.bottom_Frame, text= torque_string)
        self.label5= Label(self.bottom_Frame, text= rpm_string)
        self.label6= Label(self.bottom_Frame, text= cost_string)
        self.label7= Label(self.bottom_Frame, text= crashFactor_string)
        self.label8= Label(self.bottom_Frame, text= carName)
        self.ok_button= Button(self.car_window, text= 'Back', command = self.quit_car)
        
        self.label8.pack()
        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        self.label4.pack()
        self.label5.pack()
        self.label6.pack()
        self.label7.pack()
        
        self.top_Frame.pack()
        self.bottom_Frame.pack()
        self.ok_button.pack()

    def quit_car(self):
        self.car_window.destroy()

#--------------------------------------------------------------------------------
# Place a bet
#--------------------------------------------------------------------------------
    def place_bet(self):
        if self.moneyBook <= 0:
            messagebox.showinfo("GAME OVER.","You ran out of cash!")
            self.bet_window.destroy()
            self.main_window.destroy()    
        else:

            self.bet_window= Toplevel()
            self.label= Label(self.bet_window, text= 'Please enter the amount of money you wish to bet:')
            self.bank= 'You have $' + str("%8.2f" % (self.moneyBook)) + ' Dollars in your bank account.' 
            
            self.label2 = Label(self.bet_window, text= self.bank)
            self.entry= Entry(self.bet_window, width= 30)
            self.ok_button= Button(self.bet_window, text= "   Let's race!    ", command = self.start_race)
            self.ok_button2= Button(self.bet_window, text= '      Return        ', command = self.quit_race)
            self.label.pack()
            self.label2.pack()
            self.entry.pack()
            self.ok_button.pack()
            self.ok_button2.pack()

#------------------------------------------------------------------------
# Start Race:
# this opens a gui for the user to wager part of their money
# validates that the user doesn't bet more than they have
# and shows a message box of how much the user won or lost
#------------------------------------------------------------------------
    def start_race(self):
        print("Wallet balance: " + str("%8.2f" % (self.moneyBook)))
        self.moneyWon = 0
        self.moneyLost = 0
        try: 
            bet = float(self.entry.get())

            if bet > self.moneyBook:
                self.bet_window.destroy()
                messagebox.showinfo('info', "You don't have that much!!")
                self.place_bet()
            else:
                self.numRaces+=1
                print(self.numRaces)
                carNum = 1
                connection = sqlite3.connect('car')
                cursor = connection.cursor()
                car = cursor.execute('Select carName from car where carNum = ?',(carNum,))
                car = cursor.fetchall()
                carName = car[self.carName]
                carName = carName[-1]
                car = readCarDatabase.readCarDatabase(carName)
                horsepower = car.getHorsepower(carName)
                acceleration = car.getAcceleration(carName)
                topSpeed = car.getTopSpeed(carName)
                torque = car.getTorque(carName)
                RPM = car.getRPM(carName)
                crashFactor = car.getCrashFactor(carName)
                racer = speedAlgorithm.SpeedAlgorithm(horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
                copSuccessful = racer.copCatch()
                carStatus = random.uniform(.9,5)
                if carStatus < 1:
                    self.bet_window.destroy()
                    self.repair_window()
                carNum = 1
                connection = sqlite3.connect('car')
                cursor = connection.cursor()
                car = cursor.execute('Select carName from car where carNum = ?',(carNum,))
                car = cursor.fetchall()
                carName = car[self.carName]
                carName = carName[-1]
                racer = RaceOutcome.RaceOutcome(carName,bet)
                
                if self.numRaces == 5:
                    self.odds = 4
                    messagebox.showinfo('Great job!', "Your odds of winning have increased!")

                if self.numRaces == 10:
                    self.odds = 3
                    messagebox.showinfo('Great job!', "Your odds of winning have increased again!")

                result = random.randrange(1,self.odds,1)

                # if the user won
                if result == 1:
                    moneyWon = round(racer.moneyWon(carName,bet,result), 2)
                    print("moneyWon = " + str(moneyWon))
                    moneyWonMsg = 'you have won: ' + str("%8.2f" % moneyWon) + ' Dollars'
                    messagebox.showinfo('Race Results', moneyWonMsg)
                    self.moneyBook+= moneyWon
                    self.bet_window.destroy()
                #if the user lost
                else:
                    moneyLost = round(racer.moneyWon(carName,bet,-1), 2)
                    print("moneyLost = " + str(moneyLost))
                    moneyLostMsg = 'you have lost: ' + str("%8.2f" % moneyLost) + ' Dollars'
                    messagebox.showinfo('Race Results', moneyLostMsg)
                    self.moneyBook-= moneyLost
                    self.bet_window.destroy()
                    result = self.getWinner(carName,bet)

                # if arrested
                if copSuccessful == 1:
                    self.arrested_window= Toplevel()
                    self.img9 = PhotoImage(file = 'arrested.gif')
                    ht = self.img9.height()
                    wd = self.img9.width()
                    canvas9 = Canvas(self.arrested_window, height = ht, width = wd)      
                    canvas9.create_image(0, 0, image = self.img9, anchor = NW)
                    
                    canvas9.pack()
                    self.bail = round(random.randint(125,450), 2)
                    self.label= Label(self.arrested_window, 
                        text= 'You have been arrested. It will cost you ' + str(self.bail) + " Dollars to pay bail")
                    
                    self.ok_button= Button(self.arrested_window, text= 'Pay Bail', command = self.pay_bail)
                    self.ok_button2= Button(self.arrested_window, text= 'Go to Jail', command = self.quit_bail)
                
                    self.label.pack()
                    self.ok_button.pack()
                    self.ok_button2.pack()
        except ValueError:
            self.bet_window.destroy()
            messagebox.showinfo('ERROR', "You must enter a real value.")
#------------------------------------------------------------------------

#----------------------------------------------------------------
    def getWinner(self,carName,bet):

        randomCarList = ["Alfa Romeo 8C","BMW 525d","Bugatti Veyron","Cadillac CTS Coupe","Camaro SS",
                 "Ferrari F430","Mazda RX-8","Nissan Sentra","Shelby GT500","Subaru Outback",
                 "Suzuki Hayabusa","Toyota Camry"]

        racers = Race.Race(carName,bet)
        racerList1 = racers.getRacer1(carName)
        racer2 = randomCarList[random.randint(0,11)]
        racer3 = randomCarList[random.randint(0,11)]
        racer4 = randomCarList[random.randint(0,11)]
        racerList2 = racers.getRacer2(racer2)
        racerList3 = racers.getRacer3(racer3)
        racerList4 = racers.getRacer4(racer4)
        result = racers.getRacerWinner(racerList1,racerList2,racerList3,racerList4)

        if result == 2:
            self.win_window= Toplevel()
            self.img6 = PhotoImage(file = 'data/cars/' + str(racer2) + '.gif')
            ht = self.img6.height()
            wd = self.img6.width()
            canvas5 = Canvas(self.win_window, height = ht, width = wd)      
            canvas5.create_image(0, 0, image = self.img6, anchor = NW)
            
            canvas5.pack()
            self.cost = bet
            self.label= Label(self.win_window, text= 'You have been beaten by a random racer with the ' + str(racer2)) 
            
            self.ok_button= Button(self.win_window, text= 'Ok', command = self.quit_result)
        
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




#------------------------------------------------------------------------
# Upgrade function:
# this allows the user to upgrade their car
# it validates that they have enough money
# and tells the user when they own every car
#------------------------------------------------------------------------
    def upgrade(self):
        try:
            if self.moneyBook > 4000:
                self.carNum+= 1
                self.moneyBook-= 4000
                new_car = Character.Character(self.character, self.carNum)
                self.carName= new_car.get_car()
                messagebox.showinfo('Upgraded', "Car upgraded for $4,000!")
                self.ingame_screen.destroy()
                self.show_stats()
            else:
                self.message= "You don't have enough money, it costs $4,000 to upgrade your car. " + \
                              '\n You only have: ' + str(self.moneyBook)
                              
                messagebox.showinfo('error', self.message)
        except IndexError:
            messagebox.showinfo('Congratulations', 'You have won Project Racer!')
            self.main_window.destroy()

#------------------------------------------------------------------------------
# Money functions
#------------------------------------------------------------------------------                    
    def pay_bail(self):
        self.moneyBook-= self.bail
        self.arrested_window.destroy()

    def quit_bail(self):
        self.arrested_window.destroy()
        repair = "You're in prison and the police have taken your car. GAME OVER."
        messagebox.showinfo('Race Results', repair)
        self.main_window.destroy()

    def repair_window(self):
        self.repair_window= Toplevel()
        self.img6 = PhotoImage(file = 'crashImage.gif')
        ht = self.img6.height()
        wd = self.img6.width()
        canvas5 = Canvas(self.repair_window, height = ht, width = wd)      
        canvas5.create_image(0, 0, image = self.img6, anchor = NW)
        
        canvas5.pack()
        self.repairCost = round(random.randint(400,1000), 2)
        self.label= Label(self.repair_window, text= 'You have damaged your car, it will take $' + 
            str(repairCost) + ' to repair the damages, would you like to pay the damages?') 
        
        self.ok_button= Button(self.repair_window, text= 'Yes', command = self.repair)
        self.ok_button2= Button(self.repair_window, text= 'No', command = self.noRepair)
        self.label.pack()
        self.ok_button.pack()
        self.ok_button2.pack()

    def repair(self):
        self.moneyBook-= self.repairCost
        self.repair_window.destroy()
        

    def noRepair(self):
        repair = "You've lost your car. GAME OVER."
        messagebox.showinfo('Race Results', repair)
        self.main_window.destroy()

#--------------------------------------------------------------------------------
# quit funcitons
#--------------------------------------------------------------------------------
    def ingame_quit(self):
        self.main_window.destroy()        

    def quit_race(self):
        self.bet_window.destroy()

    def quit_result(self):
        self.win_window.destroy()

    def quit_result1(self):
        self.win_window1.destroy()

    def quit_result2(self):
        self.win_window2.destroy()
    
#------------------------------------------------------------------------
# shows credits
#------------------------------------------------------------------------
    def show_credits(self):
        message= 'By Max Aaronson and Mustafa Celebi \n' + \
                 'Song: Kickstart My Heart by Motley Crue \n' + \
                 'All photos used were found by Google image search\n' +\
                 ''
        messagebox.showinfo('info', message)

#------------------------------------------------------------------------
# Toggle music on/off
#------------------------------------------------------------------------
    def toggleSound(s):
        global MUSIC_PLAYING
        if MUSIC_PLAYING == 0:
            pygame.mixer.music.unpause()
            MUSIC_PLAYING = 1
        else:
            pygame.mixer.music.pause()
            MUSIC_PLAYING = 0;

#--------------------------------------------------------------------------------
# End of class definition
#--------------------------------------------------------------------------------

#Play sound through default mixer channel in blocking manner.
#This will load the whole sound into memory before playback
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
sound = pygame.mixer.music.load('data/ingame/kmh.wav')
clock = pygame.time.Clock()
pygame.mixer.music.play()
MUSIC_PLAYING = 1

st= Structure()



