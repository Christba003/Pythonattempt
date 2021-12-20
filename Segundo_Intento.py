#
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "almost"
    elif answerNumber == 3:
        return "yes"
    elif answerNumber == 4:
        return "pregunta de nuevo"
    elif answerNumber == 5:
        return "bla"
#Main

r = random.randint(1,5)
fortune = getAnswer(r)
print (fortune)


