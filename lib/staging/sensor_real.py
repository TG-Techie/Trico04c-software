import staging.pin_port as pp
from tg_Modules.mem_clean import clean_mem
clean_mem()

from adafruit.ds3231 import DS3231

TEST_VAL = True
def test(x):
    if TEST_VAL:
        print(x)

#set up time
rtc = DS3231(pp.i2c_port)

def get_time():
    struct = rtc.datetime
    
