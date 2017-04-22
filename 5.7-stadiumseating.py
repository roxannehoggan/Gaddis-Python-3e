#Roxanne Hoggan
#Complete
#Calculates total ticket revenue based on inputted sales numbers
def main():

    #get amount of ticket sales per class
    a_sales=int(input("Class A tickets sold: "))
    b_sales=int(input("Class B tickets sold: "))
    c_sales=int(input("Class C tickets sold: "))

    #call ticket_revenue on the 3 sales categories and assign result to total
    total = ticket_revenue(a_sales, b_sales, c_sales)

    #print total revenue
    print("Total income generated is $", format(total, ",.2f"), sep="")
    

#calculates ticket revenue for each class and sums them    
def ticket_revenue(num1, num2, num3):
    a_rev = num1 * 20
    b_rev = num2 * 15
    c_rev = num3 * 10
    total = a_rev + b_rev + c_rev
    return total

#call main
main()
