import random

game = [0] * 16

gameOver = False

def left(game):
    newGame = game.copy()

    for i in range(len(newGame)-1, 0, -1):
        if (i % 4) != 0 and newGame[i] != 0 and (newGame[i - 1] == 0 or newGame[i] == newGame[i - 1]):
            newGame[i - 1] = newGame[i] + newGame[i - 1]
            newGame[i] = 0           
    return newGame

def right(game):
    newGame = game.copy()

    for i in range(len(newGame)):
        if (i % 4) != 3 and newGame[i] != 0 and (newGame[i + 1] == 0 or newGame[i] == newGame[i + 1]):
            newGame[i + 1] = newGame[i] + newGame[i + 1]
            newGame[i] = 0
    return newGame

def up(game):
    newGame = game.copy()

    for i in range(len(newGame)-1, 0, -1):
        if i >= 4 and newGame[i] != 0 and (newGame[i - 4] == 0 or newGame[i] == newGame[i - 4]):
            newGame[i - 4] = newGame[i] + newGame[i - 4]
            newGame[i] = 0
    return newGame

def down(game):
    newGame = game.copy()

    for i in range(len(newGame)):
        if i <= 11 and newGame[i] != 0 and (newGame[i + 4] == 0 or newGame[i] == newGame[i + 4]):
            newGame[i + 4] = newGame[i] + newGame[i + 4]
            newGame[i] = 0
    return newGame

def addNewNumber(game):
    newGame = game.copy()
    i = random.randint(0, len(newGame)-1)
    while newGame[i] != 0:
        i = random.randint(0, len(newGame)-1)

    newGame[i] = 2
    
    return newGame

def printGame(game):
    print()
    for i in range(len(game)):
        if i % 4 == 3:
            print("| " + str(game[i]) + " |")
            print("  - - - - - - -")

        else:
            print(" | " + str(game[i]), end="")
    print()

while not gameOver:
    game = addNewNumber(game)
    printGame(game)

    action = input("Direction : ")

    if action == "up":
        game = up(game)
    elif action == "down":
        game = down(game)
    elif action == "left":
        game = left(game)
    elif action == "right":
        game = right(game)
