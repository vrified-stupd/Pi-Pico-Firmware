import utime
import machine
import code
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

class main():
    #Initializing Stuff
    I2C_ADDR     = 0x27
    I2C_NUM_ROWS = 4
    I2C_NUM_COLS = 20
    #END
    
    #Important Functions (DONT DELETE)
    def runFile():
        code.Main()

    def crash():
        print("This program has crashed!, please check the crash logs to see why")
        lcd.putstr("CRASHED! CHECK LOGS")

    def bootLogs():
        #LOG FILE BEGIN
        logsFile = open("logs.txt", "w")
        logsFile.write("")
        logsFile.close()
        logsFile = open("logs.txt", "a")
        logsFile.write("Booted! \n")
        logsFile.write("Checking for code.py file... \n") #Checks for the coding file
        logsFile.close()
        codeFile = open("code.py" "a")
        codeFile.close()
        logsFile = open("logs.txt", "a")
        logsFile.write("code.py file exists. \n")
        logsFile.write("Checking for LCD files... \n") #Checks for LCD files
        logsFile.close()
        lcdFile = open("lcd_api.py", "a")
        lcdFile.close()
        lcdFile = open("pico_i2c_lcd.py", "a")
        lcdFile.close()
        logsFile = open("logs.txt", "a")
        logsFile.write("LCD files exist. \n")
        logsFile.write("Boot Logging all done! Proceeding to program... \n")
        #END
        
    def crashLogs():
        print("") #THIS IS NOT YET FINISHED
        
    #END
        
    bootLogs()
    
    def boot():
        #put variables here
        hi = "Hello, World!"
        i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
        lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
        
        #END
        print("boot")
        
        def code():
            while True:
                utime.sleep(1)
                #You can put anything here
                print(hi)
                lcd.putstr("Hello")
                #Just dont delete the runFile(). Thats where you code
                #Run File
                runFile()
                #END
        code()
        
#Run Code
main()
