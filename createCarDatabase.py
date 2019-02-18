import sqlite3

def getCarDatabaseCursor():
    connection = sqlite3.connect('car')
    cursor = connection.cursor()
    return connection, cursor    

def createCarTable():
    connection, cursor = getCarDatabaseCursor()
    cursor.execute('drop table if exists car') 
    cursor.execute('''create table car(
                         carNum integer,
                         carName text,
                         horsepower integer,
                         acceleration float,
                         topSpeed integer,
                         torque integer,
                         RPM integer,
                         cost integer,
                         crashFactor float)'''
                   )
    carList = open("carList.txt","r")
    fileName = carList.readline()
    while fileName !="":
        listB =[]
        fileName = fileName.rstrip("\r\n")
        carBook = open('data/cars/' + fileName,"r")
        carNum = 1

        line = carBook.readline()
        while line !="":
            line = line.rstrip("\r\n")
            listB.append(line[13:])
            line = carBook.readline()

        carName = listB[0]
        horsepower = listB[1]
        acceleration = listB[2]
        topSpeed = listB[3]
        torque = listB[4]
        RPM = listB[5]
        cost = listB[6]
        crashFactor = listB[7]
        carNum = 1
        carBook.close()
        carData = (carNum,carName,horsepower,acceleration,topSpeed,torque,RPM,cost,crashFactor)
        cursor.execute('''insert into car(
                            carNum, carName, horsepower, acceleration, topSpeed, torque, RPM, cost,crashFactor) 
                            values(?,?,?,?,?,?,?,?,?)''', carData
                       )
        carNum += 1
        connection.commit() # needed in order for changes to take effect
        fileName = carList.readline()
    connection.commit() # needed in order for changes to take effect
    connection.close()

createCarTable()
