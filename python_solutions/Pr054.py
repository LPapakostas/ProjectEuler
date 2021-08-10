from helper_functions import timer
from collections import Counter


def read_file(path: str) -> list:
    """Helper function that reads appropriate
    file data.
    """
    data = []

    with open(path) as f:
        for line in f.readlines():
            data.append(line.split())

    return data


def high_card(cards: list) -> int:
    """
    """
    card_values = [CARD_VALUES[card[0]] for card in cards]
    return max(card_values)


def one_pair(cards: list) -> int:
    """
    """
    card_values = [card[0] for card in cards]
    card_counter = Counter(card_values)
    if (len(card_counter) == 4):
        return 10e2  # need to find max element and multiply
    return 0


def two_pairs(cards: list) -> int:
    """
    """
    cards_values = [card[0] for card in cards]
    card_counter = Counter(cards_values)
    if (len(card_counter) == 3):  # need to add more
        return 10e3
    return 0


def three_of_a_kind(cards: list) -> int:
    """
    """
    pass


if (__name__ == "__main__"):

    cards = "23456789TJQKA"
    CARD_VALUES = {card: i for i, card in enumerate(cards)}

    FPATH = "Pr054_poker.txt"
    poker_hands = read_file(FPATH)

    hand1 = poker_hands[0]
    p1_hand = ['8C', '8S', 'KC', 'KH', '4S']

    one_pair(p1_hand)

    '''
    1) Split each hand into values and suits.
    2) Implement each condition and assign it a value
    * ROYAL FLUSH --> 10^10
    * STRAIGHT FLUSH --> 10^9
    * FOUR OF A KIND --> 10^8
    * FULL HOUSE --> 10^7
    * FLUSH --> 10^6
    * STRAIGHT --> 10^5
    * THREE OF A KIND --> 10^4
    * TWO PAIRS --> 10^3
    * ONE PAIR --> 10^2
    * HIGH CARD --> 10
    '''
