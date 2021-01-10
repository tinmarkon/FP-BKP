import random
import matplotlib.pyplot as plt
from time import perf_counter
from BKP import BKP
from statistics import variance, mean

st_predmetov = [10, 25, 50, 75, 100, 500, 1000] #V seznamu dolocis stevilo predmetov za problem
st_ponovitev = 100 ### Kolikokrat ponovimo izracun za vsako stevilo predmetov

def gen_n(n, y, m): #generiranje seznamov z n predmeti, y ~ max volumen, m ~ max omejitev utezi predmetov
    koef1 = []
    koef2 = []
    utezi_predmetov = [] #utezi predmetov, pri izbiri jih omejuje kapaciteta "y"
    for i in range(0, n):
        p = random.randint(1, m)
        koef1.append(p)
        r = random.randint(1, m)
        koef2.append(r)
        k = random.randint(1, y)
        # tako dosezemo, da je vsak predmet lahko vsebovan v nahhrbtniku
        # algoritem deluje tudi za predmete z utezjo > y
        utezi_predmetov.append(k)
    return koef1, koef2, utezi_predmetov, y

seznam_casov = []
for i in st_predmetov: ### For zanka za vsako stevilo predmetov
    fiksni_seznam = []
    for j in range(st_ponovitev): ### Fiksiramo stevilo predmetov in merimo kako dolgo potrebujemo za objekt 
        koef1, koef2, utezi, kapital = gen_n(i, 40, 32)
        zacetek = perf_counter()
        bkp = BKP(utezi, koef1, koef2, 0, kapital, -1, True)
        bkp.optimalna_resitvev()
        konec = perf_counter()
        fiksni_seznam.append(konec - zacetek)
    seznam_casov.append((mean(fiksni_seznam), variance(fiksni_seznam)))


y = [seznam_casov[i][0] for i in range(len(st_predmetov))] ### Seznam y koordinat - povprecja
var = [seznam_casov[i][1] for i in range(len(st_predmetov))] ### seznam y koordinat - varianca

plt.plot(st_predmetov, y, 'o', st_predmetov, var, 'x')
plt.show()




    
