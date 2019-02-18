#Speed Generator
import random

def speed1(torque,RPM,horsepower):
    return (torque*RPM)/(horsepower*(random.randint(400,500)))
def speed2(torque,RPM,horsepower):
    return (torque*RPM)/(horsepower*(random.randint(300,399)))

def speed3(torque,RPM,horsepower):
    return (torque*RPM)/(horsepower*(random.randint(200,299)))

def speed4(torque,RPM,horsepower):
    return (torque*RPM)/(horsepower*(random.randint(190,199)))

def speed5(torque,RPM,horsepower):
    return (torque*RPM)/(horsepower*(random.randint(25,100)))

#_____________________________________________________________________________________#
# Accumulators:
total1 = 0.0
total2 = 0.0
total3 = 0.0
total4 = 0.0
total5 = 0.0

#_____________________________________________________________________________________#
# Summation of 10 random Speeds

def total1(speed1,total1):
    total1+=speed1
    return total1

def total2(speed2,total2):
    total2+=speed2
    return total2

def total3(speed3,total3):
    total3+=speed3
    return total3

def total4(speed4,total4):
    total4+=speed4
    return total4

def total5(speed5,total5):
    total5+=speed5
    return total5

#______________________________________________________________________________#
# Average of each summation

def avg1(total1):
    return (total1/10)

def avg2(total2):
    return (total2/10)

def avg3(total3):
    return (total3/10)

def avg4(total4):
    return (total4/10)

def avg5(total5):
    return (total5/10)

