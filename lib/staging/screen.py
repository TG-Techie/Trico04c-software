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
    clean_mem()

def text_task(x,y,str):
    thread.add_task(disp.text,(x,y,str),3)
    clean_mem()

def rect_task(x,y,w,h,color):
    thread.add_task(disp.rect,(x,y, w ,h,color),1)
    clean_mem()
    
def place_top_bar():
    
    time_tup = sensor.get_time()
    clean_mem()
    if time_tup[3] >12:
        time_string = str(time_tup[3]-12) + ':'
    else:
        time_string = str(time_tup[3]) + ':'
    time_string += str(time_tup[4])
    if len(time_string) < 5:
        time_string = '0' + time_string
    clean_mem()
    text_task(int(disp.width/2) - int(5*6 /2),gap,time_string)
    clean_mem()
    per_offset = 0
    bat_per = sensor.bat_percent()
    if bat_per == 100:
        per_offset = 1
    text_task(int(disp.width - gap - 6*(6+per_offset)), gap,
                               str(bat_per) +'% *bata' + str(int(bat_per*6/100)) + '*')
    rect_task(0,8+2*gap, disp.width ,gap,white)
    clean_mem()
    
