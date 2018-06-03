import board, busio

#feather express:
#['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'SCK', 'MOSI', 'MISO',
#'D0', 'RX', 'D1', 'TX', 'SDA', 'SCL', 'D5', 'D6', 'D9', 'D10',
#'D11', 'D12', 'D13', 'NEOPIXEL']

#i2c
sda = board.SDA
scl = board.SCL
i2c_port = busio.I2C(scl, sda)

#spi for display
backlight = board.D13
disp_sck = board.SCK
disp_mosi = board.MOSI
disp_miso = board.MISO
disp_cs = board.D9
disp_dc = board.D11
disp_rst = board.D12
disp_spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)
