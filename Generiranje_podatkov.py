import random
from time import perf_counter
from BKP import BKP

st_predmetov = [10, 25, 50, 75, 100] #V seznamu dolocis stevilo predmetov za problem
st_ponovitev = 100 ### Kolikokrat ponovimo izracun za vsako stevilo predmetov

def gen_n(n, y): #generiranje seznamov z n predmeti, y ~ max volumen
    koef1 = []
    koef2 = []
    utezi_predmetov = [] #utezi predmetov, pri izbiri jih omejuje kapaciteta "y"
    for i in range(0, n):
        p = random.randint(1, 30)
        koef1.append(p)
        r = random.randint(1, 30)
        koef2.append(r)
        k = random.randint(1, y)
        # tako dosezemo, da je vsak predmet lahko vsebovan v nahhrbtniku
        # algoritem deluje tudi za predmete z utezjo > y
        utezi_predmetov.append(k)
    return koef1, koef2, utezi_predmetov, y

seznam_casov = []
for i in st_predmetov:
    fiksni_seznam = []
    for j in range(st_ponovitev):
        koef1, koef2, utezi, kapital = gen_n(i, 40)
        zacetek = perf_counter()
        bkp = BKP(utezi, koef1, koef2, 0, kapital, -1, True)
        bkp.optimalna_resitvev()
        konec = perf_counter()
        fiksni_seznam.append(konec - zacetek)
    seznam_casov.append(fiksni_seznam)

print(len(seznam_casov[0]))        
