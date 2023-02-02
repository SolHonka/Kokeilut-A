import mysql.connector

Connection = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="1234",
        database="flight_game"
    )

#1

def GetAirportInfo(ICAO):
    Cursor = Connection.cursor()

    Cursor.execute(f"SELECT name, name FROM airport WHERE ident='{ICAO}'")
    Airport = Cursor.fetchone()

    Cursor.execute(f"SELECT iso_country, iso_country FROM airport WHERE ident='{ICAO}'")
    Location = Cursor.fetchone()

    if Airport and Location:
        print(f"Lentokentän nimi: {Airport[0]}")
        print(f"Maa: {Location[0]}")
    else:
        print(f"Lentokenttää ei löytynyt koodilla: {ICAO}")

    Cursor.close()

while True:
    ICAO = input("Anna ICAO koodi: ")
    if ICAO == "":
        break
    else:
        GetAirportInfo(ICAO)

#2


while True:
    Country = input("Anna maakoodi: ")
    if Country == "":
        break
    else:
        print("test")

        Cursor = Connection.cursor()
        Cursor.execute(f"SELECT type, type FROM airport WHERE iso_country='{Country}'")
        Result = Cursor.fetchall()

        Types = {}

        for _,Type in Result:
            if Type not in Types:
                Types[Type] = 0
            Types[Type] += 1

        for Type,Amount in Types.items():
            print(Type, Amount)

        Cursor.close()

#3