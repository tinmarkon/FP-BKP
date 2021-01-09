import random

y = 32 #maximalna velikost nahrbtnika, ki jo vodja lahko izbere (~omejitev kapitala)
st_predmetov = [10, 25, 50, 75, 100] #koliko predmetov je na izbiro 

koef1 = [] #koeficienti vodje (seznam koef. koristnosti za posamezen predmet)
koef2 = [] #koeficienti sledilca (seznam koef. koristnosti za posamezen predmet)
utezi_predmetov = [] #utezi predmetov, pri izbiri jih omejuje kapaciteta "y"
for n in st_predmetov:
    for i in range(0, n):
        p = random.randint(1, 30)
        koef1.append(p)
        r = random.randint(1, 30)
        koef2.append(r)
    print(koef1)
    print(koef2)
    for i in range(0, n):
        p = random.randint(1, y)
        utezi_predmetov.append(p)
    print(utezi_predmetov)
    print("")
