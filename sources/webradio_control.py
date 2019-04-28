#!/usr/bin/python
"""
   
    Changes the radio chanel or toggles play/pause

    April 2019, Ves   
 

"""
import RPi.GPIO as GPIO
import time
import os
import syslog

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

chanel=1
max_chanel=5

while True:
    input_state_23 = GPIO.input(23)
    input_state_24 = GPIO.input(24)

    # increase the chanel 
    if input_state_23 == False and input_state_24 == True:
        chanel=(chanel+1) % max_chanel 
        syslog.syslog('Button Pressed UP. Current chanel '+str(chanel))
        os.system("mpc play "+str(chanel + 1))

    # decrease the chanel  
    if input_state_24 == False and input_state_23 == True:
        chanel=(chanel-1) % max_chanel 
        syslog.syslog('Button Pressed DOWN. Current chanel '+str(chanel))
        os.system("mpc play "+str(chanel + 1))

    # toggle pause or play     
    if input_state_24 == False and input_state_23 == False:
        syslog.syslog('Buttons Pressed DOWN+UP. Toggle' )
        os.system("mpc toggle")

    time.sleep(0.3)

