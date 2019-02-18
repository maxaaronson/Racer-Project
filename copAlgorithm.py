# Cop Algorithm
#
# Analysis:
#   - This module determines if the the player gets arrested.
#   - It returns a randomly generated speed set based on actual cop car performance.

# Design:
import random

# Define Constants:
SPEED_CONSTANT = 2.5
COP_CONSTANT = random.randint(3,10)

# Define Cop Speed: 
def copCatch():
    topSpeed = random.randint(130,150)
    acceleration = random.uniform(2.8,3.61)
    copCatch1 = SPEED_CONSTANT*acceleration**2
    copCatch2 = SPEED_CONSTANT*acceleration + SPEED_CONSTANT*3*acceleration**2
    copCatch3 = SPEED_CONSTANT*2*acceleration + SPEED_CONSTANT*4*acceleration**2
    copCatch4 = SPEED_CONSTANT*3*acceleration + SPEED_CONSTANT*5*acceleration**2
    copCatch = copCatch1+copCatch2+copCatch3+copCatch4
    return copCatch/COP_CONSTANT

# Defines if racer escapes:
def copEscape():
    return 10*random.randint(0,9)

# Defines if Cop Deploys spike strip:
def spikeStrip():
    return random.uniform(0,5)
    
