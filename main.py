from tg_modules.mem_clean import clean_mem
clean_mem()
from staging import screen
clean_mem()
from tg_modules.tasking import thread_list
clean_mem()

#make the thread_list for the whole project:
trd = thread_list()

#screen init
screen.init(trd)

screen.place_top_bar()

trd.chug()



'''
import time
from adafruit_ds3231 import DS3231

ds = DS3231(i2c)
print(ds.datetime)'''


#example
"""#disp.fill(colorst(0,0,255))
#disp.text(0,0,"ABCDEFGHIJKLMNOPQRSTU")
#disp.text(0,8,"VWXYZ0123456789().")
disp.text(0,16,'"S,;:@ #$%^&*-_+=`~')
disp.text(0,50,"ROB A.", size = 3)
disp.round_rect(0,0,50,50,15,0)
disp.round_rect(60,10,40,20,5,colorst(180,255,180))"""



"""
import time
i2c = busio.I2C(board.SCL, board.SDA)
from adafruit_ds3231 import DS3231
ds = DS3231(i2c)
print(ds.datetime)"""
