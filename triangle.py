#Roxanne Hoggan
#Complete
#Calculates area or hypotnuse of a triangle
#When called from main function in separate file

#calculates area given inputted data
def area():
    height = float(input("Enter the height of the triangle: "))
    base = float(input("Enter the base of the triangle: "))
    result = height * base * 0.5
    return result


#calculates hypotenuse given inputted data 
def hypotenuse():
    side1 = float(input("Enter the length of the first side of the triangle: "))
    side2 = float(input("Enter the length of the second side of the triangle: "))
    result = math.hypot(side1, side2)
    return result
