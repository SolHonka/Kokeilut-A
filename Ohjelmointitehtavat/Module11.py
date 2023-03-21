import random

#1
class Publication:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print("Name:", self.name)


class Book(Publication):
    def __init__(self, name, author, num_pages):
        super().__init__(name)
        self.author = author
        self.num_pages = num_pages

    def print_info(self):
        super().print_info()
        print("Author:", self.author)
        print("Number of Pages:", self.num_pages)


class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_info(self):
        super().print_info()
        print("Editor:", self.editor)


# Main program
aku_ankka = Magazine("Aku Ankka", "Aki Hyyppä")
hytti_no_6 = Book("Hytti n:o 6", "Rosa Liksom", 200)

aku_ankka.print_info()
hytti_no_6.print_info()

#2


class Car:
    def __init__(self, registration_number, top_speed):
        self.registration_number = registration_number
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_travelled = 0

    def accelerate(self, speed_change):
        self.current_speed = max(0, min(self.top_speed, self.current_speed + speed_change))

    def travel(self, hours):
        self.distance_travelled += self.current_speed * hours


class ElectricCar(Car):
    def __init__(self, registration_number, top_speed, battery_capacity):
        super().__init__(registration_number, top_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, top_speed, fuel_tank_size):
        super().__init__(registration_number, top_speed)
        self.fuel_tank_size = fuel_tank_size


electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.accelerate(100)
gasoline_car.accelerate(120)

for i in range(3):
    electric_car.travel(1)
    gasoline_car.travel(1)

print(f"Electric car distance travelled: {electric_car.distance_travelled} km")
print(f"Gasoline car distance travelled: {gasoline_car.distance_travelled} km")
