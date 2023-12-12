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
    
    def boot():
        #put variables here
        hi = "Hello, World!"
        i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
        lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
        
        def runFile():
            code.Main()
        
        #END
        print("boot")
        
        def code():
            while True:
                utime.sleep(1)
                print(hi)
                lcd.putstr("Hello")
                #Run File
                runFile()
                #END
        code()
        
#Run Code
main()