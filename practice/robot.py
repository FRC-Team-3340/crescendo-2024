# THIS IS OUR PRACTICE PROJECT TO SPIN A MOTOR!!!!!!!!

import robotpy, wpilib, wpilib.drive, rev
import math


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        motor = rev.CANSparkMax(0)


        return super().robotInit()


