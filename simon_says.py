# Add your Python code here. E.g.

from microbit import *
import random


    
    





 upleft= Image("99000:99000:00000:00000:00000")
upright = Image("00099:00099:00000:00000:00000")
downleft = Image("00000:00000:00000:99000:99000")
downright = Image("00000:00000:00000:00099:00099")
    

User_input = []
Reihenfolge = []
Bilder = [upleft,upright,downleft,downright]

while True:
    #CREATION OF SEQUENCE
    s = random.randint(0,3)
    Reihenfolge.append(Bilder[s])
    for i in range(len(Reihenfolge)):
        display.show(Reihenfolge[i])
        sleep(700)
        display.clear()
        sleep(500)
    ###MOVEMENT WITH ACCELEROMETER 
    # USER INPUTS GET INSERTED IN TO LIST
    while len(User_input) < len(Reihenfolge):
        LR = accelerometer.get_x()
        WD = accelerometer.get_y()
        if LR < -110 and WD < 110:
            display.show(upleft)
            if button_b.get_presses():
                User_input.append(upleft)
        elif LR < 110 and WD < 110:
            display.show(upright)
            if button_b.get_presses():
                User_input.append(upright)
        elif LR < -110 and WD > 110:
            display.show(downleft)
            if button_b.get_presses():
                User_input.append(downleft)         
        elif LR > 110 and WD > 110:
            display.show(downright)
            if button_b.get_presses():
                User_input.append(downright)
#CHEK IF USER PRESSED THE RIGHT SEQUENCE           
    if User_input != Reihenfolge:
        break
    display.clear()
    sleep(2000)
display.scroll("Game Over")

