#Roxanne Hoggan
#Complete
#Compares student answers to answer key and evaluates amount of correct answers


def main():
    
    answer_key = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", "A", \
                  "D", "C", "A", "D", "C", "B", "B", "D", "A"]

    student_solution = []
    outfile = open('student_solution.txt', 'r')
    for i in outfile:
        i = i.rstrip('\n')
        student_solution.append(i)

    count = 0
    wrong_answers = []
    for i in range(20):
        if answer_key[i] == student_solution[i]:
            count += 1
        else:
            wrong_answers.append(i)
            count+=0
            
    if count < 15:
        print("Failed")
    else:
        print("Passed!")
    print("Correctly answered questions:", count)
    print("Incorrectly answered questions:", 20-count)
    print("The incorrectly answered questions are:", wrong_answers)

main()
