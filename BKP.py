### Vhodni podatki: teze izdelkov (seznam), s_prihodek (prihodek sledilca - seznam), i_prihodek(prihodek investitorja -seznam) 
# kapital (stevilo), optimisticen (T/F) ###

def generiranjeTabel(teze, s_prihodek, i_prihodek, kapital, optimisticen = True):
    sledilec = list()
    investitor = list()
    zacetni_predmet_s, zacetni_predmet_i = prvi_predmeti(kapital, s_prihodek, i_prihodek, teze)
    sledilec.append(zacetni_predmet_s)
    investitor.append(zacetni_predmet_i)
    for k in range(1, len(teze)):
        fiksni_sledilec = list()
        fiksni_investitor = list()
        for j in range(0, kapital + 1): ###TODO Kaj ce kapital ni celo stevilo?
            if (j < teze[k]):  ###TODO ali lahko skrajsam kodo tako da bo manj if stavkov??
               fiksni_investitor.append(investitor[-1][j])
               fiksni_sledilec.append(sledilec[-1][j])
            else: 
                maksimalna_sledilec = max(sledilec[-1][j], sledilec[-1][j - teze[k]] + s_prihodek[k])
                fiksni_sledilec.append(maksimalna_sledilec)
                if (sledilec[-1][j] != sledilec[-1][j - teze[k]] + s_prihodek[k]):
                    if fiksni_sledilec == sledilec[-1][j]:
                        fiksni_investitor.append(investitor[-1][j])
                    else: ### Ali moram tukaj pisat pogoj? A obstaja situacija ko se ne zgodi nujno drugo?
                        fiksni_investitor.append(investitor[-1][j - teze[k]] + i_prihodek[k])  

                else:
                    if optimisticen:
                        fiksni_investitor.append(max(investitor[-1][j], investitor[-1][j - teze[k]] + i_prihodek[k]))
                    else:
                        fiksni_investitor.append(min(investitor[-1][j], investitor[-1][j - teze[k]] + i_prihodek[k]))
        investitor.append(fiksni_investitor)
        sledilec.append(fiksni_sledilec)
    return investitor, sledilec
    
def prvi_predmeti(kapital, s_prihodek, i_prihodek, teze): ## To lahko vstavim v prvo funkcijo??
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


teze = [5,3,2,1]
s_prih = [1,1,1,1]
i_prih = [3,5,1,9]
kap = 6

test = generiranjeTabel(teze, s_prih, i_prih, kap)