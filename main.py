from machine import Timer,Pin, SPI, I2C
import time
import network, random


from neopixel_spi import NeoPixel_SPI

# 800kHz * 8 / 2 = 3.2MHz, on ESP32. some board need "phase=1" on SPI option.
spi=SPI(1, 3200000, sck=Pin(14), mosi=Pin(13))

neo = NeoPixel_SPI(spi,8)

neo.fill_color([0,0,0])
neo.show()

for k in range(3):
    for i in range(8):
        neo.fill_color([0,0,0])
        neo.set_color(i,[100,0,0])
        neo.show()
        time.sleep(0.1)
        
    for i in range(8):
        neo.fill_color([0,0,0])
        neo.set_color(i,[0,100,0])
        neo.show()
        time.sleep(0.1)
        
    for i in range(8):
        neo.fill_color([0,0,0])
        neo.set_color(i,[0,0,100])
        neo.show()
        time.sleep(0.1)

def updatepixel(t):
    for i in range(8):
        r = random.randint(0,80)
        g = random.randint(0,80)
        b = random.randint(0,80)
        neo.set_color(i,[r,g,b])
    neo.show()

tim=Timer(0)
tim.init(period=1000, mode=Timer.PERIODIC, callback=updatepixel)

