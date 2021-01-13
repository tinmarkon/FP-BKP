class BKP:
    def __init__(self, teze, s_prihodek, i_prihodek, s_kapital, kapital, cena_enote, optimisticen):
        """ Dodani zacetni parametri """
        self.teze = teze
        self.s_prihodek = s_prihodek
        self.i_prihodek = i_prihodek
        self.s_kapital = s_kapital
        self.kapital = kapital
        self.cena_enote = cena_enote
        self.optimisticen = True

    def prvi_predmeti(self):
        """ Metoda vraca dva seznama, kjer gledamo samo ali lahko v nahrbtnik damo prvi predmet """
        seznam_sledilec = list()
        seznam_investitor = list()
        for j in range(0, self.kapital + 1):
            if (j >= self.teze[0]):
                seznam_sledilec.append(self.s_prihodek[0])
                seznam_investitor.append(self.i_prihodek[0])
            else:
                seznam_sledilec.append(0)
                seznam_investitor.append(0)
        return seznam_sledilec, seznam_investitor

    def generiranje_tabel(self):
        """ Metoda vraca dva seznama, za sledilca in investitorja, za vse mozne delne vsote in po vseh kapitalih od 0 do y  (Forward phase) """
        sledilec = list()
        investitor = list()
        zacetni_predmet_s, zacetni_predmet_i = self.prvi_predmeti()
        sledilec.append(zacetni_predmet_s)
        investitor.append(zacetni_predmet_i)
        for k in range(1, len(self.teze)):
            fiksni_sledilec = list()
            fiksni_investitor = list()
            for j in range(0, self.kapital + 1):
                if (j < self.teze[k]):
                    fiksni_investitor.append(investitor[-1][j])
                    fiksni_sledilec.append(sledilec[-1][j])
                else:
                    maksimalna_sledilec = max(
                        sledilec[-1][j], sledilec[-1][j - self.teze[k]] + self.s_prihodek[k])
                    fiksni_sledilec.append(maksimalna_sledilec)
                    if (sledilec[-1][j] != sledilec[-1][j - self.teze[k]] + self.s_prihodek[k]):
                        if maksimalna_sledilec == sledilec[-1][j]:
                            fiksni_investitor.append(investitor[-1][j])
                        else:
                            fiksni_investitor.append(
                                investitor[-1][j - self.teze[k]] + self.i_prihodek[k])
                    else:
                        if self.optimisticen:
                            fiksni_investitor.append(
                                max(investitor[-1][j], investitor[-1][j - self.teze[k]] + self.i_prihodek[k]))
                        else:
                            fiksni_investitor.append(
                                min(investitor[-1][j], investitor[-1][j - self.teze[k]] + self.i_prihodek[k]))
            investitor.append(fiksni_investitor)
            sledilec.append(fiksni_sledilec)
        return investitor, sledilec

    def optimalna_resitvev(self):
        """ Metoda vraca par x* in y*, ki nam pove katere predmete damo v nahrbtnik in kak kapital je optimalen (Backtracking phase) """
        investitorjeva_matrika, sledilceva_matrika = self.generiranje_tabel()
        inv_resitev = investitorjeva_matrika[-1]
        zasluzek = 0
        optKapital = 0
        vmesniKapital = 0
        predmeti = list()
        for i in range(self.s_kapital, self.kapital + 1):
            if (zasluzek < inv_resitev[i] + i * self.cena_enote):
                    zasluzek = inv_resitev[i] + i * self.cena_enote
                    optKapital = i
                    vmesniKapital = i  
        for j in range(len(sledilceva_matrika) - 1, 0, -1):
            if sledilceva_matrika[j - 1][vmesniKapital] != sledilceva_matrika[j - 1][vmesniKapital - self.teze[j]] + self.s_prihodek[j]:
                if sledilceva_matrika[j][vmesniKapital] == sledilceva_matrika[j - 1][vmesniKapital]:
                    predmeti.append(0)
                else:
                    predmeti.append(1)
                    vmesniKapital = vmesniKapital - self.teze[j]
            else:
                if investitorjeva_matrika[j][vmesniKapital] == investitorjeva_matrika[j-1][vmesniKapital]:
                    predmeti.append(0)
                else:
                    predmeti.append(0)
                    vmesniKapital = vmesniKapital - self.teze[j]
        if sledilceva_matrika[0][vmesniKapital] == 0:
            predmeti.append(0)
        else:
            predmeti.append(1)
        if(self.cena_enote <= 0):
            return predmeti[::-1], optKapital
        else:
            maksimum = 0
            for j in range(self.s_kapital, self.kapital):
                if maksimum < inv_resitev[j] + self.cena_enote * (j + 1):
                    maksimum = inv_resitev[j] + self.cena_enote * (j + 1)
            if maksimum <= inv_resitev[self.kapital] + self.cena_enote * self.kapital:
                return (predmeti[::-1], self.kapital)
            else:
                print("BKP nima optimalne resitve")
                return None  

### PRIMERI ###

# bkp1 = BKP([2, 4, 1, 8], [3, 3, 2, 2], [1, 2, 3, 4], 0, 8, -2, True)
# bkp_primer1 = BKP([1, 2, 3, 4], [4,5,10,15], [5,1,1,1], 1, 4, 1, True)
# bkp_primer2 = BKP([5,3,2,1], [1, 1, 1, 1], [3,5,1,9], 0, 6, -2, True)

# print(bkp_primer1.optimalna_resitvev())
# print(bkp_primer2.optimalna_resitvev())
