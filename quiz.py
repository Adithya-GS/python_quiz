#Python Quiz Game

def strip_newline(li):            #function to remove newline characters from both question and answer list
    a = list()                    #list to store stripped strings
    for i in li:
        a.append(i.strip())
    return a

print(" "*10+"Welcome to python quiz!!")
choice = input("Do you want to play the game?(yes or no) : ")
if choice.lower() != "yes":
    quit()

#code to read both question and answer text file
f = open("C:/Users/HP/PycharmProjects/pythonquiz/questions.txt", "r")
q_list = f.readlines()
f.close()
que_list = strip_newline(q_list)

f = open("C:/Users/HP/PycharmProjects/pythonquiz/answers.txt", "r")
a_list = f.readlines()
f.close()
ans_list = strip_newline(a_list)

score = 0
for i in range(len(que_list)):

    print(que_list[i])
    ans = input("Enter your answer : ")
    if ans.lower() in ans_list:
        print("Correct answer!!!")
        score+=1

    else:
        print("Wrong Answer!!!")

    if i==len(que_list)-1:
        print("Thank you for playing the game")
        print("Your Score = ", score)
        break

    ch = input("Do you want to continue(y or n) : ")
    if ch.lower() != "y":
        print("Your Score = ", score)
        break

    else:
        continue








