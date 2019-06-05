#!/usr/bin/env python

import math
import numpy as np
from crazyflieParser import CrazyflieParser

if __name__ == '__main__':

    index = 1   # for cf1
    initialPosition = [0,1.5,0] # x,y,z coordinate for this crazyflie
    cfs = CrazyflieParser(index, initialPosition)
    cf = cfs.crazyflies[0]
    time = cfs.timeHelper

    cf.setParam("commander/enHighLevel", 1)
    cf.setParam("stabilizer/estimator", 2) # Use EKF
    cf.setParam("stabilizer/controller", 2) # Use mellinger controller
    #cf.setParam("ring/effect", 7)

    cf.takeoff(targetHeight = 0.5, duration = 3.0)
    time.sleep(3.0)

    # FILL IN YOUR CODE HERE
    # Please try both goTo and cmdPosition
    cf.goTo([1,1.5,0.5], yaw=0.0, duration=5.0)
    time.sleep(5.0)
    cf.goTo([1,1.5,1], yaw=0.0, duration=3.0)
    time.sleep(3.0)
    cf.goTo([0,1.5,1], yaw=0.0, duration=5.0)
    time.sleep(5.0)
    cf.goTo([0,1.5,0.5], yaw=0.0, duration=5.0)
    time.sleep(5.0)
    cf.land(targetHeight = 0.0, duration = 5.0)
    time.sleep(5.0)
