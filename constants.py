import wpimath.units

# Drivetrain
RIGHT_FRONT_ID = 1
RIGHT_BACK_ID = 2
LEFT_FRONT_ID = 3
LEFT_BACK_ID = 4
RIGHT_ENCODER_A = 3
RIGHT_ENCODER_B = 4
LEFT_ENCODER_A = 5
LEFT_ENCODER_B = 6
INITIAL_POSE = (0, 0, 0)
PID_ANGULAR_DRIVETRAIN = (0.02, 0.01, 0)
PID_LINEAR_DRIVETRAIN = (0.02, 0.01, 0)

# Algae Intake
INTAKE_MOTION_ID = 50
INTAKE_ROTATION_ID = 52
PID_INTAKE = (0.02, 0.01, 0)
LIMIT_SWITCH_START_INTAKE_PORT = 0
LIMIT_SWITCH_END_INTAKE_PORT = 1

# Climber
CLIMBER_ID = 12

# Coral Intake
CORAL_INTAKE_ID = 9

# Joysticks
DUALSHOCK4_ID = 0
DUALSHOCK4_2_ID = 1

# Strings
SENDABLE_CHOOSER_STEERING_WHEEL_OPTION = "Volante"
SENDABLE_CHOOSER_TWO_JOYSTICKS_OPTION = "Dois Controles"

# PixyCam
BAUD_RATE = 9600

# Photonvision (using meters and radians)
PHOTONVISION_CAMERA_NAME = "Camera7459"
CAMERA_HEIGHT_METERS = wpimath.units.inchesToMeters(24)
TARGET_HEIGHT_METERS = wpimath.units.feetToMeters(5)
CAMERA_PITCH_RADIANS = wpimath.units.degreesToRadians(0)

# Field measurements
L1_DISTANCE = 2
