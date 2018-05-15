import busio, digitalio, board, pulseio, time
from adafruit_rgb_display.rgb import colorst
from adafruit_rgb_display.st7735r import ST7735R
disp_spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)
disp = ST7735R(disp_spi, cs=digitalio.DigitalInOut(board.D9),
                      dc=digitalio.DigitalInOut(board.D11),
                      rst=digitalio.DigitalInOut(board.D12))



disp.fill(colorst(0,0,255))

#disp.text(0,0,"ABCDEFGHIJKLMNOPQRSTU")
#disp.text(0,8,"VWXYZ0123456789().")
disp.text(0,16,'"S,;:@#$%^&*-_+=`~')
disp.text(0,50,"FOOBAR", size = 3)

