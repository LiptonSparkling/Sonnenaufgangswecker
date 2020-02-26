# LED_Ansteuerung der mittig oberen 4 LED Streifen
import board
import neopixel
import time
import gc
LED_PIN = board.D12 # GPIO 12
LED_COUNT= 240
ORDER = neopixel.RGB

def mitteOben(LED_Z5, LED_Z6, LED_Z7, LED_Z8):
    ORDER = neopixel.RGB
    pixel = neopixel.NeoPixel(LED_PIN,LED_COUNT, pixel_order = ORDER)
    for i in range(60):
        pixel[i] = (LED_Z5[i],LED_Z5[i*2],LED_Z5[i*3])
        pixel[60+i]=(LED_Z6[i],LED_Z6[i*2],LED_Z6[i*3])
        pixel[120+i]=(LED_Z7[i],LED_Z7[i*2],LED_Z7[i*3])
        pixel[180+i]=(LED_Z8[i],LED_Z8[i*2],LED_Z8[i*3])   
    pixel.show()
    time.sleep(1)
    del pixel
    gc.collect()
    time.sleep(1)
