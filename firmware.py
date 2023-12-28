import sys
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
    
    #Logs
    def logs():
        global logsFile
        logsFile = open("logs.txt", "w")
        logsFile.write("")
        logsFile.close()
        logsFile = open("logs.txt", "a")
        logsFile.write("Booting... \n")
        logsFile.close()
    
    logs()
    #END
    
    #Important Functions (DONT DELETE)
    def runFile():
        code.Main()

    def crashLogs():
        global logsFile
        logsFile = open("logs.txt", "a")
        logsFile.write("ERROR AT THIS STAGE")
        logsFile.Close
        
    def crash():
        print("This program has crashed!, please check the crash logs to see when it crashed")
        lcd.putstr("CRASHED! CHECK LOGS")
        sys.exit(1)

    def bootLogs():
        #LOG FILE BEGIN
        global logsFile
        logsFile = open("logs.txt", "a")
        logsFile.write("Writing Logs... \n")
        bootLogsFile = open("bootLogs.txt", "w")
        bootLogsFile.write("")
        bootLogsFile.close()
        bootLogsFile = open("bootLogs.txt", "a")
        bootLogsFile.write("Booted! \n")
        bootLogsFile.write("Checking for code.py file... \n") #Checks for the coding file
        bootLogsFile.close()
        codeFile = open("code.py", "a")
        codeFile.close()
        bootLogsFile = open("bootLogs.txt", "a")
        bootLogsFile.write("code.py file exists. \n")
        bootLogsFile.write("Checking for LCD files... \n") #Checks for LCD files
        bootLogsFile.close()
        lcdFile = open("lcd_api.py", "a")
        lcdFile.close()
        lcdFile = open("pico_i2c_lcd.py", "a")
        lcdFile.close()
        bootLogsFile = open("bootLogs.txt", "a")
        bootLogsFile.write("LCD files exist. \n")
        bootLogsFile.write("Boot Logging all done! Proceeding to program... \n")
        logsFile.write("Boot Has been Logged \n")
        logsFile.close
        #END
        
    #END
        
    bootLogs()
    
    def boot():
        try:
            global logsFile
            logsFile = open("logs.txt", "a")
            logsFile.write("Giving Variables Value... /n")
            #put variables here
            hi = "Hello, World!"
            i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
            lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
            
            #END
            print("boot")
            logsFile.close()
            
            def code():
                while True:
                    global logsFile
                    logsFile = open("logs.txt", "a")
                    logsFile.Write("Running Code... \n")
                    utime.sleep(1)
                    #You can put anything here
                    print(hi)
                    lcd.putstr("Boot")
                    sys.implementation()
                    logsFile.write("BOOTING")
                    logsfile.close()
                    #Just dont delete the runFile(). Thats where you code
                    #Run File
                    runFile()
                    #END
            code()
        except:
            crash()
#Run Code
main()
