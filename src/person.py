##
# Author : Christian Garcia
# Project: Person class for poker game
#
class Person:
  """ Class which represents a person at a poker table """
  def __init__(self, money):
    """
    Constructs a person with the given amount of money

        Parameters:
            money(number) - the amount of money this person has

    """
    self._money = money
    self._hand = []

  def setHand(self, hand):
    """
    Sets the person's hand

        Parameters:
            hand(list of cards) - the person's hand of cards

    """
    self._hand = hand

  def win(self, amount):
    """
    Adds the amount of money won by the person

        Parameters:
            amount(number) - the amount of money won

    """
    if amount < 0:
      raise RuntimeError("Cannot win a negative amount of cash")

    self._money += amount

  def lose(self, amount):
    """
    Subtracts the amount of money lost by the person

        Parameters:
            amount(number) - the amount of money lost

    """
    if self._money - amount < 0:
      raise RuntimeError("Person doesn't have enough cash to pay")

    if amount < 0:
      raise RuntimeError("Cannot lose a negative amount of money")

    self._money -= amount

  def getBalance(self):
    """
    Gets the balance of the person

        Returns:
            (number) - the amount of cash this person has

    """
    return self._money

  def getHand(self):
    """
    Gets the hand of the person

        Returns:
            (list of cards) - this person's hand of cards

    """
    return self._hand