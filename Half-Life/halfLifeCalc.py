# Paul Lim 02/27/2023
# This script will be a half life calculator

import math

# This function will calculate the half life of a radioactive isotope by taking three paramerters as input
def halfLifeCalc(intActivity, halfLife, time):

    Lambda = math.log(2) / halfLife
    activity = intActivity * math.exp(-Lambda * time)
    return activity

