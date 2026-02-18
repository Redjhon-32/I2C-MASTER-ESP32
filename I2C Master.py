from machine import Pin, I2C
import time

SLAVE_ADDR = 0x42

i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=100000)

print("Scan:", [hex(x) for x in i2c.scan()])

while True:
    try:
    
        data = i2c.readfrom(SLAVE_ADDR, 2)
        
        valor = data[0] | (data[1] << 8)

        print("Dato recibido:", valor)

        time.sleep_ms(500)

    except OSError as e:
        print("Error I2C:", e)
        time.sleep(1)
