import random
import math

print(2**-1)

# 1
NumOfDice = int(input("Kuinka monta arpakuutiota heitetään: "))
Sum = 0

for i in range(NumOfDice):
    Sum += random.randint(1, 6)

print("Silmälukujen summa:", Sum)

#2

Numbers = []
while True:
    Number = input("Anna luku (tyhjä lopettaa): ")
    if Number == "":
        break
    Numbers.append(int(Number))

Numbers.sort(reverse=True)

if len(Numbers) >= 5:
    for i in range(5):
        print(Numbers[i])

#3

while True:
    Number = int(input("Anna kokonaisluku: "))

    print(math.sqrt(Number))

    IsPrime = True

    if not Number:
        break

    for i in range(2, int(Number)):
        if Number % i == 0:
            IsPrime = False
            break
    if IsPrime:
        print(Number, "on alkuluku.")
        # break
    else:
        print(Number, "ei ole alkuluku.")

#4

Cities = []

for i in range(5):
    City = input("Anna kaupunki: ")
    Cities.append(City)

for City in Cities:
    print(City)