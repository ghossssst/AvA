import board
from pynput import keyboard
from pynput.keyboard import Key
from rainbowio import colorwheel
import neopixel
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import AngularServo
from time import sleep
from guizero import App, Slider

factory = PiGPIOFactory()
pixel_pin = board.D18
num_pixels = 10

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0, auto_write=True)


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255,255,255)

pixels.fill((WHITE))

azimuth = AngularServo(24, min_angle=-180, max_angle=180, min_pulse_width=0.544/1000, max_pulse_width=2.5/1000, pin_factory=factory)

elevation = AngularServo(23, min_angle=-180, max_angle=180, min_pulse_width=0.544/1000, max_pulse_width=2.5/1000, pin_factory=factory)

def azimuth_slider_changed(angle):
 azimuth.angle = int(angle)
 print(int(angle))
 
def elevation_slider_changed(angle):
 elevation.angle = int(angle)
 print(int(angle))

def brightness_slider_changed(inputbrightness):
    inputbrightness = float(inputbrightness) / float(1000)
    pixels.brightness = float(inputbrightness)
 
app = App(title='Servo Angle', width=500, height=300)
azimuth_slider = Slider(app, start=-180, end=180, command=azimuth_slider_changed, width='fill', height=50)
elevation_slider = Slider(app, start=-180, end=180, command=elevation_slider_changed, width='fill', height=50)
brightness_slider = Slider(app, start=0, end=1000, command=brightness_slider_changed, width='fill', height=50)
azimuth_slider.text_size = 15
elevation_slider.text_size = 15
brightness_slider.text_size = 15
app.display()