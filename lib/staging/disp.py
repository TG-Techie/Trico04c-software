import busio, board, digitalio

backlite = digitalio.DigitalInOut(board.D13)
backlite.direction = digitalio.Direction.OUTPUT
backlite.value = False

from adafruit_rgb_display.rgb import colorst
from adafruit_rgb_display.st7735r import ST7735R
disp_spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)
disp = ST7735R(disp_spi, cs=digitalio.DigitalInOut(board.D9),
                      dc=digitalio.DigitalInOut(board.D11),
                      rst=digitalio.DigitalInOut(board.D12), rotation = 1)

disp.fill(0)

backlite.value = True


#disp.text(0,0,"ABCDEFGHIJKLMNOPQRSTU")
#disp.text(0,8,"VWXYZ0123456789().")
#self.text(0,16,'"S,;:@#$%^&*-_+=`~')
#disp.text(0,50,"FOOBAR", size = 3)
#disp.round_rect(0,0,50,50,15,0)
#disp.round_rect(60,10,40,20,5,colorst(180,255,180))        

