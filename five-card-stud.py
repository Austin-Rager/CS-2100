import random

def createDeck():
    deck = list(range(52))
    random.shuffle(deck)
    return deck

def getRank(card):
    return card % 13

def getSuit(card):
    return card // 13

def dealHand():
    deck = createDeck()
    hand = deck[:5]
    return hand

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
    if ranks == [0, 1, 2, 3, 12]:  #Special case for Ace-low straight
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

    numHands = 1000000

    for i in range(numHands):
        hand = dealHand()
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

    print(f"Royal Flush: {royalFlushCount} ({royalFlushCount/numHands * 100:.4f}%)")
    print(f"Straight Flush: {straightFlushCount} ({straightFlushCount/numHands * 100:.4f}%)")
    print(f"Four of a Kind: {fourOfAKindCount} ({fourOfAKindCount/numHands * 100:.4f}%)")
    print(f"Full House: {fullHouseCount} ({fullHouseCount/numHands * 100:.4f}%)")
    print(f"Flush: {flushCount} ({flushCount/numHands * 100:.4f}%)")
    print(f" Straight: {straightCount} ({straightCount/numHands * 100:.4f}%)")
    print(f"Three of a Kind: {threeOfAKindCount} ({threeOfAKindCount/numHands * 100:.4f}%)")
    print(f"Two Pair: {twoPairCount} ({twoPairCount/numHands * 100:.4f}%)")
    print(f"One Pair: {onePairCount} ({onePairCount/numHands * 100:.4f}%)")
    print(f"Nothing: {nothingCount} ({nothingCount/numHands * 100:.4f}%)")

if __name__ == "__main__":
    main()