from microbit import *

i=100
while True :
    if button_a.is_pressed():
        if i<=1000:
            pin0.write_analog(i)
            sleep(2000)
            i=i+100
        else:
            i=100
            pin0.write_analog(i)
   
    elif button_b.is_pressed():
        pin0.write_digital(0)
   
    
    
   