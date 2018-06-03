from tg_modules.mem_clean import clean_mem
from staging.disp import disp, backlite as back_light, colorst
clean_mem()
from staging import sensor
clean_mem()

#construction spacing
gap = 2

#colors:
text_color = colorst(255,255,255)
white = colorst(255,255,255)
black = 0
red = colorst(255,0,0)
green = colorst(0,255,0)
blue = colorst(0,0,255)

###########: the thread_list to add stuff to
thread = None
def init(thread_list):
    global thread
    thread = thread_list


def place_top_bar():
    thread.add_task(disp.rect,(0,8+2*gap, disp.width ,gap,white),1)
    time_tup = sensor.get_time()
    if time_tup[3] >12:
        time_string = str(time_tup[3]-12) + ':'
    else:
        time_string = str(time_tup[3]) + ':'
    time_string += str(time_tup[4])
    if len(time_string) < 5:
        time_string = '0' + time_string
    thread.add_task(disp.text,(int(disp.width/2) - int(5*5 /2), gap,time_string),3)
