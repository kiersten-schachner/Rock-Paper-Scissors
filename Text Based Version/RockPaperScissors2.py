from random import *
moves = ['rock', 'paper', 'scissors']
print('Whoever wins two matches first, wins!')
userWins = 0
compWins = 0

def getUserMove():
    choice = input('Rock, paper, or scissors? ')
    user = choice.lower()
    if (user != 'rock' and user != 'paper' and user != 'scissors'):
        print('Invalid input.')
        return getUserMove()
    else:
        return user

def getCompMove():
    choice = randint(0,2)
    comp = moves[choice]
    return comp

def userWin(user, comp):
    global userWins
    print('You won! You chose ' + user + ' and the computer chose ' + comp)
    userWins += 1

def compWin(user, comp):
    global compWins
    print('You lost! You chose ' + user + ' and the computer chose ' + comp)
    compWins += 1

play = True

while play:
    u = getUserMove()
    c = getCompMove()
    if u == c:
        print('Tie. You and the computer chose', u)
    elif u == 'rock':
        if c == 'scissors':
            userWin(u,c)
        else:
            compWin(u,c)
    elif u == 'paper':
        if c == 'rock':
            userWin(u,c)
        else:
            compWin(u,c)
    elif u == 'scissors':
        if c == 'paper':
            userWin(u,c)
        else:
            compWin(u,c)
    if userWins >= 2 or compWins >= 2:
        play = False

if userWins >= 2:
    print('You won the game! You had ' + str(userWins) + ' wins and the computer had ' + str(compWins) + ' wins!')
else:
    print('You lost the game! You had ' + str(userWins) + ' wins and the computer had ' + str(compWins) + ' wins!')