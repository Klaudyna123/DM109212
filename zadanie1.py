import random

def wektor7():
    wektor_losowy = []
    for i in range(7):
        liczba_los = random.uniform(0,99)
        wektor_losowy.append(liczba_los)
    return wektor_losowy
def random_wektor(n):
    wektor_losowy = []
    for i in range (n):
        liczba_los = random.uniform(0,99)
        wektor_losowy.append(liczba_los)
    return wektor_losowy

wektor_7 = wektor7()
wektor_14 = random_wektor(14)

print("Wektor z 7 elementami:")
print(wektor_7)
print("Wektor z 14 elementami:")
print(wektor_14)