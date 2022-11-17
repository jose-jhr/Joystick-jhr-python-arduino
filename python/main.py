from joystickjhr import joystickJhr as joyjhr
from tkinter import ttk, Canvas
from tkinter import *

import serial, time

hw_sensor = serial.Serial(port='COM3', baudrate=9600, timeout=1, write_timeout=1)

# save before command send
beforeCommand = 0

# draw windows
root = Tk()

root.config(width=500, height=500)
root.title("Mi joystick")
# draw label
label = ttk.Label(root, text="JOYSTICK INGENIERIA JHR")
label.pack()

# ancho canvas
widthC = 400
heightC = 400

# ancho joystick
widthJ = 350
heightJ = 350

# posicion joystick
posX = 25
posY = 25
# centro 150+200 = 350 / 2 = 175


joy = joyjhr.JoystickJhr()

canvas = Canvas(root, bg="black", height=heightC, width=widthC)
joy.joy(canvas, widthJ, heightJ, posX, posY, 0.4)
joy.movement(canvas)

canvas.pack()

label = ttk.Label(root, text="JOYSTICK INGENIERIA JHR")
label.pack()


def verifiComandSend():
    global beforeCommand
    angle = joy.angle_joy()

    if beforeCommand != 1 and (337.5 < angle < 360 or 0 < angle < 22.5):
        beforeCommand = 1
        hw_sensor.write(str("1").encode())
    else:
        if beforeCommand != 2 and 22.5 < angle < 67.5:
            beforeCommand = 2
            hw_sensor.write(str("2").encode())
        else:
            if beforeCommand != 3 and 67.5 < angle < 112.5:
                beforeCommand = 3
                hw_sensor.write(str("3").encode())
            else:
                if beforeCommand != 4 and 112.5 < angle < 157.5:
                    beforeCommand = 4
                    hw_sensor.write(str("4").encode())
                else:
                    if beforeCommand != 5 and 157.5 < angle < 202.5:
                        beforeCommand = 5
                        hw_sensor.write(str("5").encode())
                    else:
                        if beforeCommand != 6 and 202.5 < angle < 247.5:
                            beforeCommand = 6
                            hw_sensor.write(str("6").encode())
                        else:
                            if beforeCommand != 7 and 247.5 < angle < 292.5:
                                beforeCommand = 7
                                hw_sensor.write(str("7").encode())
                            else:
                                if beforeCommand != 8 and 292.5 < angle < 337.5:
                                    beforeCommand = 8
                                    hw_sensor.write(str("8").encode())
                                else:
                                    if beforeCommand != 0 and angle == 0:
                                        beforeCommand = 0
                                        hw_sensor.write(str("0").encode())


while True:
    # capturar tiempo trascurrido
    verifiComandSend()
    root.update_idletasks()
    root.update()
