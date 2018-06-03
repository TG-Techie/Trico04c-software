import board, time
import neopixel_write
import digitalio

""" example code:
import board, time
from staging.tg_neo import neo_strand

my_strand = neo_strand(board.NEOPIXEL,10)
my_strand.clear()

my_strand.write(0,255,0,0)
time.sleep(1)
my_strand.write(1,0,255,0)
time.sleep(1)
my_strand.write(2,0,0,255)
time.sleep(3)
my_strand.write((3,4,5,6,7,8,9),128,128,128)
time.sleep(2)


my_strand.clear()
time.sleep(1)

my_strand.set_pixel(2,0,0255,255)
my_strand.send()
time.sleep(3)

my_strand.clear()

"""
global color_buf
#this is for development deguging
TEST_VAL = False
def test(*x):
    if TEST_VAL:
        for i in x:
            print(i)

class neo_strand():

    def __init__(self,brd_pin,length):
        self.pin =  digitalio.DigitalInOut(brd_pin)
        self.pin.direction = digitalio.Direction.OUTPUT
        self.length = length
        self.stat_list = [0]*length*3
        self.send()

    def write(self, location_tup, r,g,b):
        if type(location_tup) != tuple:
            location_tup = (location_tup,)
        for i in location_tup:
            self.set_pixel(i,r,g,b)
        self.send()

    def send(self):
        test('list sent: ',self.stat_list)
        neopixel_write.neopixel_write(self.pin, bytearray(self.stat_list))

    def set_pixel(self,location,r,g,b):
        test("colors set rgb:")
        for i in range(3):
            test((r,g,b)[i])
            self.stat_list[location*3+i] = (g,r,b)[i]
#******************************************^^^^^^*********
#change color order here >>>>>>>>>>>>>>>   ^^^^^^
#*********************************************************


    def clear(self):
        self.stat_list = [0]*self.length*3
        self.send()

""" def blink(self, location,r,g,b, duration=.2):
        color_buf = self.stat_list[0:]
        test('buffered color list',color_buf)
        self.write(location,r,g,b)
        test('blink duration: seconds',duration)
        time.sleep(duration)
        
        self.send()"""
