import random
import createRacer
import speedAlgorithm
import readCarDatabase





randomCarList = ["Alfa Romeo 8C","BMW 525d","Bugatti Veyron","Cadillac CTS Coupe","Camaro SS",
                 "Ferrari F430","Mazda RX-8","Nissan Sentra","Shelby GT500","Subaru Outback",
                 "Suzuki Hayabusa","Toyota Camry"]

class Race:
    def __init__(self,carName,bet):
        self.__carName = carName
        self.__bet = bet

    def getRacer1(self,carName):
        racerList1 = []
        car = readCarDatabase.readCarDatabase(carName)
        horsepower = car.getHorsepower(carName)
        acceleration = car.getAcceleration(carName)
        topSpeed = car.getTopSpeed(carName)
        torque = car.getTorque(carName)
        RPM = car.getRPM(carName)
        crashFactor = car.getCrashFactor(carName)
        racer1 = createRacer.createRacer(horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racer1.getGearList1(racerList1,horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racer1.getGearList2(racerList1,horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racer1.getGearList3(racerList1,horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racer1.getGearList4(racerList1,horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racer1.getGearList5(racerList1,horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racerList1.sort()
        return racerList1
    

    def getRacer2(self,carName):
        racerList2 = []
        car = readCarDatabase.readCarDatabase(carName)
        horsepower = car.getHorsepower(carName)
        acceleration = car.getAcceleration(carName)
        topSpeed = car.getTopSpeed(carName)
        torque = car.getTorque(carName)
        RPM = car.getRPM(carName)
        crashFactor = car.getCrashFactor(carName)
        racer2 = createRacer.createRacer(horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racer2.getGearList1(racerList2,horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racer2.getGearList2(racerList2,horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racer2.getGearList3(racerList2,horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racer2.getGearList4(racerList2,horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racer2.getGearList5(racerList2,horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racerList2.sort()
        return racerList2

    def getRacer3(self,carName):
        racerList3 = []
        car = readCarDatabase.readCarDatabase(carName)
        horsepower = car.getHorsepower(carName)
        acceleration = car.getAcceleration(carName)
        topSpeed = car.getTopSpeed(carName)
        torque = car.getTorque(carName)
        RPM = car.getRPM(carName)
        crashFactor = car.getCrashFactor(carName)
        racer3 = createRacer.createRacer(horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racer3.getGearList1(racerList3,horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racer3.getGearList2(racerList3,horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racer3.getGearList3(racerList3,horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racer3.getGearList4(racerList3,horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racer3.getGearList5(racerList3,horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racerList3.sort()
        return racerList3


    def getRacer4(self,carName):
        racerList4 = []
        car = readCarDatabase.readCarDatabase(carName)
        horsepower = car.getHorsepower(carName)
        acceleration = car.getAcceleration(carName)
        topSpeed = car.getTopSpeed(carName)
        torque = car.getTorque(carName)
        RPM = car.getRPM(carName)
        crashFactor = car.getCrashFactor(carName)
        racer4 = createRacer.createRacer(horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racer4.getGearList1(racerList4,horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racer4.getGearList2(racerList4,horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racer4.getGearList3(racerList4,horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racer4.getGearList4(racerList4,horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racer4.getGearList5(racerList4,horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racerList4.sort()
        return racerList4
        
    def getRacerWinner(self,racerList1,racerList2,racerList3,racerList4):
        number = 0
        racerNumber1 = 0
        racerNumber2 = 0
        racerNumber3 = 0
        racerNumber4 = 0
        for num in range(50):
            racerOne = racerList1[number]
            racerTwo = racerList2[number]
            racerThree = racerList3[number]
            racerFour = racerList4[number]
            if racerOne > racerTwo and racerOne > racerThree and racerOne > racerFour:
                racerNumber1 += 5
            elif racerTwo > racerOne and racerTwo > racerThree and racerTwo > racerFour:
                racerNumber2 += 1
            elif racerThree > racerOne and racerThree > racerTwo and racerThree > racerFour:
                racerNumber3 += 1
            elif racerFour > racerOne and racerFour > racerTwo and racerFour > racerThree:
                racerNumber4 += 1
            number+=1
        
        racer = 0
         
        if racerNumber1 > max(racerNumber2,racerNumber3, racerNumber4):
            racer = 1
        elif racerNumber2 > max(racerNumber1,racerNumber3,racerNumber4):
            racer = 2
        elif racerNumber3 > max(racerNumber1,racerNumber2,racerNumber4):
            racer = 3
        elif racerNumber4 > max(racerNumber1,racerNumber2,racerNumber3):
            racer = 4

        if racerNumber1 > min(racerNumber2,racerNumber3, racerNumber4) and racer < 1:
            racer = -1
        elif racerNumber2 > min(racerNumber1,racerNumber3,racerNumber4)and racer < 2:
            racer = -2
        elif racerNumber3 > min(racerNumber1,racerNumber2,racerNumber4)and racer < 3:
            racer = -3
        elif racerNumber4 > min(racerNumber1,racerNumber2,racerNumber3)and racer < 4:
            racer = -4
        return racer
        
    def moneyEarned(self,carName,bet):
        car = readCarDatabase.readCarDatabase(carName)
        horsepower = car.getHorsepower(carName)
        acceleration = car.getAcceleration(carName)
        topSpeed = car.getTopSpeed(carName)
        torque = car.getTorque(carName)
        RPM = car.getRPM(carName)
        racerMoney = 0
        crashFactor = car.getCrashFactor(carName)
        algorithm = speedAlgorithm.SpeedAlgorithm(horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
        racerMoney = algorithm.getMoney(crashFactor,bet)
        # moneyBook = open("MoneyFile.txt","a")
        # moneyBook.write(str(int(racerMoney))+"\n")
        # moneyBook = open("MoneyFile.txt","r")
        # line = moneyBook.readline()
        # total = 0
        # while line !="":
        #     total+=float(line)
        #     line = moneyBook.readline()
        # moneyBook.close()
        return racerMoney
   
    
    
        


