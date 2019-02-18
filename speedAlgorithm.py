import random
import speedGenerator
import copAlgorithm
import distanceTimeCalculator

class SpeedAlgorithm:
    def __init__(self,horsepower,acceleration,topSpeed,torque,RPM,crashFactor):
        self.__horsepower = horsepower
        self.__acceleration = acceleration
        self.__topSpeed = topSpeed
        self.__torque = torque
        self.__RPM = RPM
        self.__crashFactor = crashFactor
        
#________________________________________________________________________________________________#
# Speed Generators
    
    def getSpeed1(self,horsepower,RPM,torque):
        speed1 = 0 
        for number in range(10):
            speed1 += speedGenerator.speed1(self.__torque,self.__RPM,self.__horsepower)
        return speed1
    
    def getSpeed2(self,horsepower,RPM,torque):
        speed2 = 0 
        for number in range(10):
            speed2 += speedGenerator.speed2(self.__torque,self.__RPM,self.__horsepower)
        return speed2
    
    def getSpeed3(self,horsepower,RPM,torque):
        speed3 = 0 
        for number in range(10):
            speed3 += speedGenerator.speed3(self.__torque,self.__RPM,self.__horsepower)
        return speed3
    
    def getSpeed4(self,horsepower,RPM,torque):
        speed4 = 0 
        for number in range(10):
            speed4 += speedGenerator.speed4(self.__torque,self.__RPM,self.__horsepower)
        return speed4
    
    def getSpeed5(self,horsepower,RPM,torque):
        speed5 = 0 
        for number in range(10):
            speed5 += speedGenerator.speed5(self.__torque,self.__RPM,self.__horsepower)
        return speed5
    
    def getTopSpeed(self):
        return self.__topSpeed
            
#________________________________________________________________________________________________#
# Average Speed For Each Gear

    def getAvg1(self,speed1):
        avg1 = speedGenerator.avg1(speed1)
        return avg1

    def getAvg2(self,speed2):
        avg2 = speedGenerator.avg2(speed2)
        return avg2

    def getAvg3(self,speed3):
        avg3 = speedGenerator.avg3(speed3)
        return avg3

    def getAvg4(self,speed4):
        avg4 = speedGenerator.avg4(speed4)
        return avg4

    def getAvg5(self,speed5):
        avg5 = speedGenerator.avg5(speed5)
        return avg5

#________________________________________________________________________________________________#
# Time Calculators

    def getTime1(self,avg1,acceleration):
        time1 = distanceTimeCalculator.time1(avg1,acceleration)
        return time1

    def getTime2(self,avg2,acceleration):
        time2 = distanceTimeCalculator.time2(avg2,acceleration)
        return time2

    def getTime3(self,avg3,acceleration):
        time3 = distanceTimeCalculator.time3(avg3,acceleration)
        return time3

    def getTime4(self,avg4,acceleration):
        time4 = distanceTimeCalculator.time4(avg4,acceleration)
        return time4
        
    def getTime5(self,avg5,acceleration):
        time5 = distanceTimeCalculator.time5(avg5,acceleration)
        return time5

    def getTotalTime(time1,time2,time3,time4,time5):
        totalTime = distanceTimeCalculator.totalTime(time1,time2,time3,time4,time5)
        return totalTime

#________________________________________________________________________________________________#
# Distance Calculators

    def getDist1(self,acceleration,time1):
        dist1 = distanceTimeCalculator.dist1(self.__acceleration,time1)
        return dist1

    def getDist2(self,acceleration,time2,avg2):
        dist2 = distanceTimeCalculator.dist2(self.__acceleration,time2,avg2)
        return dist2

    def getDist3(self,acceleration,time3,avg3):
        dist3 = distanceTimeCalculator.dist3(self.__acceleration,time3,avg3)
        return dist3

    def getDist4(self,acceleration,time4,avg4):
        dist4 = distanceTimeCalculator.dist4(self.__acceleration,time4,avg4)
        return dist4

    def getDist5(self,acceleration,time5,avg5):
        dist5 = distanceTimeCalculator.dist5(self.__acceleration,time5,avg5)
        return dist5

#________________________________________________________________________________________________#
# 

    def copCatch(self):
        copCatch = copAlgorithm.copCatch()
        copEscape = copAlgorithm.copEscape()
        spikeStrip = copAlgorithm.spikeStrip()

        if copCatch > 85:
            if copEscape < 15:
                copSuccessful = 1
            elif spikeStrip > 4:
                copSuccessful = 1
            else:
                copSuccessful = 0
        else:
            copSuccessful = 0 

        return copSuccessful

    
    def getCrash(self,crashFactor):
        damage = random.uniform(0,10)
        crashProbability = random.uniform(-2,2)*crashFactor
        
        if damage >= 5:
            carStatus = 0
        else:
            carStatus = 1
        return carStatus
        

    def getMoney(self,crashFactor,bet):
        money = random.uniform(0,1)*crashFactor*int(bet)
        return money
        
    
   
