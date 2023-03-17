import random
from prettytable import PrettyTable


# 1-3
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
        print(f"Elevator is on floor {self.current_floor}")

    def go_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
        print(f"Elevator is on floor {self.current_floor}")

    def go_to_floor(self, floor):
        while self.current_floor != floor:
            if self.current_floor < floor:
                self.go_up()
            else:
                self.go_down()


class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.number_of_elevators = number_of_elevators
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(number_of_elevators)]

    def move_elevator(self, elevator_number, destination_floor):
        print(f"Moving elevator {elevator_number} to floor {destination_floor}")
        self.elevators[elevator_number].go_to_floor(destination_floor)

    def fire_alarm(self):
        print("FIRE ALARM! ALL ELEVATORS GO TO THE GROUND FLOOR!")
        for i, elevator in enumerate(self.elevators):
            elevator.go_to_floor(self.bottom_floor)
            print(f"Elevator {i} is on the ground floor.")


# 3 Testing

hotel = Building(0, 10, 2)
hotel.move_elevator(1, 5)
hotel.move_elevator(1, 3)
hotel.move_elevator(0, 7)
hotel.fire_alarm()

# 4

class Car:
    def __init__(self, registration_number):
        self.registration_number = registration_number
        self.top_speed = random.randint(100, 200)
        self.current_speed = 0
        self.distance_travelled = 0

    def accelerate(self, speed_change):
        self.current_speed = max(0, min(self.top_speed, self.current_speed + speed_change))

    def travel(self, hours):
        self.distance_travelled += self.current_speed * hours

    def __str__(self):
        return f"{self.registration_number}\t{self.top_speed} km/h\t{self.current_speed} km/h\t{self.distance_travelled} km"


class Race:
    def __init__(self, name, length, cars):
        self.name = name
        self.length = length
        self.cars = cars
        self.current_hour = 0

    def simulate_hour(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))

        for car in self.cars:
            car.travel(1)

        self.current_hour += 1

    def print_status(self):
        print(f"\nHour {self.current_hour} update:")
        for car in self.cars:
            print(f"{car.registration_number} has traveled {car.distance_travelled} km")

    def print_end(self):
        table = PrettyTable()
        table.field_names = ["Registration Number", "Top Speed", "Current Speed", "Distance Travelled", "Winner"]
        for car in self.cars:
            winner = False
            if car.distance_travelled >= self.length:
                winner = True
            table.add_row([car.registration_number, f"{car.top_speed} km/h", f"{car.current_speed} km/h",
                           f"{car.distance_travelled} km", winner])
        print(table)

    def race_over(self):
        for car in self.cars:
            if car.distance_travelled >= self.length:
                return True
        return False


cars = [Car(f"ABC-{i + 1}") for i in range(10)]
race = Race("Suuri romuralli", 8000, cars)

while not race.race_over():
    race.simulate_hour()
    if race.current_hour % 10 == 0:
        race.print_status()

print("\nThe race is over! Final results:")
race.print_end()
