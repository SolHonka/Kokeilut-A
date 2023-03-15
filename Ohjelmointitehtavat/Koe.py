import math

Maat1 = ["Viro lol"]
Maat2 = ["Helsinki"]
Maat3 = ["Test"]

Maat1.extend(Maat2)
Maat2.extend(Maat3)

print(Maat1)
print((Maat1[-1]))


for a in range(0,10,2):
    print(a)


while True:
    Luku = float(input("Luku"))
    if Luku / 2 == math.floor(Luku / 2):
        print("jee")