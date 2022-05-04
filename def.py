import random
def getAnswer(answerNumb):
    if answerNumb ==1:
        return "it is cool"
    elif answerNumb ==2:
        return "It is decidedly so"
    r = random.randint(1,9)
    fortune = getAnswer(r)
    print(fortune)
    
    def two_oldest_ages(ages):
     y=two_oldest_ages([1,43,5,6,78])              #i realized that i could just do whatever we were doing under the function and continue calling it.
     print(y)

