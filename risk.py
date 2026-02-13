import random

def attackerDiceRoll():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    die3 = random.randint(1, 6)
    dice = sorted([die1, die2, die3], reverse=True)
    return dice[:2]  # Return the two highest rolls

def defenderDiceRoll():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    dice = sorted([die1, die2], reverse=True)
    return dice  # Return both rolls sorted

def battle():
    attacker = attackerDiceRoll()
    defender = defenderDiceRoll()

    attacker_losses = 0
    defender_losses = 0

    for a_roll, d_roll in zip(attacker, defender):
        if a_roll > d_roll:
            defender_losses += 1
        else:
            attacker_losses += 1

    return attacker_losses, defender_losses

def simulateBattles(num_battles):
    total_attacker_losses = 0
    total_defender_losses = 0 

    for _ in range(num_battles):
        a_losses, d_losses = battle()
        total_attacker_losses += a_losses
        total_defender_losses += d_losses

    return total_attacker_losses, total_defender_losses

def main():
    num_battles = 10
    attacker_losses, defender_losses = simulateBattles(num_battles)
    print(f"After {num_battles} battles:")
    print(f"Total Attacker Losses: {attacker_losses}")
    print(f"Total Defender Losses: {defender_losses}")

    total_points = attacker_losses + defender_losses
    attacker_points = defender_losses  # Attacker wins when defender loses!
    attacker_percentage = (attacker_points / total_points) * 100

    print(f"\nTotal points awarded: {total_points}")
    print(f"Attacker won: {attacker_points} points ({attacker_percentage:.2f}%)")
    print(f"Defender won: {attacker_losses} points ({100 - attacker_percentage:.2f}%)")

if __name__ == "__main__":
    main()