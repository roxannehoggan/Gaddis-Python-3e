#Roxanne Hoggan
#Complete
#Presents user with a menu function that provides two options:
#Calculating hypotnuse or area or a triangle
#Imports functions from a separate file

#imports the triangle.py file with the area and hypot functions
import triangle

#this is the main function
def main():
    #sets keepgoing menu loop to continue as long as it == "yes"
    keepgoing = "yes"
    while keepgoing == "yes":
        #calls the menu function
        print_menu()
        choice = input("Enter your choice 1-3: ")

        if choice == "1":
            #calls area function from triangle.py and returns its result
            result = triangle.area()
            print("The area is", result)
        elif choice == "2":
            #calls hypot function from triangle.py and returns its result 
            result = triangle.hypotenuse()
            print("The hypotenuse is", result)
        elif choice == "3":
            print("Goodbye!")
            #ends menu loop
            keepgoing="no"
        else:
            #validates input
            print("Invalid input.")
            choice = input("Enter your choice 1-3:")

def print_menu():
    print("Press 1 to calculate area.")
    print("Press 2 to calculate hypotenuse")
    print("Press 3 to quit.")
    
main()
