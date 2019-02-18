#DistanceTimeCalculator
import random
TIME_CONSTANT = 60.0
#______________________________________________________________________________#
# Time Calculations

def time1(avg1,acceleration):
    return(avg1/TIME_CONSTANT)*acceleration

def time2(avg2,acceleration):
    return((avg2+(random.randint(0,10)))/TIME_CONSTANT)*acceleration

def time3(avg3,acceleration):
    return((avg3+(random.randint(2,10)))/TIME_CONSTANT)*acceleration

def time4(avg4,acceleration):
    return((avg4+(random.randint(4,10)))/TIME_CONSTANT)*acceleration

def time5(avg5,acceleration):
    return((avg5+(random.randint(6,10)))/TIME_CONSTANT)*acceleration

def totalTime(time1,time2,time3,time4,time5):
    return time1+time2+time3+time4+time5

#______________________________________________________________________________#
# Distance Calculations

def dist1(acceleration,time1):
    return (.5)*acceleration*time1**2

def dist2(acceleration,time2,avg2):
    return avg2*time2 + (.5*acceleration*time2**2)

def dist3(acceleration,time3,avg3):
    return avg3*time3 + (.5*acceleration*time3**2)

def dist4(acceleration,time4,avg4):
    return avg4*time4 + (.5*acceleration*time4**2)

def dist5(acceleration,time5,avg5):
    return avg5*time5 + (.5*acceleration*time5**2)



