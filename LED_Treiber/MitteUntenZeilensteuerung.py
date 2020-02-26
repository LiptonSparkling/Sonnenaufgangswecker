# LED_Ansteuerung der mitte unten 4 LED Streifen
import board
import neopixel
import time
LED_PIN = board.D18 # GPIO 18
LED_COUNT= 240

def mitteUnten(LED_Z9, LED_Z10, LED_Z11, LED_Z12):
    ORDER = neopixel.RGB
    pixels = neopixel.NeoPixel(LED_PIN,LED_COUNT, pixel_order = ORDER)
    for i in range(60):
        pixels[i] = (LED_Z9[i],LED_Z9[i*2],LED_Z9[i*3])
        pixels[60+i]=(LED_Z10[i],LED_Z10[i*2],LED_Z10[i*3])
        pixels[120+i]=(LED_Z11[i],LED_Z11[i*2],LED_Z11[i*3])
        pixels[180+i]=(LED_Z12[i],LED_Z12[i*2],LED_Z12[i*3])   
    pixels.show()
    del pixels
    time.sleep(2)
