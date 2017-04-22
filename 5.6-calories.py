#Roxanne Hoggan
#Complete
#Calculates calories from inputted amt of fat and inputted amt of carbs

def main():
    #get values for fat and carbs
    fat = int(input("Daily fat consumption in grams: "))
    carbs = int(input("Daily carb consumption in grams: "))
    
    #call calc_fat to determine calories from fat
    calorie_fat = calc_fat(fat)

    #call calc_carbs to determine calories from carbs
    calorie_carbs = calc_carbs(carbs)

    #output original inputted values
    print("You consume ", fat, " grams of fat per day and ", carbs,\
          " grams of carbs.", sep="")
    
    #output calorie calculations
    print("This is equal to ", calorie_fat, " calories from fat, and ",\
          calorie_carbs, " calories from carbs.", sep="")


#calculate calories from fat
def calc_fat(x):
    result = x * 9
    return result

#calculate calories from carbs
def calc_carbs(x):
    result = x * 4
    return result

#call main
main()
