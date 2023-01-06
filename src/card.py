##
# Author : Christian Garcia
# Project: Card class for poker game
#
from imagesprite import ImageSprite

class Card(ImageSprite):
  """ Object to represent a playing card """
  def __init__(self, x, y, num):
    """
    Initializes the variables for this Card object

        Parameters:
            x(int) - the x coordinate of the left side of the card
            y(int) - the y coordinate of the top of the card
            num(int) - the int associated with this card's image/value

    """
    self._images = self._createImageDict()
    self._file = "../DECK/" + self._images[num]
    super().__init__(x, y, self._file)
    self._layer = 1
    self._faceUp = True
    self._num = num
    self._x = x
    self._y = y

  def flip(self):
    """ Flips this card by changing its image """
    if self._faceUp:
      super().loadImage(self._x, self._y, "../DECK/b.gif")
      self._faceUp = False
    else:
      super().loadImage(self._x, self._y, self._file)
      self._faceUp = True

  def getNumber(self):
    """ 
    Gets the number of this card (0-51) associated with its image/value

        Returns:
            (int) - The int associated with this card's image/value

    """
    return self._num

  def updatePos(self, x, y):
    """
    Updates the position of the card

        Parameters:
            x(int) - the new x coordinate of the left side of the card
            y(int) - the new y coordinate of the top of the card

    """
    super().__init__(x, y, self._file)
    self._x = x
    self._y = y

  def _createImageDict(self):
    """
    Creates a dictionary mapping numbers 0-51 to a card image

        Returns:
            The dictionary

    """
    images = {}
    suits = ['c','d','h','s']

    i = 0
    for num in range(13):
      char = str(num+1)
      for suit in suits:
        images[i] = (char + suit + ".gif")
        i += 1

    return images

  