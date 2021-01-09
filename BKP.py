def generiranjeTabel(teze, s_prihodek, i_prihodek, kapital, optimisticen = True):
    sledilec = list()
    investitor = list()
    zacetni_predmet_s, zacetni_predmet_i = prvi_predmeti(kapital, s_prihodek, i_prihodek, teze)
    sledilec.append(zacetni_predmet_s)
    investitor.append(zacetni_predmet_i)
    for k in range(1, len(teze)):
        fiksni_sledilec = list()
        fiksni_investitor = list()
        for j in range(0, kapital + 1): 
            if (j < teze[k]):  
               fiksni_investitor.append(investitor[-1][j])
               fiksni_sledilec.append(sledilec[-1][j])
            else: 
                maksimalna_sledilec = max(sledilec[-1][j], sledilec[-1][j - teze[k]] + s_prihodek[k])
                fiksni_sledilec.append(maksimalna_sledilec)
                if (sledilec[-1][j] != sledilec[-1][j - teze[k]] + s_prihodek[k]):
                    if fiksni_sledilec == sledilec[-1][j]:
                        fiksni_investitor.append(investitor[-1][j])
                    else: 
                        fiksni_investitor.append(investitor[-1][j - teze[k]] + i_prihodek[k])  

                else:
                    if optimisticen:
                        fiksni_investitor.append(max(investitor[-1][j], investitor[-1][j - teze[k]] + i_prihodek[k]))
                    else:
                        fiksni_investitor.append(min(investitor[-1][j], investitor[-1][j - teze[k]] + i_prihodek[k]))
        investitor.append(fiksni_investitor)
        sledilec.append(fiksni_sledilec)
    return investitor, sledilec
    
def prvi_predmeti(kapital, s_prihodek, i_prihodek, teze):
    seznam_sledilec = list()
    seznam_investitor = list()
    for j in range(0, kapital + 1):
        if (j >= teze[0]):
            seznam_sledilec.append(s_prihodek[0])
            seznam_investitor.append(i_prihodek[0])
        else:
            seznam_sledilec.append(0)
            seznam_investitor.append(0)
    return seznam_sledilec, seznam_investitor

def iskanjeResitvev(investitorjevaMatrika, sledilcevaMatrika, sKapital, kapital, cenaEnote, teze, i_prih, s_prih): 
    invResitev = investitorjevaMatrika[-1] 
    zasluzek = 0
    optKapital = 0
    vmesniKapital = 0
    predmeti = list()
    for i in range(sKapital, kapital + 1):  
        if (zasluzek < invResitev[i] + i * cenaEnote): 
            zasluzek = invResitev[i] + i * cenaEnote
            optKapital = i
            vmesniKapital = i
    for j in range(len(sledilcevaMatrika) - 1, 0, -1):
        if sledilcevaMatrika[j - 1][vmesniKapital] != sledilcevaMatrika[j - 1][vmesniKapital - teze[j]] + s_prih[j]:
            if sledilcevaMatrika[j][vmesniKapital] == sledilcevaMatrika[j - 1][vmesniKapital]:
                predmeti.append(0)
            else:
                predmeti.append(1)
                vmesniKapital = vmesniKapital - teze[j]
        else:
            if investitorjevaMatrika[j][vmesniKapital] == investitorjevaMatrika[j-1][vmesniKapital]:
                predmeti.append(0)
            else:
                predmeti.append(0)
                vmesniKapital = vmesniKapital - teze[j]
    if sledilcevaMatrika[0][vmesniKapital] == 0:
        predmeti.append(0)
    else:
        predmeti.append(1)
    return predmeti[::-1], optKapital

