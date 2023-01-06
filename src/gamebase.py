##
# Author : Christian Garcia
# Project: GameBase class for poker game
#
import pygame

class GameBase:
  """ Class to manage a group of sprites """
  def __init__(self, width, height):
    """
    Initialize variables for the game

        Parameters:
            width(int) - the width of the display
            height(int) - the height of the display

    """
    pygame.init()
    self._width = width
    self._height = height
    self._display = pygame.display.set_mode((self._width, self._height))
    self._clock = pygame.time.Clock()
    self._framesPerSecond = 30
    self._sprites = pygame.sprite.LayeredUpdates()
    self._ticks = 0
    self._done = False

  def mouseButtonDown(self, x, y):
    """ 
    Performs the following code when mouse button is clicked

        Parameters:
            x(int) - the x coordinate of the mouse position
            y(int) - the y coordinate of the mouse position

    """
    return

  def keyDown(self, key):
    """ 
    Performs the following code when a key is pressed

        Parameters:
            key - the key being pressed

    """
    return

  def update(self):
    """ Updates this object's sprites """
    self._sprites.update()

  def draw(self):
    """ Draws this object's sprites """
    self._sprites.draw(self._display)

  def add(self, sprite):
    """
    Adds a sprite to this object's sprites 

        Parameters:
            sprite - a sprite object

    """
    self._sprites.add(sprite)

  def getTicks(self):
    """
    Gets the current ticks

        Returns:
            An int representing the current number of ticks
    """
    return self._ticks

  def reset(self):
    """ Resets sprites and ticks """
    self._sprites = pygame.sprite.LayeredUpdates()
    self._ticks = 0

  def quit(self):
    """ Tells the object to finish the 'run' loop """
    self._done = True

  def run(self):
    """ Runs the game """
    while not self._done:
      # Check events that occurred
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          self.mouseButtonDown(event.pos[0], event.pos[1])
        elif event.type == pygame.KEYDOWN:
          self.keyDown(event.key)
      self.update()
      # Set background color
      WHITE = (255, 255, 255)
      self._display.fill(WHITE)
      # Draw the sprites
      self.draw()
      # Update the display
      pygame.display.update()
      self._clock.tick(self._framesPerSecond)
      self._ticks += 1
