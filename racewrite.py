#Roxanne Hoggan
#Complete
#Recieves horse names and purse amt from input, writes results to a new txt file

def main():
    try:
        race_file = open("horse_list.txt", "w")
        again = "y"
        while again == "y" or again == "Y":
            purse = 0
            name = input("Enter the horse's name: ")
            while purse == 0:
                try:
                    purse = float(input("Enter the amount earned: "))
                except ValueError:
                    print("Not a number!")
            while purse < 0:
                print("Enter a positive number!")
                purse = float(input("Enter the amount earned: "))
            race_file.write(name + "\n")
            race_file.write(str(purse) + "\n")
            again = input("Would you like to enter another horse? press Y for yes. ")
        race_file.close()
    except:
        print("An error occurred!")

main()
