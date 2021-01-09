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

# print(gen_n(50, 32))
# i, j, k = gen_n(50, 32)
# print(len(i))

for i in [10, 25, 50, 75, 100]:
    koef1, koef2, utezi, kapital = gen_n(i, 40)
    bkp = BKP(utezi, koef1, koef2, 0, kapital, -1, True)
    print(bkp.optimalna_resitev())
    

#bkp1 = BKP([2, 4, 1, 8], [3, 3, 2, 2], [1, 2, 3, 4], 0, 8, -2, True)
#bkp2 = BKP(utezi_predmetov, koef1, koef2, 0, y, -1, True)
#print(bkp2.optimalna_resitev())