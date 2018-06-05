from gc import collect as clean_mem
clean_mem()
import random
clean_mem()


def get_time():
    return (2018,06,13,15,14,15,0,135)
    clean_mem()

def bat_percent():
    return (100,10,50)[random.randrange(3)]
    clean_mem()

def is_charging():
    return(0,1,0)[random.randrange(3)]
    clean_mem()
