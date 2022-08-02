import random

deck = [
    ["AC", "5C", "10C", "7C", "3S"],
    ["2C", "3D", "4S", "5H", "2D"],
    ["2C", "3D", "4S", "3H", "2D"],
    ["5S", "4C", "AD", "4S", "4H"],
    ["3H", "7H", "6S", "4D", "5S"],
    ["AC", "5C", "10C", "7C", "3C"],
    ["5C", "8D", "5H", "8S", "8H"],
    ["3D", "7H", "7S", "7C", "7D"],
    ["AS", "10S", "QS", "KS", "JS"],
]

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

def compare_hands(hand1, hand2):
  r1 = hand_rank(hand1)
  r2 = hand_rank(hand2)
  if r1 < r2:
    return -1
  if r1 > r2:
    return 1
  # Need to add test for high cards - tie breakers
  return 0

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

def shuffled_deck():
  deck = make_deck()
  random.shuffle(deck)
  return deck

def deal(deck, n):
  hand = deck[0:n]
  del deck[0:n]
  return hand

rank_names = ["high card", "pair", "two pair", "three of a kind", "straight", "flush", "full house",
"four of a kind", "straight flush"]

def show_compare_hands(hand1, hand2):
  sgn = compare_hands(hand1, hand2)
  result = ("loses to", "ties", "beats")[sgn + 1]

  r1 = hand_rank(hand1)
  r2 = hand_rank(hand2)


hand1 = deal(deck, 5)
hand2 = deal(deck, 5)

def test_random_hands(n=20):
  for i in range(n):
    deck = shuffled_deck()
    show_compare_hands(deal(deck, 5), deal(deck, 5))

deal(deck, 5)
hand1
hand2
show_compare_hands(hand1, hand2)
    
