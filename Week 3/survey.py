# allAnswers = [Q1:{}, Q2:{}, Q3:{}, Q4:{}, Q5:{}]
#
# Q1 = {}
# Q2 = {}
# Q3 = {}
# Q4 = {}
# Q5 = {}
#
# q1 = input("What's your name?")
# Q1.append(q1)
#
# q2 = input("What is your least favorite technical term?")
# Q2.append(q2)
#
# q3 = input("When is your birthday?")
# Q3.append(q3)
#
# q4 = input("How many siblings do you have?")
# Q4.append(q4)
#
# q5 = input("What is your favorite word?")
# Q5.append(q5)

answers = []

questions = ["What's your name?", "What's your age?", "What's your favorite ice cream?", "What state do you live in?", "What color is your hair?"]

for i in range(5):
    print("NEW SURVEY")
    answer = {}
    for q in questions:
        answer[q] = input(q)
        if (input("Continue? yes or no") != yes):
            break
    answers.append(answer)
