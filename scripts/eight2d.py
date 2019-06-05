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

    cf.takeoff(targetHeight = 1.0, duration = 6.0)
    time.sleep(6.0)

    # FILL IN YOUR CODE HERE
    # Please try both goTo and cmdPosition
    r,num=0.5,72
    theta = np.array(range(num-1)).astype(float)*2*np.pi/num
    org = np.array([0,1.5,1])
    for th in theta:
        goal = org + np.array([r-r*np.cos(th),0,r*np.sin(th)])
        cf.cmdPosition(list(np.round(goal,3)),yaw=0)
        time.sleep(0.1)
    cf.cmdPosition(org,yaw=0)
    time.sleep(0.1)
    for th in theta:
        goal = org + np.array([r*np.cos(th)-r,0,r*np.sin(th)])
        cf.cmdPosition(list(np.round(goal,3)),yaw=0)
        time.sleep(0.1)
    cf.cmdPosition(org,yaw=0)
    time.sleep(3.0)
    cf.land(targetHeight = 0.0, duration = 5.0)
    time.sleep(5.0)
