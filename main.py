from gc import collect as clean_mem
import gc
gc.enable()
clean_mem()
from staging import screen
clean_mem()
from tg_modules.tasking import thread_list
clean_mem()


#make the thread_list for the whole project, send to screen:
trd = thread_list()
screen.init(trd)
clean_mem()



screen.place_top_bar()
trd.chug()
clean_mem()
screen.place_top_bar()
trd.chug()


'''from staging.pin_port import i2c_port
import time

from adafruit.ds3231 import DS3231

print(gc.mem_free(),gc.mem_alloc())

ds = DS3231(i2c_port)
print(ds.datetime)'''
