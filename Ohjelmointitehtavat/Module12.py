
import requests

#1

try:
    response = requests.get("https://api.chucknorris.io/jokes/random")
    if response.status_code == 200:
        joke = response.json()["value"]
        print(joke)
    else:
        print("Haku epäonnistui!")
except:
    print("Virhe!")

#2

city = input("Anna paikkakunnan nimi: ")

api_key = "7b6ef06aba08f13d8644a7378c791517"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
print(url)

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]

        print(f"Sääpaikkakunnalla {city}: {description}, lämpötila: {temperature - 273.15} C")
    else:
        print("Virhe!")
except:
    print("Haku epäonnistui!")


