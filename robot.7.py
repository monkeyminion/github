#import angle
import wpilib
import ctre
from robotpy_ext.common_drivers.navx import ahrs, AHRS
from wpilib.command import CommandGroup, Scheduler

from basic_commands import *  # ADDED


class MyRobot(wpilib.IterativeRobot):
    def robotInit(self):
        self.leftFront = ctre.CANTalon(2)
        self.leftBack = ctre.CANTalon(0)
        self.rightFront = ctre.CANTalon(1)
        self.rightBack = ctre.CANTalon(3)
        self.ahrs = ahrs


    def autonomousInit(self):
        ahrs = AHRS.create_spi()
        #ahrs.getYaw()
        ahrs.getAngle()
        oneGroup = CommandGroup()  # CHANGED (parentheses are needed to create a CommandGroup object)

        # CHANGED:
        oneGroup.addSequential(DriveForwardCommand(
            self.leftFront, self.rightFront, self.leftBack, self.rightBack,
            1.0, 1.0))  # speed, seconds
        oneGroup.addSequential(RotateCommand(self.leftFront,self.leftBack, self.rightFront,self.rightBack,
                                             self.ahrs, math.radians(45)))

        scheduler = Scheduler.getInstance()
        scheduler.add(oneGroup)

    # ADDED (tell the Scheduler to update Commands)
    def autonomousPeriodic(self):
        Scheduler.getInstance().run()


if __name__ == "__main__":
    wpilib.run(MyRobot, physics_enabled=True)
