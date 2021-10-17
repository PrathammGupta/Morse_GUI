from tkinter import *
import tkinter.font
import time
import RPi.GPIO as GPIO
from gpiozero import LED
GPIO.setmode(GPIO.BCM)

Code = { 'A' : '.-' , 'B' : '-...' , 'C' : '-.-.' , 'D' : '-..' , 'E' : '.' ,
'F' : '..-.' ,'G' : '--.' , 'H' : '....' ,'I' : '..' ,'J' : '.---' ,'K' : '-.-' ,
'L' : '.-..' , 'M' : '--' , 'N' : '-.' ,'O' : '---' ,'P' : '.--.' ,'Q' : '--.-' ,
'R' : '.-.' , 'S' : '...' ,'T' : '-' ,'U' : '..-' ,'V' : '...-' ,'W' : '.--' ,
'X' : '-..-' ,'Y' : '-.--' , 'Z' : '--..' }

LED = 20
GPIO.setup(LED, GPIO.OUT)

Window = Tk()
Window.title("Task 5.3D ")
myFont = tkinter.font.Font( family = 'Aerial', size = 16, weight = "bold")

def DOT():
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.4)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.4)

def DASH():
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(1.2)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.4)

def MORSE():
    TEXT = INPUT.get()
    for alphabet in TEXT:
        for symbol in Code[alphabet.upper()]:
            if symbol == '-':
                DASH()
            elif symbol == '.':
                DOT()
            else:
                time.sleep(0.4)
        time.sleep(0.4) 

read_value = Entry(window, font = myFont, width = 16)
read_value.grid(row = 0, column = 0)

button = Button(window, text = 'Start', font = myFont, command = Morse(), height = 1, width = 8)
button.grid( row =1, column = 0)

window.mainloop()
                



