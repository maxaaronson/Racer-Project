import sqlite3

class readCarDatabase:
    
    def __init__(self,carName):
        self.__connection = sqlite3.connect('car')
        self.__cursor = self.__connection.cursor()
        self.__carName = carName
    
    def getHorsepower(self,carName):
        Car = self.__cursor.execute('Select horsepower from car where carName = ?',(carName,))
        horsepower = self.__cursor.fetchall()
        horsepower = str(horsepower[-1])
        horsepower = int(horsepower[1:-2])
        return horsepower


    def getAcceleration(self,carName):
        Car = self.__cursor.execute('Select acceleration from car where carName = ?',(carName,))
        acceleration = self.__cursor.fetchall()
        acceleration = str(acceleration[-1])
        acceleration = float(acceleration[1:-2])
        return acceleration

    def getTopSpeed(self,carName):
        Car = self.__cursor.execute('Select topSpeed from car where carName = ?',(carName,))
        topSpeed = self.__cursor.fetchall()
        topSpeed = str(topSpeed[-1])                    
        topSpeed = int(topSpeed[1:-2])
        return topSpeed

    def getTorque(self,carName):
        Car = self.__cursor.execute('Select torque from car where carName = ?',(carName,))
        torque = self.__cursor.fetchall()
        torque = str(torque[0])
        torque = int(torque[1:-2])
        return torque

    def getRPM(self,carName):
        Car = self.__cursor.execute('Select RPM from car where carName = ?',(carName,))
        RPM = self.__cursor.fetchall()
        RPM = str(RPM[-1])
        RPM = int(RPM[1:-2])
        return RPM

    def getCost(self,carName):
        Car = self.__cursor.execute('Select cost from car where carName = ?',(carName,))
        cost = self.__cursor.fetchall()
        cost = str(cost[-1])
        cost = int(cost[1:-2])
        return cost

    def getCrashFactor(self,carName):
        Car = self.__cursor.execute('Select crashFactor from car where carName = ?',(carName,))
        crashFactor = self.__cursor.fetchall()
        crashFactor = str(crashFactor[-1])
        crashFactor = float(crashFactor[1:-2])
        return crashFactor
    
