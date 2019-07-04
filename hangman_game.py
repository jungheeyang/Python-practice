
from lxml import html
import requests
import string
import re
from xml.etree import ElementTree as etree
import random

# Scraping words to use for a game
page = requests.get('https://1000mostcommonwords.com/1000-most-common-english-words/')
tree = html.document_fromstring(page.content)
words = tree.xpath('//*[@id="post-192"]/div/table')

col = []
i = 0

for t in words[0]:
    i += 1
    scarps = t.text_content()
    col.append((scarps))

# making a list
scarps = " ".join(re.findall("[a-zA-Z]+",scarps.replace('\n','')))
scarps=list(scarps.split(" "))


# pick a random word
answer = random.choice(scarps)
temp_answer = answer
# print(answer)


print("\n\nLet's play hangman!")
print("Guess the word character by character!")
print("You only have 10 chances to save man's life. ")
print("Good luck! ♣︎\n")
print(f'The word has {len(answer)} characters')



# FUNCTION checking if it's valid input
def right_or_not(char):
    if not char.isalpha():
        if len(char) != 1:
            return False
        return False

    else:
        if len(char) != 1:
            return False
        return True

# FUNCTION hangman figure
def hangman_figure(num):
    if num==1:
        print('-----')
        print('\n\n\n\n\n\n')
    elif num==2:
        print('-----')
        print('|\n|\n|\n|\n|\n|')
    elif num==3:
        print('-----')
        print('|\n|\n|\n|\n|\n|')
        print('--------')
    elif num==4:
        print('-----')
        print('|  |')
        print('|\n|\n|\n|\n|')
        print('--------')
    elif num==5:
        print('-----')
        print('|  |')
        print('|  0')
        print('|\n|\n|\n|')
        print('--------')
    elif num==6:
        print('-----')
        print('|  |')
        print('|  0')
        print('|  |')
        print('|  |')
        print('|\n|')
        print('--------')
    elif num==7:
        print('-----')
        print('|  |')
        print('|  0')
        print('| \\|')
        print('|  |')
        print('|\n|')
        print('--------')
    elif num==8:
        print('-----')
        print('|  |')
        print('|  0')
        print('| \\|/')
        print('|  |')
        print('|')
        print('|')
        print('--------')
    elif num==9:
        print('-----')
        print('|  |')
        print('|  0')
        print('| \\|/')
        print('|  |')
        print('| / ')
        print('|')
        print('--------')
    elif num==10:
        print('The man is dead  :(')
        print('-----')
        print('|  |')
        print('|  0')
        print('| \\|/')
        print('|  |')
        print('| / \\')
        print('|')
        print('--------')

# FUNCTION check the answer
def checking(answer):
    count = 1
    guess = ''

    while True:
        char = input('What is your guess? \t>> ')
        char = char.lower()

        if not right_or_not(char):
            print('Please enter valid input')

        elif char == answer[0]:
            print('Good guess! :) ')
            answer = answer[1:]
            guess = guess + char
            if guess == temp_answer:
                return True

        else:
            print('Wrong guess :(')
            print(f'{10 - count} guesses left!')
            count += 1
            hangman_figure(count)
            if count == 10:
                return False

        print(f'Your guess >> {guess}')


# Game ending
if checking(answer):
    print('\nYou have saved a man! Congrats! :D')
    print('    ♥︎')
    print('♥︎')
    print('  0  ♥︎')
    print(' \\|/ ')
    print('  |   < Thank you!')
    print(' / \\')
    print('------')

else:
    print('\nGame over.')
