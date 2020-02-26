
from main_LED_Treiber import *
PIXEL_COUNT_ZEILE = 60
Z1 = [None]*PIXEL_COUNT_ZEILE
Z2 = [None]*PIXEL_COUNT_ZEILE
Z3 = [None]*PIXEL_COUNT_ZEILE
Z4 = [None]*PIXEL_COUNT_ZEILE
Z5 = [None]*PIXEL_COUNT_ZEILE
Z6 = [None]*PIXEL_COUNT_ZEILE
Z7 = [None]*PIXEL_COUNT_ZEILE
Z8 = [None]*PIXEL_COUNT_ZEILE
Z9 = [None]*PIXEL_COUNT_ZEILE
Z10 = [None]*PIXEL_COUNT_ZEILE
Z11 = [None]*PIXEL_COUNT_ZEILE
Z12 = [None]*PIXEL_COUNT_ZEILE
Z13 = [None]*PIXEL_COUNT_ZEILE
Z14 = [None]*PIXEL_COUNT_ZEILE
Z15 = [None]*PIXEL_COUNT_ZEILE

for i in range (180):
    Z1[i] = [i,0,255-i]
    Z2[i] = [i,0,255-i]
    Z3[i] = [i,0,255-i]
    Z4[i] = [i,0,255-i]
    Z5[i] = [i,0,255-i]
    Z6[i] = [i,0,255-i]
    Z7[i] = [i,0,255-i]
    Z8[i] = [i,0,255-i]
    Z9[i] = [i,0,255-i]
    Z10[i] = [i,0,255-i]
    Z11[i] = [i,0,255-i]
    Z12[i] = [i,0,255-i]
    Z13[i] = [i,0,255-i]
    Z14[i] = [i,0,255-i]
    Z15[i] = [i,0,255-i]
    
x = LED_Treiber(Z1, Z2, Z3, Z4, Z5,Z6, Z7, Z8, Z9, Z10, Z11, Z12, Z13, Z14, Z15)
x.anzeigen()