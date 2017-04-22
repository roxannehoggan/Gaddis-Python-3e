#Roxanne Hoggan
#Complete
#Analyzes characters in given text file

def main():
    upper_count = 0
    lower_count = 0
    num_count = 0
    whitesp_count = 0
    infile = open("text.txt", "r")
    text = infile.read()
    for ch in text:
        if ch.isupper():
            upper_count +=1
        if ch.islower():
            lower_count +=1
        if ch.isdigit():
            num_count +=1
        if ch.isspace():
            whitesp_count +=1
    print("Uppercase letters:", upper_count)
    print("Lowercase letters:", lower_count)
    print("Digits:", num_count)
    print("Whitespace characters:", whitesp_count)

main()
