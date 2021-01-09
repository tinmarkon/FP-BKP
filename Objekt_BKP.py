import time
class BKP:

    def __init__(self, teze, s_prihodek, i_prihodek, kapital, optimisticen):
        self.teze = teze
        self.s_prihodek = s_prihodek
        self.i_prihodek = i_prihodek
        self.kapital = kapital
        self.optimisticen = True

    def optimalna_resitev(self):
        print("Optimalna resitev danega problema:") #uporabimo funkcijo iz BKP.py

    def casovna_zahtevnost(self):
        print("Cas, ki ga algoritem porabi za izracun opt. resitve danega problema:")
        zacetek = time.perf_counter()
        ### Tu kličema bkp ###
        konec = time.perf_counter()
        return(konec - zacetek)

bkp1 = BKP([2, 4, 1, 8], [3, 3, 2, 2], [1, 2, 3, 4], 8, True)

print(bkp1.kapital)
print(bkp1.optimalna_resitev())
print(bkp1.casovna_zahtevnost())

        