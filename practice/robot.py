# THIS IS OUR PRACTICE PROJECT TO SPIN A MOTOR!!!!!!!!

import robotpy, wpilib, wpilib.drive, rev
import math, time


class MyRobot(wpilib.TimedRobot):
    motorID = 1
    brushless = rev.CANSparkMaxLowLevel.MotorType.kBrushless

    
    def robotInit(self):
        self.motor = rev.CANSparkMax(self.motorID, self.brushless) 

    def disabledInit(self):
        self.motor.set(0)

    def testPeriodic(self):
        self.motor.set(1)
        


