### Vhodni podatki: teže izdelkov (seznam), s_prihodek (prihodek sledilca - seznam), i_prihodek(prihodek investitorja -seznam) 
# kapital (število), optimisticen (T/F) ###

### TODO naredi objekt z vsemi temi podatki

def generiranjeTabel(teže, s_prihodek, i_prihodek, kapital, optimisticen = True):
    sledilec = list()
    investitor = list()
    zacetni_predmet_s, zacetni_predmet_i = prvi_predmeti(kapital, s_prihodek, i_prihodek, teže)
    sledilec.append(zacetni_predmet_s)
    investitor.append(zacetni_predmet_i)
    for k in range(1, len(teže)):
        fiksni_sledilec = list()
        fiksni_investitor = list()
        for j in range(0, kapital + 1): 
            if (j < teže[k]):  ###TODO ali lahko skrajšam kodo tako da bo manj if stavkov??
               fiksni_investitor.append(investitor[-1][j])
               fiksni_sledilec.append(sledilec[-1][j])
            else: 
                maksimalna_sledilec = max(sledilec[-1][j], sledilec[-1][j - teže[k]] + s_prihodek[k])
                fiksni_sledilec.append(maksimalna_sledilec)
                if (sledilec[-1][j] != sledilec[-1][j - teže[k]] + s_prihodek[k]):
                    if fiksni_sledilec == sledilec[-1][j]:
                        fiksni_investitor.append(investitor[-1][j])
                    else: ### Ali moram tukaj pisat pogoj? A obstaja situacija ko se ne zgodi nujno drugo?
                        fiksni_investitor.append(investitor[-1][j - teže[k]] + i_prihodek[k])  

                else:
                    if optimisticen:
                        fiksni_investitor.append(max(investitor[-1][j], investitor[-1][j - teže[k]] + i_prihodek[k]))
                    else:
                        fiksni_investitor.append(min(investitor[-1][j], investitor[-1][j - teže[k]] + i_prihodek[k]))
        investitor.append(fiksni_investitor)
        sledilec.append(fiksni_sledilec)
    return investitor, sledilec
    
def prvi_predmeti(kapital, s_prihodek, i_prihodek, teže): ## To lahko vstavim v prvo funkcijo??
    seznam_sledilec = list()
    seznam_investitor = list()
    for j in range(0, kapital + 1):
        if (j >= teže[0]):
            seznam_sledilec.append(s_prihodek[0])
            seznam_investitor.append(i_prihodek[0])
        else:
            seznam_sledilec.append(0)
            seznam_investitor.append(0)
    return seznam_sledilec, seznam_investitor

def iskanjeResitvev(investitorjevaMatrika, sledilcevaMatrika, sKapital, kapital, cenaEnote, teze, i_prih, s_prih): #To bi bila lahko funkcija optimalni y
    invResitev = investitorjevaMatrika[-1] ## Obe matriki lahko zgeneriram znotraj funkcije tako da kličem prvo?
    sleResitev = sledilcevaMatrika[-1]
    zasluzek = 0
    optKapital = 0
    vmesniKapital = 0
    predmeti = list()
    for i in range(sKapital, kapital + 1):  #TODO naredi transformacijo na celem seznamu in in najdo max element in njegov index
        if (zasluzek < invResitev[i] + i * cenaEnote): #Kaj se zgodi v primeru da sta enaka??
            zasluzek = invResitev[i] + i * cenaEnote
            optKapital = i
            vmesniKapital = i
    for j in range(len(sledilcevaMatrika) - 1, 1, -1):
        if sledilcevaMatrika[j - 1][vmesniKapital] != sledilcevaMatrika[j - 1][vmesniKapital - teze[j]] + s_prih[j]:
            if sledilcevaMatrika[j][vmesniKapital] == sledilcevaMatrika[j - 1][vmesniKapital]:
                predmeti.append(0)
        if sledilcevaMatrika[j][vmesniKapital] == sledilcevaMatrika[j - 1][vmesniKapital - teze[j]] + s_prih[j]:
                predmeti.append(1)
                vmesniKapital = vmesniKapital - teze[j]
        else:
            if investitorjevaMatrika[j][vmesniKapital] == investitorjevaMatrika[j-1][vmesniKapital]:
                predmeti.append(0)
            if investitorjevaMatrika[j][vmesniKapital] == investitorjevaMatrika[j-1][vmesniKapital - teze[j]] + i_prih[j]:
                predmeti.append(0)
                vmesniKapital = vmesniKapital - teze[j]
    if sledilcevaMatrika[0][vmesniKapital] == 0:
        predmeti.append(0)
    else:
        predmeti.append(1)
    return predmeti[::-1], optKapital



t = -2
teze = [5,3,2,1]
s_prih = [1,1,1,1]
i_prih = [3,5,1,9]
kap = 6

inv, sle = generiranjeTabel(teze, s_prih, i_prih, kap)

print(iskanjeResitvev(inv, sle, 0, kap, t, teze, i_prih, s_prih ))

