from gc import collect as clean_mem
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
    del thread_list
    clean_mem()

def text_task(x,y,str, priority = 3):
    thread.add_task(disp.text,(x,y,str),priority)
    del x,y,str
    clean_mem()

def rect_task(x,y,w,h,color,priority = 1):
    thread.add_task(disp.rect,(x,y, w ,h,color),priority)
    del x,y,w,h,color
    clean_mem()
    
def place_top_bar():
    rect_task(0,0,disp.width,10,black)
    #figure out time
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
    del time_string, time_tup
    clean_mem()
    #figure out bat percent
    bat_per = sensor.bat_percent()
    bat_string = ''
    if bat_per < 100:
        bat_string += ' '
    if bat_per < 10:
        bat_string += ' '
    bat_string += str(bat_per) + '%__bata'
    if sensor.is_charging():
        bat_string += 'chrg__'
    else:
        bat_string += str(int((bat_per+10)*6/100)) + '__'
    text_task(int(disp.width - 3 - 6*(6)), gap, bat_string)
    del bat_per, bat_string
    clean_mem()
    #add rect bar
    rect_task(0,8+2*gap, disp.width ,gap,white)
    clean_mem()


