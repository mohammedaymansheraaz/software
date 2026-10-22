from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
remoteInit()

screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


joystick_x_value = None
joystick_y_value = None
slider_value = None







def joystick_1_callback(joystick_x_value, joystick_y_value):
  global slider_value 
  print(joystick_y_value)
  print(joystick_x_value)

def slider_1_callback(slider_value):
  global joystick_y_value, joystick_x_value 
  print(slider_value)

def slider_2_callback(slider_value):
  global joystick_y_value, joystick_x_value 
  print(slider_value)

lcd.qrcode('http://mclab.ai/remote?id=8d42760a951740cb8af50758c253a5c9', 72, 32, 176)
