#Roxanne Hoggan
#Complete
#Reads records from horse_list.txt, displays them, and calculates average

def main():
    count = 0
    total = 0
    try:
        print("Today's Winnings")
        print("-"*15)
        race_file = open("horse_list.txt", "r")
        horse = race_file.readline()
        
        while horse != "":
            count += 1
            purse = float(race_file.readline())
            total += purse
            horse = horse.rstrip("\n")

            print("Horse:", horse)
            print("Purse: $", format(purse, ",.2f"), sep="")
            horse = race_file.readline()

        print("The total purse for the day is: $", format(total, ",.2f"), sep="")
        print("The average purse for the day is: $", format(total/count, ",.2f"), sep="")

        race_file.close()

    except IOError:
        print("An error occured trying to read the file.")
    except ValueError:
        print("Non numeric data found in the file.")
    except:
        print("An error occured!")

main()
