import math
import random

# 1. Nimi

MyName = "Salomon"
print("Terve,",MyName)





# 2. Ympyrän Pinta-ala

Radius = 2
Circumference = math.pi*Radius**2

print(Circumference)





# 3.

Base = 2
Height = 3

Perimeter = 2 * (Base + Height)
Area = Base * Height

print("Suorakulmion piiri on ", Perimeter)
print("Suorakulmion pinta-ala on ", Area)





# 4. Summa, Tulo & Keskiarvo

Numbers = {
    4,
    6,
    2,
}

Summa = sum(Numbers)
Tulo = 1
Keskiarvo = 0

for Num in Numbers:
    Keskiarvo += Num
Keskiarvo /= len(Numbers)

for Num in Numbers:
    Tulo *= Num

print(Summa)
print(Tulo)
print(Keskiarvo)





# 5. Massalaskenta

def GramToKilogram(Grams):
    return Grams*0.001

class Luoti:
    Weight = 13.3 #g
    Quantity = 13.5
    pass

class Naula:
    RatioToLuoti = 32
    Quantity = 9
    Weight = 0
    pass

class Leivaska:
    RatioToNaula = 20
    Quantity = 3
    Weight = 0
    pass

Naula.Weight = Luoti.Weight * Naula.RatioToLuoti
Leivaska.Weight = Naula.Weight * Leivaska.RatioToNaula

GramSum = Luoti.Weight * Luoti.Quantity + Naula.Weight * Naula.Quantity + Leivaska.Weight * Leivaska.RatioToNaula

print(Leivaska.Weight)

print(GramSum)






# 6. Arvonta

print()
print("Kolminumerinen Koodi:")

ThreeNumCode = {}

ThreeNumCode[2] = 3

for i in range(3):
    ThreeNumCode[i] = random.randint(0,9)
    print(ThreeNumCode[i])


print()
print("Nelinumerinen Koodi:")

FourNumCode = {}

for i in range(4):
    FourNumCode[i] = random.randint(1,6)
    print(FourNumCode[i])