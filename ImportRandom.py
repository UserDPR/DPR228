
getAnswer= input("What would you ask a Fortune Teller?")
import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Is that what you really want?'
    elif answerNumber == 5:
        return 'I had to laugh at that'
    elif answerNumber == 6:
        return 'Really?'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber ==8:
        return 'What do you think?'
    elif answerNumber == 9:
        return 'Surprisingly Yes'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

#print(getAnswer(random.randint(1,9)))
