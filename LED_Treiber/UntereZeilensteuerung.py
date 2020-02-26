#LED_Ansteuerung der unteren 3 LED Streifen
import board
import neopixel
LED_PIN = board.D21 # GPIO Pin 21
LED_COUNT= 180
LED_COUNT_ZEILE = 60

def untereZeile(LED_Z13, LED_Z14, LED_Z15):
    ORDER = neopixel.RGB
    pixels = neopixel.NeoPixel(LED_PIN,LED_COUNT, pixel_order = ORDER)
    for i in range(60):
        pixels[i] = (LED_Z13[i],LED_Z13[i*2],LED_Z13[i*3])
        pixels[60+i]=(LED_Z14[i],LED_Z14[i*2],LED_Z14[i*3])
        pixels[120+i]=(LED_Z15[i],LED_Z15[i*2],LED_Z15[i*3])
        
    pixels.show()
    del pixels
    
    
