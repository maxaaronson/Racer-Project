import speedAlgorithm
import random

# Create Racer Profile
class createRacer():
    
    def __init__(self,horsepower,acceleration,topSpeed,torque,RPM,crashFactor):
        self.__horsepower = horsepower
        self.__acceleration = acceleration
        self.__topSpeed = topSpeed
        self.__torque = torque
        self.__RPM = RPM
        self.__crashFactor = crashFactor

    
    def getGearList1(self,racerList1,horsepower,acceleration,topSpeed,torque,RPM,crashFactor):
        try:
            racer = speedAlgorithm.SpeedAlgorithm(horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
            firstGear = racer.getAvg1(racer.getSpeed1(horsepower,RPM,torque))
            for num in range(10):
                racerList1.append(random.randint(1,int(firstGear)))
            return racerList1
        except ValueError:
            racer = speedAlgorithm.SpeedAlgorithm(horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
            firstGear = racer.getAvg1(racer.getSpeed1(horsepower,RPM,torque))
            for num in range(10):
                racerList1.append(random.randint(1,int(firstGear)))
            return racerList1
            
    def getGearList2(self,racerList1,horsepower,acceleration,topSpeed,torque,RPM,crashFactor):
        try:
            racer = speedAlgorithm.SpeedAlgorithm(horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
            firstGear = racer.getAvg1(racer.getSpeed1(horsepower,RPM,torque))
            secondGear = racer.getAvg2(racer.getSpeed2(horsepower,RPM,torque))
            for num in range(10):
                racerList1.append(random.randint(int(firstGear),int(secondGear)))
        except ValueError:
            racer = speedAlgorithm.SpeedAlgorithm(horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
            firstGear = racer.getAvg1(racer.getSpeed1(horsepower,RPM,torque))
            secondGear = racer.getAvg2(racer.getSpeed2(horsepower,RPM,torque))
            for num in range(10):
                racerList1.append(random.randint(int(firstGear),int(secondGear)))
            
    
    def getGearList3(self,racerList1,horsepower,acceleration,topSpeed,torque,RPM,crashFactor):
        try:
            racer = speedAlgorithm.SpeedAlgorithm(horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
            secondGear = racer.getAvg2(racer.getSpeed2(horsepower,RPM,torque))
            thirdGear = racer.getAvg3(racer.getSpeed3(horsepower,RPM,torque))
            for num in range(10):
                racerList1.append(random.randint(int(secondGear),int(thirdGear)))
        except ValueError:
            racer = speedAlgorithm.SpeedAlgorithm(horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
            secondGear = racer.getAvg2(racer.getSpeed2(horsepower,RPM,torque))
            thirdGear = racer.getAvg3(racer.getSpeed3(horsepower,RPM,torque))
            for num in range(10):
                racerList1.append(random.randint(int(secondGear),int(thirdGear)))
    
    def getGearList4(self,racerList1,horsepower,acceleration,topSpeed,torque,RPM,crashFactor):
        try:
            racer = speedAlgorithm.SpeedAlgorithm(horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
            thirdGear = racer.getAvg3(racer.getSpeed3(horsepower,RPM,torque))
            fourthGear = racer.getAvg4(racer.getSpeed4(horsepower,RPM,torque))
            for num in range(10):
                racerList1.append(random.randint(int(thirdGear),int(fourthGear)))
        except ValueError:
            racer = speedAlgorithm.SpeedAlgorithm(horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
            thirdGear = racer.getAvg3(racer.getSpeed3(horsepower,RPM,torque))
            fourthGear = racer.getAvg4(racer.getSpeed4(horsepower,RPM,torque))
            for num in range(10):
                racerList1.append(random.randint(int(thirdGear),int(fourthGear)))

        except ValueError:
            racer = speedAlgorithm.SpeedAlgorithm(horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
            thirdGear = racer.getAvg3(racer.getSpeed3(horsepower,RPM,torque))
            fourthGear = racer.getAvg4(racer.getSpeed4(horsepower,RPM,torque))
            for num in range(10):
                racerList1.append(random.randint(int(thirdGear),int(fourthGear)))
  
            
    def getGearList5(self,racerList1,horsepower,acceleration,topSpeed,torque,RPM,crashFactor):
        try:
            racer = speedAlgorithm.SpeedAlgorithm(horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
            fourthGear = racer.getAvg4(racer.getSpeed4(horsepower,RPM,torque))
            fifthGear = racer.getAvg5(racer.getSpeed5(horsepower,RPM,torque))
            for num in range(10):
                racerList1.append(random.randint(int(fourthGear),topSpeed))
        except ValueError:
            racer = speedAlgorithm.SpeedAlgorithm(horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
            fourthGear = racer.getAvg4(racer.getSpeed4(horsepower,RPM,torque))
            fifthGear = racer.getAvg5(racer.getSpeed5(horsepower,RPM,torque))
            for num in range(10):
                racerList1.append(random.randint(int(fourthGear),topSpeed))

        except ValueError:
            racer = speedAlgorithm.SpeedAlgorithm(horsepower,acceleration,topSpeed,torque,RPM,crashFactor)
            fourthGear = racer.getAvg4(racer.getSpeed4(horsepower,RPM,torque))
            fifthGear = racer.getAvg5(racer.getSpeed5(horsepower,RPM,torque))
            for num in range(10):
                racerList1.append(random.randint(int(fourthGear),topSpeed))
             
