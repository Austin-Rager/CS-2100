# Five Card Stud - Exact Calculation
# Using combination generator to calculate exact probabilities

def next_r_combination(a, n):
    r = len(a)
    i = r - 1
    while i >= 0 and a[i] == n - r + i:
        i -= 1
    if i < 0:
        return False
    a[i] += 1
    for j in range(i + 1, r):
        a[j] = a[j - 1] + 1
    return True

def generateAllCombinations(n, r):
    if r > n or r < 0:
        return []

    a = list(range(r))
    allCombinations = [a[:]]

    while next_r_combination(a, n):
        allCombinations.append(a[:])

    return allCombinations

def getRank(card):
    return card % 13

def getSuit(card):
    return card // 13

def handRanks(hand):
    ranks = [getRank(card) for card in hand]
    ranks.sort()
    return ranks

def handSuits(hand):
    suits = [getSuit(card) for card in hand]
    return suits

def handFrequency(hand):
    ranks = handRanks(hand)
    frequency = {}
    for rank in ranks:
        if rank in frequency:
            frequency[rank] += 1
        else:
            frequency[rank] = 1
    return frequency

def isFlush(hand):
    suits = handSuits(hand)
    return all(suit == suits[0] for suit in suits)

def isFourOfAKind(hand):
    frequency = handFrequency(hand)
    return 4 in frequency.values()

def isThreeOfAKind(hand):
    frequency = handFrequency(hand)
    return 3 in frequency.values() and 2 not in frequency.values()

def isFullHouse(hand):
    frequency = handFrequency(hand)
    return sorted(frequency.values()) == [2, 3]

def isTwoPair(hand):
    frequency = handFrequency(hand)
    return list(frequency.values()).count(2) == 2

def isOnePair(hand):
    frequency = handFrequency(hand)
    return list(frequency.values()).count(2) == 1 and 3 not in frequency.values() and 4 not in frequency.values()

def isStraight(hand):
    ranks = handRanks(hand)
    if ranks == [0, 1, 2, 3, 12]:  # Special case for Ace-low straight
        return True
    for i in range(4):
        if ranks[i] + 1 != ranks[i + 1]:
            return False
    return True

def isStraightFlush(hand):
    return isStraight(hand) and isFlush(hand)

def isRoyalFlush(hand):
    ranks = handRanks(hand)
    return isFlush(hand) and ranks == [0, 9, 10, 11, 12]

def main():
    royalFlushCount = 0
    straightFlushCount = 0
    fourOfAKindCount = 0
    fullHouseCount = 0
    flushCount = 0
    straightCount = 0
    threeOfAKindCount = 0
    twoPairCount = 0
    onePairCount = 0
    nothingCount = 0

    # Generate all possible 5-card combinations from a 52-card deck
    # Cards are numbered 0-51
    allHands = generateAllCombinations(52, 5)
    numHands = len(allHands)

    print(f"Generating all {numHands} possible hands...")

    # Count each type of hand
    for hand in allHands:
        if isRoyalFlush(hand):
            royalFlushCount += 1
        elif isStraightFlush(hand):
            straightFlushCount += 1
        elif isFourOfAKind(hand):
            fourOfAKindCount += 1
        elif isFullHouse(hand):
            fullHouseCount += 1
        elif isFlush(hand):
            flushCount += 1
        elif isStraight(hand):
            straightCount += 1
        elif isThreeOfAKind(hand):
            threeOfAKindCount += 1
        elif isTwoPair(hand):
            twoPairCount += 1
        elif isOnePair(hand):
            onePairCount += 1
        else:
            nothingCount += 1

    print(f"\nEXACT PROBABILITIES FROM {numHands} HANDS:")
    print(f"Royal Flush: {royalFlushCount} ({royalFlushCount/numHands * 100:.6f}%)")
    print(f"Straight Flush: {straightFlushCount} ({straightFlushCount/numHands * 100:.6f}%)")
    print(f"Four of a Kind: {fourOfAKindCount} ({fourOfAKindCount/numHands * 100:.6f}%)")
    print(f"Full House: {fullHouseCount} ({fullHouseCount/numHands * 100:.6f}%)")
    print(f"Flush: {flushCount} ({flushCount/numHands * 100:.6f}%)")
    print(f"Straight: {straightCount} ({straightCount/numHands * 100:.6f}%)")
    print(f"Three of a Kind: {threeOfAKindCount} ({threeOfAKindCount/numHands * 100:.6f}%)")
    print(f"Two Pair: {twoPairCount} ({twoPairCount/numHands * 100:.6f}%)")
    print(f"One Pair: {onePairCount} ({onePairCount/numHands * 100:.6f}%)")
    print(f"Nothing: {nothingCount} ({nothingCount/numHands * 100:.6f}%)")

    # Verify all hands are accounted for
    total = (royalFlushCount + straightFlushCount + fourOfAKindCount +
             fullHouseCount + flushCount + straightCount + threeOfAKindCount +
             twoPairCount + onePairCount + nothingCount)
    print(f"\nTotal hands counted: {total} (should equal {numHands})")

if __name__ == "__main__":
    main()
