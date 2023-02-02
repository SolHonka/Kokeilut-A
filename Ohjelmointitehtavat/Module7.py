#1

Seasons = {
    "Talvi": [12,1,2],
    "Kevät": [3,4,5],
    "Kesä": [6,7,8],
    "Syksy": [9,10,11]
}
while True:
    MonthNumber = int(input("Anna kuu (1-12): "))
    if MonthNumber < 1 or MonthNumber > 12:
        break

    for Season,Months in Seasons.items():
        if MonthNumber in Months:
            print(f"Kuukauden {MonthNumber} vuodenaika on {Season}")



#2

Names = set()

while True:
    Name = input("Syötä nimi: ")
    if Name == "":
        break
    if Name in Names:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        Names.add(Name)

print("Syötetyt nimet:")
for Name in Names:
    print(Name)

#3

Airports = {}
while True:
    print("1. Syötä uusi lentoasema")
    print("2. Hae lentoaseman tiedot")
    print("3. Lopeta")
    Choice = input("Valitse toiminto (1-3): ")

    if Choice == "1":
        ICAO = input("Syötä ICAO-koodi: ")
        Name = input("Syötä lentoaseman nimi: ")
        Airports[ICAO] = Name
    elif Choice == "2":
        ICAO = input("Syötä ICAO-koodi: ")
        if ICAO in Airports:
            print("Lentoaseman nimi:", Airports[ICAO])
        else:
            print("Lentoasemaa ei löytynyt.")
    elif Choice == "3":
        break
    else:
        print("Virheellinen valinta.")
