#LED_Ansteuerung der oberen 4 LED Streifen
import board
import neopixel
import time
LED_PIN = board.D10 # GPIO Pin 10
LED_COUNT= 240
LED_COUNT_ZEILE = 60
import gc
def obereZeile(LED_Z1, LED_Z2, LED_Z3, LED_Z4):
    ORDER = neopixel.RGB
    pixels = neopixel.NeoPixel(LED_PIN,LED_COUNT, pixel_order = ORDER)
    for i in range(60):
        pixels[i] = (LED_Z1[i],LED_Z1[i*2],LED_Z1[i*3])
        pixels[60+i]=(LED_Z2[i],LED_Z2[i*2],LED_Z2[i*3])
        pixels[120+i]=(LED_Z3[i],LED_Z3[i*2],LED_Z3[i*3])
        pixels[180+i]=(LED_Z4[i],LED_Z4[i*2],LED_Z4[i*3])   
    pixels.show()
    del pixels
    time.sleep(2)
    gc.collect()
