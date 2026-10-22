from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from MCLab.robocar import Robocar

remoteInit()

# ---------------- SCREEN & HUD SETUP ----------------

screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0x1E1E1E)  # Dark theme for better visibility

# Title Header
title_label = MCLabel(
    'RC COMPETITION HUD',
    x=15, y=10,
    color=0x00FFCC,
    font=FONT_MONT_20,
    parent=None
)

# Live Status Display
status_label = MCLabel(
    'Status: READY',
    x=15, y=50,
    color=0xFFFFFF,
    font=FONT_MONT_14,
    parent=None
)

# Telemetry Display
telemetry_label = MCLabel(
    'Speed: 50% | Arm: 90° | Grip: 90°',
    x=15, y=85,
    color=0xAAAAAA,
    font=FONT_MONT_12,
    parent=None
)

# ---------------- STATE MANAGEMENT ----------------

current_speed_setting = 50  # Master speed multiplier
arm_angle = 90              # Servo 1: Arm lift angle
gripper_angle = 90          # Servo 2: Gripper open/close angle

# ---------------- ROBOT INITIALIZATION ----------------

robo = Robocar()
robo.init_motor_module()

if not robo.select_lego:
    robo.encoder4.set_all_motors_mode(0x00)

def update_hud(status_text):
    """Updates the on-screen dashboard text cleanly."""
    status_label.set_text(f"Status: {status_text}")
    telemetry_label.set_text(f"Speed: {current_speed_setting}% | Arm: {arm_angle}° | Grip: {gripper_angle}°")

# ---------------- MOTOR & DRIVE CONTROL ----------------

def MotorsStopAll():
    robo.motor_stop(1)
    robo.motor_stop(2)
    robo.motor_stop(3)
    robo.motor_stop(4)
    update_hud("STOPPED")

def execute_drive(forward_val, turn_val):
    """Handles arcade/differential drive mixing without limits."""
    speed_mult = current_speed_setting / 100.0
    
    if forward_val > 0:
        power = int(forward_val * speed_mult)
        robo.move_forward(power)
        update_hud(f"Driving Forward ({power}%)")
    elif forward_val < 0:
        power = int(abs(forward_val) * speed_mult)
        robo.move_backward(power)
        update_hud(f"Driving Backward ({power}%)")
    elif turn_val > 0:
        power = int(turn_val * speed_mult)
        robo.move_right(power)
        update_hud(f"Turning Right ({power}%)")
    elif turn_val < 0:
        power = int(abs(turn_val) * speed_mult)
        robo.move_left(power)
        update_hud(f"Turning Left ({power}%)")
    else:
        MotorsStopAll()

# ---------------- JOYSTICK CALLBACK ----------------

DEADZONE = 10

def joystick_rcjoystick_callback(joystick_x_value, joystick_y_value):
    x = joystick_x_value
    y = joystick_y_value

    # Filter out minor thumb drift
    if abs(x) < DEADZONE:
        x = 0
    if abs(y) < DEADZONE:
        y = 0

    if x == 0 and y == 0:
        MotorsStopAll()
        return

    if abs(y) >= abs(x):
        execute_drive(y, 0)
    else:
        execute_drive(0, x)

# ---------------- SPEED SLIDER CALLBACK ----------------

def slider_bottommotor_callback(slider_value):
    global current_speed_setting
    current_speed_setting = int(slider_value)
    update_hud("Speed Adjusted")

# ---------------- SERVO ARM & GRIPPER CALLBACKS ----------------

def slider_maingripper_callback(slider_value):
    global arm_angle
    arm_angle = int(slider_value)
    try:
        robo.set_servo_angle(1, arm_angle)
    except Exception as e:
        pass
    update_hud("Arm Adjusted")

def slider_5_callback(slider_value):
    global gripper_angle
    gripper_angle = int(slider_value)
    try:
        robo.set_servo_angle(2, gripper_angle)
    except Exception as e:
        pass
    update_hud("Gripper Adjusted")


lcd.qrcode('http://mclab.ai/remote?id=undefined', 72, 32, 176)




