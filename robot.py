#import commands2.sysid
import wpilib
import wpilib.drive
import constants
import wpimath.geometry
#import commands2

from climber import Climber
from drivetrain import Drivetrain
from buttons import dualshock4_map, g_xbox_360_map
from algae_intake import AlgaeIntake
from coral_intake import CoralIntake
from wpimath.controller import PIDController
from navx import AHRS

class TestRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.climber = Climber()
        self.drivetrain = Drivetrain()
        self.algae_intake = AlgaeIntake()
        self.coral_intake = CoralIntake()

        self.dualshock4 = wpilib.Joystick(constants.DUALSHOCK4_ID)
        self.dualshock4_2 = wpilib.Joystick(constants.DUALSHOCK4_2_ID)
        
        #routine = commands2.sysid.SysIdRoutine(
            #commands2.sysid.SysIdRoutine.Config(),
            #commands2.sysid.SysIdRoutine.Mechanism(self.voltageDrive, self.logMotors, self),
        #)
        self.led = wpilib.AddressableLED(0)
        self.ledData = [wpilib.AddressableLED.LEDData() for _ in range(60)]
        self.led.setLength(60)
        self.led.setData(self.ledData)
        self.led.start()
        self.rainbowFirstPixelHue = 0

    def rainbow(self):
        for i in range(60):
            hue = (self.rainbowFirstPixelHue + (i * 180 / 60)) % 180
            self.ledData[i].setHSV(int(hue), 255, 128)

        self.rainbowFirstPixelHue += 3
        self.rainbowFirstPixelHue %= 180

    def robotPeriodic(self):
        self.drivetrain.updateData()
        self.rainbow()

    def autonomousInit(self):
        self.drivetrain.safetyMode()
        self.drivetrain.reset()
        self.climber.startMotor()

    def autonomousPeriodic(self):
        #self.drivetrain.followTag(0,0)
        pass

    def teleopInit(self):
        self.drivetrain.safetyMode()
        self.algae_intake.reset_intake()

    def teleopPeriodic(self):
        self.climber.isFinished()

        if self.dualshock4.getRawButton(g_xbox_360_map["a"]):
            self.drivetrain.slowdrive(
                self.dualshock4.getRawAxis(g_xbox_360_map["right-trigger-axis"]),
                self.dualshock4.getRawAxis(g_xbox_360_map["left-trigger-axis"]),
                -self.dualshock4.getRawAxis(g_xbox_360_map["left-x-axis"]) 
            )
        #elif self.dualshock4.getRawButton(g_xbox_360_map["b"]):
            #self.drivetrain.turnToDegrees()
        else:
            self.drivetrain.arcadeDrive(
                self.dualshock4.getRawAxis(g_xbox_360_map["right-trigger-axis"]),
                self.dualshock4.getRawAxis(g_xbox_360_map["left-trigger-axis"]),
                -self.dualshock4.getRawAxis(g_xbox_360_map["left-x-axis"]) 
            )

        if self.dualshock4_2.getPOV() == 0:
            self.climber.climbUp()
        elif self.dualshock4_2.getPOV() == 180:
            self.climber.climbDown()
        else:
            self.climber.idle()
            
        if self.dualshock4_2.getRawAxis(g_xbox_360_map["left-trigger-axis"]) > 0:
            self.algae_intake.intake_expel()
        elif self.dualshock4_2.getRawAxis(g_xbox_360_map["right-trigger-axis"]) > 0: 
            self.algae_intake.intake_absorb()
        else:
            self.algae_intake.deactivate_intake()
        
        if self.dualshock4_2.getRawButton(g_xbox_360_map["lb"]):
            self.coral_intake.enable()
        elif self.dualshock4_2.getRawButton(g_xbox_360_map["rb"]):
            self.coral_intake.invert()
        else:
            self.coral_intake.disable()

        #self.intake.readjust_encoder()
        #wpilib.SmartDashboard.putBoolean("Limit Switch", self.algae_intake.limit_switch.get())

        # Intake control position
        if self.dualshock4_2.getRawButtonPressed(g_xbox_360_map["y"]):
            self.algae_intake.setControlVal(2)
           
        if self.dualshock4_2.getRawButtonPressed(g_xbox_360_map["b"]):
            self.algae_intake.setControlVal(1)
            
        if self.dualshock4_2.getRawButtonPressed(g_xbox_360_map["a"]):
            self.algae_intake.setControlVal(0)

        if self.dualshock4_2.getRawButton(g_xbox_360_map["start"]):
            self.algae_intake.full_min_intake()
        elif self.dualshock4_2.getRawButton(g_xbox_360_map["back"]):
            self.algae_intake.full_max_intake()
        else:
            self.algae_intake.deactivate_intake()
           
        match self.algae_intake.getControlVal():
            case 0:
                self.algae_intake.intake_reset_position()
            case 1:
                self.algae_intake.intake_receiving_position()
            case 2:
                self.algae_intake.intake_removing_position()
