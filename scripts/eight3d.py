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
    
    alp,beta,phi = np.pi*20/180,np.pi*10/180,np.pi*10/180
    Rx = np.array([[1,0,0],[0,np.cos(alp),-np.sin(alp)],[0,np.sin(alp),np.cos(alp)]])
    Ry = np.array([[np.cos(beta),0,np.sin(beta)],[0,1,0],[-np.sin(beta),0,np.cos(beta)]])
    Rz = np.array([[np.cos(phi),-np.sin(phi),0],[np.sin(phi),np.cos(phi),0],[0,0,1]])
    R_bs = Rx.dot(Ry).dot(Rz).T
    cf.takeoff(targetHeight = 1.0, duration = 6.0)
    time.sleep(6.0)

    # FILL IN YOUR CODE HERE
    # Please try both goTo and cmdPosition
    r,num=0.4,72
    theta = np.array(range(num-1)).astype(float)*2*np.pi/num
    org = np.array([0,1.5,1])
    #R_bs = np.array([[0.933,0.3491,-0.0871],[-0.25,0.803,0.541],[0.2588,-0.483,0.8365]])
    for th in theta:
        augm = np.array([r-r*np.cos(th),0,r*np.sin(th)]).reshape(3,1)
        goal = org + R_bs.dot(augm).reshape(3)
        #print(goal)
        cf.cmdPosition(list(np.round(goal,3)),yaw=0)
        time.sleep(0.1)
    cf.cmdPosition(org,yaw=0)
    time.sleep(0.1)
    for th in theta:
        augm = np.array([r*np.cos(th)-r,0,r*np.sin(th)]).reshape(3,1)
        goal = org + R_bs.dot(augm).reshape(3)
        #print(goal)
        cf.cmdPosition(list(np.round(goal,3)),yaw=0)
        time.sleep(0.1)
    cf.cmdPosition(org,yaw=0)
    time.sleep(3.0)
    cf.land(targetHeight = 0.0, duration = 5.0)
    time.sleep(5.0)
