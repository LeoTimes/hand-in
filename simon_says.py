# Add your Python code here. E.g.

from microbit import *
import random

#CREATION OF THE FOUR IMAGES
upleft= Image("99000:99000:00000:00000:00000")
upright = Image("00099:00099:00000:00000:00000")
downleft = Image("00000:00000:00000:99000:99000")
downright = Image("00000:00000:00000:00099:00099")

sequence = []
pictures = [upleft,upright,downleft,downright]

while True:
    #DEFINE LIST IN WHILE-LOOP, SO USER MUST PRESS WHOLE SEQUENCES AGAIN
    user_input = []
    
    #CREATION OF SEQUENCE
    s = random.randint(0,3)
    sequence.append(pictures[s])

    #SHOW SEQUENCE
    for i in range(len(sequence)):
        display.show(sequence[i])
        sleep(700)
        display.clear()
        sleep(500)

    ###MOVEMENT WITH ACCELEROMETER 
    # USER INPUTS GET INSERTED IN TO LIST
    while len(user_input) < len(sequence):
        LR = accelerometer.get_x()
        WD = accelerometer.get_y()
        if LR < -110 and WD < 110:
            display.show(upleft)
            if button_b.get_presses():
                user_input.append(pictures[0])
       
        elif LR < 110 and WD < 110:
            display.show(upright)
            if button_b.get_presses():
                user_input.append(pictures[1])
        
        elif LR < -110 and WD > 110:
            display.show(downleft)
            if button_b.get_presses():
                user_input.append(pictures[2])         
        
        elif LR > 110 and WD > 110:
            display.show(downright)
            if button_b.get_presses():
                user_input.append(pictures[3])

#CHEK IF USER PRESSED THE RIGHT SEQUENCE           
    if user_input != sequence:
        break
    display.clear()
    sleep(2000)
display.scroll("Game Over")
