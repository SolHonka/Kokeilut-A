import math
import random

# 1. Nimi

MyName = "Salomon"
print("Terve,",input("Anna nimesi: "))





# 2. Ympyrän Pinta-ala


Radius = int(input("Syötä säde: "))
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

Leivaska = float(input("Anna leiväskät:\t"))
Naula = float(input("Anna naulat:\t"))
Luoti = float(input("Anna luodit:\t"))

NaulaPaino = Leivaska * 20 + Naula
LuotiPaino = NaulaPaino * 32 +Luoti
Paino = LuotiPaino * 13.3


print("\nGrammoina: ", int(Paino%1000))
print("Kilogrammoina: ", int(GramToKilogram(Paino)))



# 6. Arvonta

print("\n Kolminumerinen Koodi:")

ThreeNumCode = {}

ThreeNumCode[2] = 3

for i in range(3):
    ThreeNumCode[i] = random.randint(0,9)
    print(ThreeNumCode[i])

print("\n Nelinumerinen Koodi:")

FourNumCode = {}

for i in range(4):
    FourNumCode[i] = random.randint(1,6)
    print(FourNumCode[i])