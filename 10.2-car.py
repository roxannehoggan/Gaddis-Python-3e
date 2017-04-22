#Roxanne Hoggan
#Complete
#Creates car object, calls its various methods

import car

def main():
    yearmodel = input("Year model: ")
    make = input("Make: ")
    speed = 0
    Car = car.Car(yearmodel, make, speed)
    print("*"*10)
    for count in range(1,6):
        Car.accelerate()
        print(Car.get_speed())
    print("*"*10)
    for count in range(1,6):
        Car.brake()
        print(Car.get_speed())

main()
