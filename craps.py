from random import randint

def roll():
    dice1 = randint(1,6)
    dice2 = randint(1,6)

    result = dice1 + dice2
    return result

def sim_games(n):
    wins = losses = 0
    for i in range(n):
        if game():
            wins = wins + 1
        else:
            losses = losses + 1
    return wins, losses


def game():
    dice = roll()

    if dice in (2,3,12):
        return False

    if dice in (7,11):
        return True

    while True:
        new_roll = roll()

        if new_roll==dice:
            return True

        if new_roll == 7:
            return False

def main():

    n = eval(input("How many games of craps would you like to play? "))
    w, l = sim_games(n)
    percentage = float(w/l)

    print("wins:", w,"losses:", l)
    print("Win/Loss ratio: ", percentage)


main()
