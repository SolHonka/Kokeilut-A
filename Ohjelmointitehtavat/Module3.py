#1

KalanPituus = float(input("Mikä on kalan pituus?"))

if KalanPituus <= 37:
    print("Kala on alamittainen!", 37-KalanPituus, "cm liian pieni!")


#2

Luokat = {
    "LUX": "on parvekkeellinen hytti yläkannella.",
    "A": "on ikkunallinen hytti autokannen yläpuolella.",
    "B": "on ikkunaton hytti autokannen yläpuolella.", 
    "C": "on ikkunaton hytti autokannen alapuolella."
}
Luokka = str.upper(input("Anna laivan hyttiluokka:"))

if not Luokat[Luokka]:
    print(Luokka, "on virheellinne luokka!")
else:
    print(Luokka, Luokat[Luokka])   

#3

Sukupuoli = str.lower(input("Anna henkilön sukupuoli:"))
Hemoglobiini = float(input("Anna henkilön hemoglobiiniarvo:"))

Hemoglobiiniarvot = {
    "mies":range(134,195),
    "nainen":range(117,175)
}

if Hemoglobiiniarvot[Sukupuoli]:
    ArvoPrint = "Henkilön hemoglobiini arvo on"

    if Hemoglobiini in Hemoglobiiniarvot[Sukupuoli]:
        print(ArvoPrint, "normaali.")
    elif Hemoglobiini > max(Hemoglobiiniarvot[Sukupuoli]):
        print(ArvoPrint, "liiaan korkea!")
    elif Hemoglobiini < min(Hemoglobiiniarvot[Sukupuoli]):
        print(ArvoPrint, "liian alhainen!")
else:
    print("Virheellinen sukupuoli!")


#4

Vuosi = int(input("Anna vuosi:"))

if Vuosi % 4 == 0 and (Vuosi % 100 != 0 or Vuosi % 400 == 0):
    print(Vuosi, "on karkausvuosi!")
else:
    print(Vuosi, "ei ole karkausvuosi!")