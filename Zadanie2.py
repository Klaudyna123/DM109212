import random
import numpy

def random_wektor(n):
    wektor_losowy = []
    for i in range (n):
        liczba_los = random.normalvariate(4,2)
        wektor_losowy.append(liczba_los)
    return wektor_losowy


wektor_100 = random_wektor(100)

srednia=numpy.mean(wektor_100)
odchyl=numpy.std(wektor_100)


print(wektor_100)
print(srednia)
print(odchyl)