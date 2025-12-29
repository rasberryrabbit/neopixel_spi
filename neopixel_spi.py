# Simple Neopixel library on SPI
# must be set SPI clock to 3.2MHz for 800kHz neopixel
# b1000 for 0,  b1110 for 1. It saves memory.
# W600 Pico board need SPI option "phase=1"

import struct

class NeoPixel_SPI:
    spi=None
    count=None
    colors=None
    bpp=3
    
    def __init__(self, spi, count, bpp=3):
        self.spi=spi
        self.count=count
        self.colors=bytearray(count*bpp)
        self.bpp=bpp
        
    def init(self, count, bpp=3):
        self.count=count
        self.colors=bytearray(count*bpp)
        self.bpp=bpp
        
    def fillbyte(self, data, buf, idx):
        x=data
        # 2 bits in 1 byte
        for i in range(4):
            if x & 0x80:
                nb=0xe0
            else:
                nb=0x80
            if x & 0x40:
                nb |= 0x0e
            else:
                nb |= 0x08
            x <<= 2
            buf[idx+i]=nb

    def set_color(self, idx, color):
        idx=idx*self.bpp
        for i in range(self.bpp):
            self.colors[idx+i]=struct.pack('<H', color[i])[0]
        
    def fill_color(self, color):
        for i in range(self.count):
            self.set_color(i,color)

    def show(self):
        bufc=bytearray(4*self.bpp*self.count)
        for i in range(self.count):
            icolor=i*self.bpp
            idx=icolor*4
            # G, R, B
            self.fillbyte(self.colors[icolor+1],bufc,idx)
            self.fillbyte(self.colors[icolor+0],bufc,idx+4)
            self.fillbyte(self.colors[icolor+2],bufc,idx+8)
            if self.bpp>3:
                self.fillbyte(self.colors[icolor+3],bufc,idx+12)
        self.spi.write(bufc)


