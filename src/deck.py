## 
# Author : Christian Garcia
# Project: Deck class for poker game
#
from random import shuffle

class Deck:
  """ Object to represent a deck of playing cards """
  def __init__(self):
    """ Initializes variables for the Deck """
    self._cards = []
    for i in range(52):
      self._cards.append(i)

  def shuffle(self):
    """ Shuffles the cards """
    shuffle(self._cards)

  def draw(self, amount):
    """
    Draws the given amount of cards from the deck

        Parameters:
            amount(int) - the number of cards being drawn

        Returns:
            A list of integers representing the cards' values

    """
    # Check if the user is trying to draw too many cards than exist
    if amount > len(self._cards):
      raise RuntimeError("cannot draw more cards than in existence")
    
    # Create an empty list of cards
    cards = []

    # Add the given amount of cards to the list
    for i in range(amount):
      card = self._cards.pop(0)
      cards.append(card)
      self._cards.append(card)

    return cards