import random
from time import perf_counter
from BKP import BKP
from statistics import variance, mean
import matplotlib.pyplot as plt

st_predmetov = [10, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750] # Izbor vseh moznih stevil predmetov, ki sva jih izbrala za testiranje
st_ponovitev = 3 # Parameter, ki pove kolikokrat naredimo objekt z nakljucnimi tezami, koristnostmi za vsak izbor stevila predmetov



def gen_n(n, y, m): # Generiranje seznamov z n predmeti, y kapitala in m kot zgornja izbira koeficientov teze in koristnosti 
    koef1 = []
    koef2 = []
    utezi_predmetov = [] # Utezi predmetov, pri izbiri jih omejuje kapaciteta "y"
    for i in range(0, n):
        p = random.randint(1, m)
        koef1.append(p)
        r = random.randint(1, m)
        koef2.append(r)
        k = random.randint(1, y)
        utezi_predmetov.append(k)
    return koef1, koef2, utezi_predmetov, y

def casovna_odvisnost(y, m): 
    seznam_casov = []
    for i in st_predmetov: # For zanka za vsako stevilo predmetov
        fiksni_seznam = []
        for j in range(st_ponovitev): # Fiksiramo stevilo predmetov in merimo kako dolgo potrebujemo za objekt 
            koef1, koef2, utezi, kapital = gen_n(i, y, m)
            zacetek = perf_counter() 
            bkp = BKP(utezi, koef1, koef2, 0, kapital, -1, True) # Naredimo objekt
            bkp.optimalna_resitvev() # Izracunamo optimalno resitev
            konec = perf_counter()
            fiksni_seznam.append(konec - zacetek) # V seznam za fiksno stevilo predmetov vstavimo nov cas algoritma
        seznam_casov.append((mean(fiksni_seznam), variance(fiksni_seznam))) # V splosnejsi seznam vrnemo povprecje vseh seznam za fiksno stevilo predmetov
    return seznam_casov


primer_1 = casovna_odvisnost(40, 40) 
primer_2 = casovna_odvisnost(80, 80)
primer_3 = casovna_odvisnost(100, 100)
primer_4 = casovna_odvisnost(150, 150)
primer_5 = casovna_odvisnost(60, 60)

y_1  = [primer_1[i][0] for i in range(len(st_predmetov))]
y_2 = [primer_2[i][0] for i in range(len(st_predmetov))]
y_3 = [primer_3[i][0] for i in range(len(st_predmetov))]
y_4 = [primer_4[i][0] for i in range(len(st_predmetov))]
y_5 = [primer_5[i][0] for i in range(len(st_predmetov))]

var_1 = [primer_1[i][1] for i in range(len(st_predmetov))]
var_2 = [primer_2[i][1] for i in range(len(st_predmetov))]
var_3 = [primer_3[i][1] for i in range(len(st_predmetov))]
var_4 = [primer_4[i][1] for i in range(len(st_predmetov))]
var_5 = [primer_5[i][1] for i in range(len(st_predmetov))]

z_1 = [casovna_odvisnost(40, 10)[i][0] for i in range(len(st_predmetov))] # Gledava primere ko so teze zagotovo manjse od skupnega kapitala
z_2 = [casovna_odvisnost(40, 80)[i][0] for i in range(len(st_predmetov))] # Gledava primere ko so teze lahko tudi vecje kot je kapital




### PLOT 1 ###
plt.plot(st_predmetov, y_1, label = "y = 40")
plt.plot(st_predmetov, y_2, label = "y = 80")
plt.plot(st_predmetov, y_3, label = "y = 100")
plt.plot(st_predmetov, y_4, label = "y = 150")
plt.plot(st_predmetov, y_5, label = "y = 60")
plt.xlabel("Stevilo predmetov (n)")
plt.ylabel("Povprecno izvajanje programa (s)")
plt.legend()
plt.show()
### 

### PLOT 2 ###
plt.plot(st_predmetov, var_1, label = "y = 40")
plt.plot(st_predmetov, var_2, label = "y = 80")
plt.plot(st_predmetov, var_3, label = "y = 100")
plt.plot(st_predmetov, var_4, label = "y = 150")
plt.plot(st_predmetov, var_5, label = "y = 60")
plt.xlabel("Stevilo predmetov (n)")
plt.ylabel("Varianca izvajanja programa (s)")
plt.legend()
plt.show()
###

### PLOT 3 ###
plt.plot(st_predmetov, y_1, label="m = 40")
plt.plot(st_predmetov, z_1, label="m = 10")
plt.plot(st_predmetov, z_2, label="m = 80")
plt.xlabel("Stevilo predmetov (n)")
plt.ylabel("Povprecno izvajanje programa (s)")
plt.legend()
plt.show()
###


