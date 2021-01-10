class BKP:
    def __init__(self, teze, s_prihodek, i_prihodek, s_kapital, kapital, cena_enote, optimisticen):
        self.teze = teze
        self.s_prihodek = s_prihodek
        self.i_prihodek = i_prihodek
        self.s_kapital = s_kapital
        self.kapital = kapital
        self.cena_enote = cena_enote
        self.optimisticen = True

    def prvi_predmeti(self):
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
                        if fiksni_sledilec == sledilec[-1][j]:
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

    def iskanje_resitvev(self):
        investitorjeva_matrika, sledilceva_matrika = self.generiranje_tabel()
        invResitev = investitorjeva_matrika[-1]
        zasluzek = 0
        optKapital = 0
        vmesniKapital = 0
        predmeti = list()
        for i in range(self.s_kapital, self.kapital + 1):
            if (zasluzek < invResitev[i] + i * self.cena_enote):
                zasluzek = invResitev[i] + i * self.cena_enote
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
        return predmeti[::-1], optKapital