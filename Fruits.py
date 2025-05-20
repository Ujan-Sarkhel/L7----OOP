import random

class Questionnaire:
    def __init__(self):
        self.fruits={'apple':'red','orange':'orange','watermelon':'green', 'banana':'yellow'}
def quiz(self):
    while(True):
        fruit,color=random.choice(list(self.fruits.items()))
        print("Whats is the color of {}".format(fruit))
        answer=input()
        if(answer.lower()==color):
            print("Correct answer")
        else: 
            print("Wrong answer")
        option=int(input("enter 99, if you want to play again otherwise enter 1: "))
        if(option):
            break
print("welcome to fruit quiz")
fq=Questionnaire()
fq.quiz()