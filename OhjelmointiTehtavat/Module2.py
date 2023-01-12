import math

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

print(GramToKilogram(4))

class Luoti:
    Paino = 13.3 #g
    pass

class Naula:
    SuhdeLuotiin = 32
    pass

class Leivaska:
    SuhdeNaulaan = 20 # kg
    pass

Yhteismassa =