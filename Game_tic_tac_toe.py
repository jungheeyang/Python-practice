# tic tac toe game
# point to improve: use of function


no_winner = True
player = True
x_player = []
o_player = []

the_board = {'00': ' ', '01': ' ', '02': ' ',
             '10': ' ', '11': ' ', '12': ' ',
             '20': ' ', '21': ' ', '22': ' '}

winning_list=[['00','11','22'], ['02','11','20'],['00','10','20'],['01','11','21'],
              ['02','12','22'], ['00','01','02'], ['10','11','12'],['20','21','22']]



print("\nWelcome to 'Tic Tac Toe' game!\n")
print('Here is a few rules')
print("\t1. This game is played on a grid that's 3 squares by 3 squares.")
print("\t2. First player is X, opponent is O. Players take turns putting their marks in empty squares.")
print("\t3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.")
print("\t4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.\n")
print('Here is the board with numbers of each squares')



flag = 0
print('\n----------------')
for squares in the_board.keys():
    print('|', end='')
    print(f' {squares} ', end='')
    flag += 1
    if flag % 3 == 0:
        print('|\n----------------')

print('Please enter the number according the number of each squares.')
print('Have fun playing! :) \n\n')



while no_winner:

    # marking
    if player: # X playing
        mark = input('X >> ')
    else:      # O playing
        mark = input('O >> ')

    # wrong marking
        # case 1: marked number
        # case 2: not square numbers
    # X player
    while player:
        # case 1
        if (mark in x_player) or (mark in o_player):
            while not ((mark in x_player) and (mark in o_player)):
                print('\nMarked already. Please choose other squares.\n')
                mark = input('X >> ')
                if (mark in x_player) or (mark in o_player):
                    continue
                else:
                    break
        # case 2
        elif not mark in the_board.keys():
            while not(mark in the_board.keys()):
                print('\nPlease input the valid square number.\n')
                mark = input('X >> ')
                if not mark in the_board.keys():
                    continue
                else:
                    break
        else:
            break

    # O player
    while not player:
        if (mark in x_player) or (mark in o_player):
            while not ((mark in x_player) and (mark in o_player)):
                print('\nMarked already. Please choose other squares.\n')
                mark = input('O >> ')
                if (mark in x_player) or (mark in o_player):
                    continue
                else:
                    break
        elif not mark in the_board.keys():
            while not(mark in the_board.keys()):
                print('\nPlease input the valid square number.\n')
                mark = input('O >> ')
                if not mark in the_board.keys():
                    continue
                else:
                    break
        else:
            break



    # X player play saving
    while player:
        if mark in the_board.keys():
            the_board.update({mark: 'X'})
            x_player.append(mark)
        break


    # O player play saving
    while not player:
        if mark in the_board.keys():
            the_board.update({mark: '0'})
            o_player.append(mark)
        break


    # find the winner
    x_player.sort()
    o_player.sort()

    flag=0
    print('\n-------------')
    for xos in the_board.values():
        print('|', end='')
        print(f' {xos} ', end = '')
        flag += 1
        if flag%3==0:
            print('|\n-------------')
    print('\n')



    # find the winner
    if x_player in winning_list:
        print('\nX player is the Winner!')
        break

    if o_player in winning_list:
        print('\nO player is the Winner!')
        break

    if (len(x_player)+len(o_player))==9:
        print('Draw!')
        break


    # change player
    if player:
        player = False
    else:
        player = True

