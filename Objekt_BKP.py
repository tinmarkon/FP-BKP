class BKP:

    def __init__(self, teze, s_prihodek, i_prihodek, kapital, optimisticen):
        self.teze = teze
        self.s_prihodek = s_prihodek
        self.i_prihodek = i_prihodek
        self.kapital = kapital
        self.optimisticen = True

    def optimalna_resitev(self):
        print("resitev, ki jo vrne funkcija") #uporabimo funkcijo v BKP.py

    def casovna_zahtevnost(self):
        print("koliko casa porabi algoritem")

bkp1 = BKP([2, 4, 1, 8], [3, 3, 2, 2], [1, 2, 3, 4], 8, True)

print(bkp1.kapital)
print(bkp1.optimalna_resitev())
print(bkp1.casovna_zahtevnost())

        