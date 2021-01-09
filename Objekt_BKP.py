import time
from BKP import generiranjeTabel, iskanjeResitvev, prvi_predmeti

class BKP:

    def __init__(self, teze, s_prihodek, i_prihodek, s_kapital, kapital, cenaEnote, optimisticen):
        self.teze = teze
        self.s_prihodek = s_prihodek
        self.i_prihodek = i_prihodek
        self.s_kapital = s_kapital
        self.kapital = kapital
        self.cenaEnote = cenaEnote
        self.optimisticen = True

    def optimalna_resitev(self):
        zacetek = time.perf_counter()
        inv, sle = generiranjeTabel(self.teze, self.s_prihodek, self.i_prihodek, self.kapital, self.optimisticen)
        resitev = iskanjeResitvev(inv, sle, self.s_kapital, self.kapital, self.cenaEnote, self.teze, self.i_prihodek, self.s_prihodek)
        konec = time.perf_counter()
        print("Optimalna resitev danega problema: {}".format(resitev)) #uporabimo funkcijo iz BKP.py
        print("Casovna zahtevnost: {}".format(konec - zacetek))
        return(resitev)

# Testni primeri
#bkp1 = BKP([2, 4, 1, 8], [3, 3, 2, 2], [1, 2, 3, 4], 0, 8, -2, True)
#bkp2 = BKP([1, 2, 3, 4], [4,5,10,15], [5,1,1,1], 1, 4, -1, True)
#bkp3 = BKP([5,3,2,1], [1, 1, 1, 1], [3,5,1,9], 0, 6, -2, True)




        