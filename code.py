import sys
import firmware
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

class Main():
    #Initializing Again
    I2C_ADDR     = 0x27
    I2C_NUM_ROWS = 4
    I2C_NUM_COLS = 20
    #END
    
    while True:
        def successfulAction():
            logsFile = open("logs.txt", "a");
            logsFile.write("Action Done Successfully \n")
            logsFile.close()
            
        def failedAction():
            logsfile = open("logs.txt", "a")
            logsFile.write("Action Could Not Be Done \n")
            logsFile.close()
        try:
            #Write Code Here :)
            print("hi")
            action.successfulAction()
            break
            #END
        except:
            print("PROGRAM ERROR! CHECK BOOTLOGS")
            failedAction()
            sys.exit(1)
Main()