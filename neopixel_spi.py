# Simple Neopixel library on SPI

import struct

class NeoPixel_SPI:
    spi=None
    count=None
    colors=None
    
    def __init__(self, spi, count):
        self.spi=spi
        self.count=count
        self.colors=bytearray(count*3)
        
    def init(self, count):
        self.count=count
        self.colors=bytearray(count*3)        
        
    def fillbyte(self, data, buf, idx):
        x=data
        for i in range(8):
            if x & 0x80:
                buf[idx+i]=0xf0
            else:
                buf[idx+i]=0xc0
            x <<= 1

    def set_color(self, idx, color):
        idx=idx*3
        self.colors[idx+0]=struct.pack('<H', color[0])[0]
        self.colors[idx+1]=struct.pack('<H', color[1])[0]
        self.colors[idx+2]=struct.pack('<H', color[2])[0]
        
    def fill_color(self, color):
        for i in range(self.count):
            self.set_color(i,color)

    def show(self):
        bufc=bytearray(8*3*self.count)
        for i in range(self.count):
            icolor=i*3
            idx=icolor*8
            # G, R, B
            self.fillbyte(self.colors[icolor+1],bufc,idx)
            self.fillbyte(self.colors[icolor+0],bufc,idx+8)
            self.fillbyte(self.colors[icolor+2],bufc,idx+16)
        self.spi.write(bufc)


