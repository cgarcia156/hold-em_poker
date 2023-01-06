##
# Author : Christian Garcia
# Project: ImageSprite class
#
import pygame

class ImageSprite(pygame.sprite.Sprite):
  """ Object to represent a sprite """
  def __init__(self, x, y, filename):
    """ 
    Initializes the variables for the ImageSprite

        Parameters:
            x(int) - the x coordinate of the left side of the sprite
            y(int) - the y coordinate of the top of the sprite
            filename(str) - the path/name of the object's image file

    """
    super().__init__()
    self.loadImage(x, y, filename)

  def loadImage(self, x, y, filename):
    """ 
    Loads the sprite's image

        Parameters:
            x(int) - the x coordinate of the left side of the object
            y(int) - the y coordinate of the top of the object
            filename(str) - the path/name of the object's image file

    """
    img = pygame.image.load(filename).convert()
    self.image = img
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y - self.rect.height

  def moveBy(self, dx, dy):
    """
    Moves the sprite by (dx,dy)

        Parameters:
            dx(int) - the change of the x coordinate
            dy(int) - the change of the y coordinate 

    """
    self.rect.x += dx
    self.rect.y += dy