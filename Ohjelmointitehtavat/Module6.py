import random
import math

#1

def RollDie():
    return random.randint(1, 6)

while True:
    Result = RollDie()
    print(Result)
    if Result == 6:
        break

#2

def RollDie(Sides):
    return random.randint(1, Sides)

MaxSides = int(input("Syätä nopan maximisivut: "))

while True:
    Result = RollDie(MaxSides)
    print(Result)
    if Result == MaxSides:
        break

#3

def GallonsToLiters(Gallons):
    return Gallons * 3.785

while True:
    Gallons = float(input("Syötä bensiinimäärä Gallonoina: "))
    if Gallons <= 0:
        break
    Liters = GallonsToLiters(Gallons)
    print(Gallons, "Gallonaa on ", Liters, "Litraa.")

#4

def SumList(Numbers):
    return sum(Numbers)

Numbers = [1, 2, 3, 4, 5]
print("Numerot: ", Numbers)
Result = SumList(Numbers)
print("Summa: ", Result)

#5

def RemoveOddNumbers(Numbers):
    return [x for x in Numbers if x % 2 == 0]

Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Alkuperäiset numerot: ", Numbers)
Result = RemoveOddNumbers(Numbers)
print("Parilliset numerot: ", Result)

#6

def PizzaUnitPrice(Diameter, Price):
    Area = math.pi * (Diameter/2)**2
    UnitPrice = Price / Area
    return UnitPrice

Result1 = PizzaUnitPrice(float(input("Pizza 1 halkaisia: ")), float(input("Pizza 1 hinta: ")))
Result2 = PizzaUnitPrice(float(input("Pizza 2 halkaisa: ")), float(input("Pizza2 hinta: ")))

if Result1 < Result2:
    print("Pizza 1 on parempi valinta.")
else:
    print("Pizza 2 on parempi valinta.")
