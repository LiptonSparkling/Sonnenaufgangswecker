from ObereZeilensteuerung import obereZeile
from MitteObereZeilensteuerung import mitteOben
from MitteUntenZeilensteuerung import mitteUnten
from UntereZeilensteuerung import untereZeile

class LED_Treiber():
    def __init__(self, z1, z2, z3, z4, z5, z6, z7, z8, z9, z10, z11, z12, z13, z14, z15, helligkeit = 0.2):
        self.helligkeit = helligkeit
        self.z1 = z1
        self.z2 = z2
        self.z3 = z3
        self.z4 = z4
        self.z5 = z5
        self.z6 = z6
        self.z7 = z7
        self.z8 = z8
        self.z9 = z9
        self.z10 = z10
        self.z11 = z11
        self.z12 = z12
        self.z13 = z13
        self.z14 = z14
        self.z15 = z15
        
    def anzeigen(self):
        obereZeile(self.z1,self.z2, self.z3, self.z4)
       # mitteOben(self.z5, self.z6, self.z7, self.z8)
        #mitteUnten(self.z9, self.z10, self.z11, self.z12)
        #untereZeile(z13, z14, z15)
        return
