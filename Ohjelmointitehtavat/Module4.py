import random

# 1
CurrentNum = 1

while CurrentNum <= 1000:
    if CurrentNum % 3 == 0:
        print(CurrentNum)
    CurrentNum += 1

#2

while True:
    Inches = float(input("Anna tuumat."))

    if Inches < 0:
        break

    Centimeters = Inches * 2.54

    print(Inches,"tuumaa on",Centimeters,"senttimetriä.")

#3

Numbers = []

while True:
    Input = input("Anna luku:")
    if not Input:
        break
    Numbers.append(float(Input))

if len(Numbers) >= 0:
    print("Pienin luku: ", min(Numbers))
    print("Suurin luku: ", max(Numbers))

#4

NumberToGuess = random.randint(1, 10)

while True:
    PlayerGuess = int(input("Make a guess between 1 and 10: "))

    if not PlayerGuess:
        break

    if PlayerGuess == NumberToGuess:
        print("Oikein!")
        break
    elif PlayerGuess > NumberToGuess:
        print("Liaan korkea!")
    else:
        print("Liian pieni!")

#5

Correct_Username = "python"
Correct_Password = "rules"

Attempts = 0

while Attempts:
    Username = input("Enter your username: ")
    Password = input("Enter your password: ")

    if Username == Correct_Username and Password == Correct_Password:
        print("Pääsy sallittu. Tervetuloa!")
        break
    else:
        print("Väärä käyttäjätunnust tai salasana. Yritä uudelleen.")
        Attempts += 1

    if Attempts >= 5:
        print("Liian monta yritystä. Yritä myöhemmin uudelleen.")
        break

#6

N = int(input("Kuinka monta pistettä arvotaan: "))
n = 0

for i in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        n += 1

pi = 4 * n / N
print("Piin likiarvo on: ", pi)

