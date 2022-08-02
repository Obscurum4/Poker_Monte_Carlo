from random import shuffle
import random

point_1 = 0
point_2 = 0



deck = ["AC","2C","3C","4C","5C","6C","7C","9C","8C","9C","10C","JC","QC","KC",
        "AD","2D","3D","4D","5D","6D","7D","9D","8D","9D","10D","JD","QD","KD",
        "AH","2H","3H","4H","5H","6H","7H","9H","8H","9H","10H","JH","QH","KH",
        "AS","2S","3S","4S","5S","6S","7S","9S","8S","9S","10S","JS","QS","KS" ]



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

"""
shuffle()
give_hands()
hand_rank(hand1)
hand_rank(hand2)
rank()
point_1 += 1
point_2 += 1
print(point_2)
print(point_1)
"""



for i in range(20):
    shuffle()

    give_hands()
    print(hand1)
    print(hand2)
    hand_rank(hand1)
    hand_rank(hand2)
    rank()
    hand1 = []
    hand2 = []
    deck = ["AC","2C","3C","4C","5C","6C","7C","9C","8C","9C","10C","JC","QC","KC",
        "AD","2D","3D","4D","5D","6D","7D","9D","8D","9D","10D","JD","QD","KD",
        "AH","2H","3H","4H","5H","6H","7H","9H","8H","9H","10H","JH","QH","KH",
        "AS","2S","3S","4S","5S","6S","7S","9S","8S","9S","10S","JS","QS","KS" ]


"""
hand1 = ["3D", "7H", "7S", "7C", "7D"]


x = str(hand_dist(hand1))
print(x)
"""
