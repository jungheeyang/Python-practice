from random import randint

def guessing_game(guessedNum, randNum):
    if 100<guessedNum or guessedNum<1:
        print('Out of bound! Please enter a number between 1 to 100\n')
        guessedNum = int(input('Guess the number!'))

    while guessedNum != randNum:
        if abs(guessedNum - randNum) <= 10:
            print('WARM\n')
        elif abs(guessedNum - randNum) > 10:
            print('COLD\n')

        guessedNum = int(input('Guess the number!'))
        continue

    else:
        print('You guessed it!\n')


randNum=randint(1,100)
print(randNum)
guessedNum=int(input('Guess the number!'))


guessing_game(guessedNum, randNum)


