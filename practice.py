# Guess the number game


from random import randint

print('This is a number guessing game')
print('Please guss the number between 1 to 100')
print('If the guessed number is within 10 of the number, it will say "WARM"')
print('If the guessed number is further than 10 away from the number, it will say "COLD"')
print('When your guess is closer than previous guess, it will say "WARMER"')
print('Otherwise it will say "COLDER"')
print("Okay, let's play now!\n")


nums=[0]

def guessing_game(guessed_num, rand_num):

    while True:
        if guessed_num>100 or guessed_num<1:
            guessed_num=int(input('Please guess the number again'))

        if guessed_num==rand_num:
            print('You guessed it!')
            break

        nums.append(guessed_num)

        if nums[-2]:
            if abs(guessed_num-rand_num) < abs(nums[-2]-rand_num):
                print('Warmer')
            else:
                print('Colder')

        else:
            if abs(guessed_num-rand_num)<10:
                print('Warm')
            else:
                print('Cold')

        guessed_num = int(input('Guess the number >> '))


rand=randint(1,100)
print(rand)
guess=int(input('Guess the number!'))

guessing_game(guess, rand)


################################################################################################



