def battle(attacker_dice, defender_dice):
    """
    Simulate a single battle and return (attacker_losses, defender_losses)
    attacker_dice: list of 3 dice values
    defender_dice: list of 2 dice values
    """
    # Get top 2 attacker dice
    attacker_sorted = sorted(attacker_dice, reverse=True)[:2]
    # Sort defender dice
    defender_sorted = sorted(defender_dice, reverse=True)

    attacker_losses = 0
    defender_losses = 0

    if attacker_sorted[0] > defender_sorted[0]:
        defender_losses += 1
    else:
        attacker_losses += 1

    if attacker_sorted[1] > defender_sorted[1]:
        defender_losses += 1
    else:
        attacker_losses += 1

    return attacker_losses, defender_losses

def main():
    total_attacker_losses = 0
    total_defender_losses = 0
    total_battles = 0

    # Generate all possible outcomes
    # Attacker rolls 3 dice (each die: 1-6)
    # Defender rolls 2 dice (each die: 1-6)
    # Total combinations: 6^3 * 6^2 = 216 * 36 = 7,776

    print("Calculating exact probabilities for all possible dice combinations...")

    for a1 in range(1, 7):
        for a2 in range(1, 7):
            for a3 in range(1, 7):
                for d1 in range(1, 7):
                    for d2 in range(1, 7):
                        attacker_dice = [a1, a2, a3]
                        defender_dice = [d1, d2]

                        a_losses, d_losses = battle(attacker_dice, defender_dice)
                        total_attacker_losses += a_losses
                        total_defender_losses += d_losses
                        total_battles += 1

    print(f"\nEXACT RESULTS FROM {total_battles} POSSIBLE BATTLES:")
    print(f"Total Attacker Losses: {total_attacker_losses}")
    print(f"Total Defender Losses: {total_defender_losses}")

    total_points = total_attacker_losses + total_defender_losses
    attacker_points = total_defender_losses
    attacker_percentage = (attacker_points / total_points) * 100

    print(f"\nTotal points awarded: {total_points}")
    print(f"Attacker won: {attacker_points} points ({attacker_percentage:.6f}%)")
    print(f"Defender won: {total_attacker_losses} points ({100 - attacker_percentage:.6f}%)")

    print(f"\nPer-battle averages:")
    print(f"Average attacker losses per battle: {total_attacker_losses / total_battles:.6f}")
    print(f"Average defender losses per battle: {total_defender_losses / total_battles:.6f}")

if __name__ == "__main__":
    main()
