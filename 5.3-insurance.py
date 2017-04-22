#Roxanne Hoggan
#Complete
#Calculates insurance minimum from building cost

#This is the main function
def main():
    #Get the cost of the replacement building
    bldg_cost=float(input("Enter the cost to replace the building: $"))
    #Call ins_min to calculate the insurance cost
    calc_ins(bldg_cost)

#Calculate 80% of building cost to find insurance minimum
def calc_ins(bldg_cost):
    ins_min = bldg_cost * .80
    print("The minimum amount of insurance is $", \
          format(ins_min, ".2f"), sep="")

#call the main function
main()

    
