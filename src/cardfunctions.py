##
# Author : Christian Garcia
# Project: Card functions
#
from math import ceil
from random import randint
from deck import Deck

def main():
  """ Tests the functions with two sets of 7 cards """
  middleCards = []
  userCards = []
  aiCards = []
  suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
  values = ['Ace','2','3','4','5','6','7','8','9','10',
            'Jack','Queen','King']
  deck = Deck()
  deck.shuffle()

  # Draw the cards
  middleCards = deck.draw(5)
  userCards = deck.draw(2)
  aiCards = deck.draw(2)

  # Display the ai's card values
  print("AI Cards:")
  for x in aiCards:
    print(values[(x // 4)], "of", suits[x % 4])
  print()

  # Display the middle card values 
  print("Middle Cards:")
  for x in middleCards:
    print(values[(x // 4)], "of", suits[x % 4])
  print()

  # Display the user's card values
  print("Your Cards:")
  for x in userCards:
    print(values[(x // 4)], "of", suits[x % 4])
  print()

  userCards += middleCards
  aiCards += middleCards

  # Check for the best hand value
  userValue = checkHand(userCards)
  print("You got:", userValue)
  aiValue = checkHand(aiCards)
  print("The computer got:", aiValue)

  # Compare the hand values
  winner = compareHands(userValue, aiValue)

  # Determine the winner
  if winner == 0:
    print("Tie")
  elif winner == 1:
    print("You Win")
  else:
    print("You lost")
  print()

def checkHand(hand):
  """
  Checks a hand and returns the highest hand value

      Parameters:
          hand(list of cards) - the player's hand

      Returns:
          (str) - the highest hand value

  """
  if royalFlush(hand): return "Royal Flush"
  if straightFlush(hand): return "Straight Flush"
  if fourOfAKind(hand): return "Four of a Kind"
  if fullHouse(hand): return "Full House"
  if flush(hand): return "Flush"
  if straight(hand): return "Straight"
  if threeOfAKind(hand): return "Three of a Kind"
  if twoPairs(hand): return "Two Pairs"
  if pair(hand): return "Pair"

  return highcard(hand)
  
def royalFlush(hand):
  """
  Checks if the hand contains a royal flush

      Parameters:
          hand(list of cards) - the player's hand

      Returns:
          True if the hand contains a royal flush, otherwise False

  """
  royalSet = set([10,11,12,13,1])
  possibleCards = set()
  suitCounts = [0,0,0,0]

  for card in hand:
    if (card // 4)+1 in royalSet:
      possibleCards.add(card)

  for card in possibleCards:
    suitCounts[card % 4] += 1

  for count in suitCounts:
    if count == 5:
      return True
  
  return False

def straightFlush(hand):
  """
  Checks if the hand contains a straight flush

      Parameters:
          hand(list of cards) - the player's hand

      Returns:
          True if the hand contains a straight flush, otherwise False

  """
  possibleCards = set()
  suitCounts = [0,0,0,0]
  values = []

  for card in hand:
    suitCounts[card % 4] += 1

  maximum = max(suitCounts)
  if maximum < 5:
    return False

  i = suitCounts.index(maximum)
  for card in hand:
    if card % 4 == i:
      possibleCards.add(card)

  for card in possibleCards:
    value = (card // 4) + 1
    if value not in values:
      values.append((card // 4)+1)

  values.sort()
  for x in range(len(values) - 4):
    if values[x] == values[x+1]-1 and \
      values[x+1] == values[x+2]-1 and\
      values[x+2] == values[x+3]-1 and\
      values[x+3] == values[x+4]-1:
      return True

  if set([10,11,12,13,1]).issubset(values):
    return True

  return False

def fourOfAKind(hand):
  """
  Checks if the hand contains four of a kind

      Parameters:
          hand(list of cards) - the player's hand

      Returns:
          True if the hand contains four of a kind, otherwise False

  """
  values = [0,0,0,0,0,0,0,0,0,0,0,0,0]

  for card in hand:
    values[card // 4] += 1

  if 4 in values:
    return True
  else:
    return False

def fullHouse(hand):
  """
  Checks if the hand contains a full house

      Parameters:
          hand(list of cards) - the player's hand

      Returns:
          True if the hand contains a full house, otherwise False

  """
  values = [0,0,0,0,0,0,0,0,0,0,0,0,0]

  for card in hand:
    values[card // 4] += 1

  if 3 in values and 2 in values:
    return True
  else:
    return False

def flush(hand):
  """
  Checks if the hand contains a flush

      Parameters:
          hand(list of cards) - the player's hand

      Returns:
          True if the hand contains a flush, otherwise False

  """
  suitCounts = [0,0,0,0]

  for card in hand:
    suitCounts[card % 4] += 1

  for count in suitCounts:
    if count >= 5:
      return True

  return False

def straight(hand):
  """
  Checks if the hand contains a straight

      Parameters:
          hand(list of cards) - the player's hand

      Returns:
          True if the hand contains a straight, otherwise False

  """
  
  values = []

  for card in hand:
    value = (card // 4) + 1
    if value not in values:
      values.append((card // 4)+1)

  values.sort()
  for x in range(len(values) - 4):
    if values[x] == values[x+1]-1 and \
      values[x+1] == values[x+2]-1 and\
      values[x+2] == values[x+3]-1 and\
      values[x+3] == values[x+4]-1:
      return True

  if set([10,11,12,13,1]).issubset(values):
    return True

  return False

def threeOfAKind(hand):
  """
  Checks if the hand contains three of a kind

      Parameters:
          hand(list of cards) - the player's hand

      Returns:
          True if the hand contains three of a kind, otherwise False

  """
  values = [0,0,0,0,0,0,0,0,0,0,0,0,0]

  for card in hand:
    values[card // 4] += 1

  if 3 in values:
    return True
  else:
    return False
  
def twoPairs(hand):
  """
  Checks if the hand contains two pairs

      Parameters:
          hand(list of cards) - the player's hand

      Returns:
          True if the hand contains two pairs, otherwise False

  """
  values = [0,0,0,0,0,0,0,0,0,0,0,0,0]

  for card in hand:
    values[card // 4] += 1

  if values.count(2) >= 2:
    return True
  else:
    return False

def pair(hand):
  """
  Checks if the hand contains a pair

      Parameters:
          hand(list of cards) - the player's hand

      Returns:
          True if the hand contains a pair, otherwise False

  """
  values = [0,0,0,0,0,0,0,0,0,0,0,0,0]

  for card in hand:
    values[card // 4] += 1

  if 2 in values:
    return True
  else:
    return False

def highcard(hand):
  """
  Gets the highest card in the hand

      Parameters:
          hand(list of cards) - the player's hand

      Returns:
          Returns the value of the highest card

  """
  values = set()

  for card in hand:
    values.add((card // 4) + 1)

  if 1 in values: return 'Ace'
  if 13 in values: return 'King'
  if 12 in values: return 'Queen'
  if 11 in values: return 'Jack'

  return str(max(values))

def compareHands(hand1, hand2):
  """
  Compares two hand values to see which is better

      Parameters:
          hand1(list of cards) - the first hand
          hand2(list of cards) - the second hand

      Returns:
          (int) - 0: draw, 1: hand1 wins, 2: hand2 wins

  """
  ranking = ['2','3','4','5','6','7','8','9','10','Jack','Queen',
  'King','Ace','Pair','Two Pairs','Three of a Kind','Straight',
  'Flush','Full House','Four of a Kind','Straight Flush','Royal Flush']

  if ranking.index(hand1) > ranking.index(hand2):
    return 1
  elif ranking.index(hand1) < ranking.index(hand2):
    return 2
  else:
    return 0

if __name__ == "__main__":
  main()

# Sample Run:

# AI Cards:
# Jack of Spades
# 4 of Diamonds

# Middle Cards:
# 10 of Hearts
# 7 of Hearts
# Jack of Diamonds
# 9 of Diamonds
# Jack of Hearts

# Your Cards:
# 10 of Clubs
# 7 of Diamonds

# You got: Two Pairs
# The computer got: Three of a Kind
# You lost