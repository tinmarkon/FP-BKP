import random
from Objekt_BKP import BKP

st_predmetov = [10, 25, 50, 75, 100] #koliko predmetov je na izbiro 

def gen_n(n, y): #generiranje seznamov z n predmetov, y ~ max volumen
    koef1 = []
    koef2 = []
    utezi_predmetov = [] #utezi predmetov, pri izbiri jih omejuje kapaciteta "y"
    for i in range(0, n):
        p = random.randint(1, 30)
        koef1.append(p)
        r = random.randint(1, 30)
        koef2.append(r)
        k = random.randint(1, y)
        utezi_predmetov.append(k)
    return koef1, koef2, utezi_predmetov, y

for i in st_predmetov:
    koef1, koef2, utezi, kapital = gen_n(i, 40)
    bkp = BKP(utezi, koef1, koef2, 0, kapital, -1, True)
    bkp.optimalna_resitev()
    
