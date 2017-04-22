#Roxanne Hoggan
import math
import random

def main():
    radius = random.uniform(1.0, 100.0)
    area = circlearea(radius)
    print("The radius is", radius,"and the area of the circle is",\
          area)

def circlearea(x):
    result = math.pi * x ** 2
    return result

main()
