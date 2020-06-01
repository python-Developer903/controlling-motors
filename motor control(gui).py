import RPi.GPIO as GPIO
import time
from tkinter import *
import tkinter.font

# Libraries Imported successfully

# Raspberry Pi 3 Pin Settings

PWMPin = 21 # PWM Pin connected to ENA.
Motor1 = 20 # Connected to Input 1.
Motor2 = 16 # Connected to Input 2.
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # We are accessing GPIOs according to their physical location
GPIO.setup(PWMPin, GPIO.OUT) # We have set our pin mode to output
GPIO.setup(Motor1, GPIO.OUT)
GPIO.setup(Motor2, GPIO.OUT)

GPIO.output(PWMPin, GPIO.LOW) # When it will start then all Pins will be LOW.
GPIO.output(Motor1, GPIO.LOW)
GPIO.output(Motor2, GPIO.LOW)

PwmValue = GPIO.PWM(PWMPin, 2000) # We have set our PWM frequency to 2000.
PwmValue.start(100) # That's the maximum value 100 %.

# Raspberry Pi 3 Pin Settings Completed

# tkinter GUI basic settings

Gui = Tk()
Gui.title("DC Motor Control with Pi 3")
Gui.config(background= "#0080FF")
Gui.minsize(800,300)
Font1 = tkinter.font.Font(family = 'Helvetica', size = 18, weight = 'bold')

# tkinter simple GUI created

def MotorClockwise():
    GPIO.output(Motor1, GPIO.LOW) # Motor will move in clockwise direction.
    GPIO.output(Motor2, GPIO.HIGH)
    
def MotorAntiClockwise():
    GPIO.output(Motor1, GPIO.HIGH) # Motor will move in anti-clockwise direction.
    GPIO.output(Motor2, GPIO.LOW)

def MotorStop():
    GPIO.output(Motor1, GPIO.LOW) # Motor will stop.
    GPIO.output(Motor2, GPIO.LOW)
    
def ChangePWM(self):
    PwmValue.ChangeDutyCycle(Scale1.get())

Text1 = Label(Gui,text='Motor Status:', font = Font1, fg='#FFFFFF', bg = '#0080FF', padx = 50, pady = 50)
Text1.grid(row=0,column=0)

Text2 = Label(Gui,text='Stop', font = Font1, fg='#FFFFFF', bg = '#0080FF', padx = 0)
Text2.grid(row=0,column=1)

Text1 = Label(Gui,text=' ', font = Font1, fg='#FFFFFF', bg = '#0080FF', padx = 150, pady = 50)
Text1.grid(row=0,column=2)

Button1 = Button(Gui, text='Clockwise', font = Font1, command = MotorClockwise, bg='bisque2', height = 1, width = 10)
Button1.grid(row=1,column=0)

Button2 = Button(Gui, text=' Motor Stop', font = Font1, command = MotorStop, bg='bisque2', height = 1, width = 10)
Button2.grid(row=1,column=1)

Button2 = Button(Gui, text='AntiClockwise', font = Font1, command = MotorAntiClockwise, bg='bisque2', padx = 50, height = 1, width = 10)
Button2.grid(row=1,column=2)

Text3 = Label(Gui,text='', font = Font1, bg = '#0080FF', fg='#FFFFFF', padx = 50, pady = 50)
Text3.grid(row=2,columnspan=2)

Scale1 = Scale(Gui, from_=0, to=100, orient = HORIZONTAL, resolution = 1, command = ChangePWM)
Scale1.grid(row=2,column=2)

Gui.mainloop()
