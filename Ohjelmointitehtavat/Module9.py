import random
from prettytable import PrettyTable

#1

def Clamp(Value, Min, Max):
    if Value < Min: return Min
    if Value > Max: return Max
    return Value
class Car:
    def __init__(self, RegistrationNumber, TopSpeed):
        self.RegistrationNumber = RegistrationNumber
        self.TopSpeed = TopSpeed
        self.CurrentSpeed = 0
        self.DistanceTravelled = 0

    def Accelerate(self, SpeedChange):
        self.CurrentSpeed = Clamp(self.CurrentSpeed + SpeedChange, 0, self.TopSpeed)

    def Travel(self, Time):
        self.DistanceTravelled += self.CurrentSpeed * Time

NewCar = Car("ABC-123", 142)

print("Registration number:", NewCar.RegistrationNumber)
print("Top speed:", NewCar.TopSpeed, "km/h")
print("Current speed:", NewCar.TopSpeed, "km/h")
print("Distance traveled:", NewCar.DistanceTravelled, "km")

#2

NewCar.Accelerate(30)
NewCar.Accelerate(70)
NewCar.Accelerate(50)

print("Current speed:", NewCar.CurrentSpeed, "km/h")

NewCar.Accelerate(-200)

print("Current speed after emergency stop:", NewCar.CurrentSpeed, "km/h")

#4

Cars = []
for i in range(10):
    RegNum = f"ABC-{i+1}"
    TopSpeed = random.randint(100, 200)
    Cars.append(Car(RegNum, TopSpeed))

# Race

print()
print("Race begun!")

Finished = False

while not Finished:
    for CarX in Cars:
        CarX.Accelerate(random.randint(-10, 15))

    for CarX in Cars:
        CarX.Travel(1)


    for CarX in Cars:
        if CarX.DistanceTravelled >= 10000:
            Finished = True
            print()
            print(f"{CarX.RegistrationNumber} reached the finish line!")

            CarStats = PrettyTable()
            CarStats.field_names = ["Registration Number", "Top Speed (km/h)", "Current Speed (km/h)",
                                 "Distance Traveled (km)"]

            CarStats.add_row([CarX.RegistrationNumber, CarX.TopSpeed, CarX.CurrentSpeed, CarX.DistanceTravelled])

            print(CarStats)