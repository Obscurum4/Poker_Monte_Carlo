from random import shuffle
import random

point_1 = 0
point_2 = 0
rank_names = ["high card", "pair", "two pair", "three of a kind", "straight", "flush", "full house",
"four of a kind", "straight flush"]

"""
deck = ["AC","2C","3C","4C","5C","6C","7C","9C","8C","9C","10C","JC","QC","KC",
        "AD","2D","3D","4D","5D","6D","7D","9D","8D","9D","10D","JD","QD","KD",
        "AH","2H","3H","4H","5H","6H","7H","9H","8H","9H","10H","JH","QH","KH",
        "AS","2S","3S","4S","5S","6S","7S","9S","8S","9S","10S","JS","QS","KS" ]

"""

def shuffle():
    random.shuffle(deck)
    print(deck)

hand1 = []
hand2 = []


def give_hands():
    count = 0
    while count <= 4 :
        hand1.append(deck[0])
        deck.remove(deck[0])
        hand2.append(deck[0])
        deck.remove(deck[0])
        count += 1


def suit(card):
    return card[-1]

def value(card):
    if card[0] == "A":
        return 14
    if card[0] == "J":
        return 11
    if card[0] == "Q":
        return 12
    if card[0] == "K":
        return 13
    return int(card[0:-1])

def is_flush(cards):
  return all([suit(card) == suit(cards[0]) for card in cards[1:]])

def hand_dist(cards):
  dist = {i:0 for i in range(1, 15)}
  for card in cards:
    dist[value(card)] += 1
  dist[1] = dist[14]
  return dist

def straight_high_card(cards):
  dist = hand_dist(cards)
  for value in range(1, 11):
    if all([dist[value + k] == 1 for k in range(5)]):
      return value + 4
  return None

def card_count(cards, num, but=None):
  dist = hand_dist(cards)
  for value in range(2, 15):
    if value == but:
      continue
    if dist[value] == num:
      return value
  return None

def hand_rank(cards):
  if straight_high_card(cards) is not None and is_flush(cards):
    return 8
  if card_count(cards, 4) is not None:
    return 7
  if card_count(cards, 3) is not None and card_count(cards, 2) is not None:
    return 6
  if is_flush(cards):
    return 5
  if straight_high_card(cards) is not None:
    return 4
  if card_count(cards, 3) is not None:
    return 3
  pair1 = card_count(cards, 2)
  if pair1 is not None:
    if card_count(cards, 2, but=pair1) is not None:
      return 2
    return 1
  return 0

def compare():
    if x <= y:
        point_2 += 1
        print("Player 2 wins")
        print(point_2_)
    if x>= y:
        point_1 += 1
        print("Player 1 wins")
        print (point_1)
    else:
        print("Tie")

def rank():
    global point_1
    global point_2
    x = str(hand_rank(hand1))
    print(x)
    y = str(hand_rank(hand2))
    print(y)
    if x < y:
        point_2 += 1
        print("Player 2 wins")
    if x> y:
        point_1 += 1
        print("Player 1 wins")
    if x == y:
        print("Tie")
    print("Player 1 has ", point_1, "point/s")
    print("Player 2 has ", point_2, " point/s")


def make_deck():
  deck = []
  for suit in ("D", "C", "H", "S"):
    for value in range(2, 15):
      if value < 11:
        value_string = str(value)
      else:
        value_string = ("J", "Q", "K", "A")[value - 11]
      deck.append(value_string + suit)
  return deck

def show_compare_hands(hand1, hand2):
  sgn = compare(hand1, hand2)
  result = ("loses to", "ties", "beats")[sgn + 1]
  print(f'{hand1} {result} {hand2}')
  r1 = rank(hand1)
  r2 = rank(hand2)
  print(f'{rank_names[r1]} {result} {rank_names[r2]}')

def deal(deck, n):
  hand = deck[0:n]
  del deck[0:n]
  return hand

def shuffled_deck():
  deck = make_deck()
  random.shuffle(deck)
  return deck

def rank_distribution(n=100000):
  dist = {i: 0 for i in range(9)}
  for i in range(n):
    deck = shuffled_deck()
    hand = deal(deck, 5)
    dist[hand_rank(hand)] += 1

  for r in range(9):
    print(f'{rank_names[r]}: {dist[r]} ({100 * dist[r] / n}%)')

rank_distribution()



