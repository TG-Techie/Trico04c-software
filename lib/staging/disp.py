#import pins
from staging.pin_port import disp_spi,disp_cs, disp_dc, disp_rst, backlight
from tg_modules.make_ios import dio

#start backlight in off position
backlite = dio(backlight,0,False)
backlite.value = False

from adafruit_rgb_display.rgb import colorst
from adafruit_rgb_display.st7735r import ST7735R

disp = ST7735R(disp_spi, cs=dio(disp_cs),
               dc=dio(disp_dc),rst=dio(disp_rst),rotation = 1)
disp.fill(0)

backlite.value = True




def print_credit():
    disp.text(0,0,"Thanks to:")
    disp.text(0,8,'Martin & Arlene Yolles')
    disp.text(0,16,'Kathy Keough')
    disp.text(0,24,'Adafuit Community')
    disp.text(0,32,'Joseph Murphy')
    disp.text(0,0,"   ")
    disp.fill(0)



#disp.text(0,0,"ABCDEFGHIJKLMNOPQRSTU")
#disp.text(0,8,"VWXYZ0123456789().")
#self.text(0,16,'"S,;:@#$%^&*-_+=`~')
#disp.text(0,50,"FOOBAR", size = 3)
#disp.round_rect(0,0,50,50,15,0)
#disp.round_rect(60,10,40,20,5,colorst(180,255,180))        

