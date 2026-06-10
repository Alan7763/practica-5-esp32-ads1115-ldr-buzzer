from machine import Pin, I2C, PWM
from time import sleep_ms

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=100000)

print(i2c.scan())

ADS_ADDR = 0x48

buzzer = PWM(Pin(4))
buzzer.duty_u16(0)

def write_config(channel=0):
    mux = 0x4000
    pga = 0x0200
    mode = 0x0100
    dr = 0x0080
    comp = 0x0003
    os = 0x8000
    config = os | mux | pga | mode | dr | comp
    i2c.writeto_mem(ADS_ADDR, 0x01, config.to_bytes(2, "big"))

def read_ads():
    write_config()
    sleep_ms(10)
    data = i2c.readfrom_mem(ADS_ADDR, 0x00, 2)
    value = int.from_bytes(data, "big")
    if value > 32767:
        value -= 65536
    return value

def map_value(x, in_min, in_max, out_min, out_max):
    if x < in_min:
        x = in_min
    if x > in_max:
        x = in_max
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while True:
    valor = read_ads()
    frecuencia = map_value(valor, 0, 26400, 200, 3000)
    buzzer.freq(frecuencia)
    buzzer.duty_u16(32768)
    print(valor, frecuencia)
    sleep_ms(100)
