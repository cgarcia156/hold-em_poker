##
# Author : Christian Garcia
# Project: PokerGame
#
from cardfunctions import checkHand, compareHands
from gamebase import GameBase
from person import Person
from deck import Deck
from card import Card
import pygame

# Colors
LIGHT_GRAY = (230,230,230)
GRAY = (170,170,170)
BLACK = (0,0,0)

class PokerGame(GameBase):
  """ Class to represent a game of Texas Hold 'Em Poker """
  minWage = 20
  def __init__(self, width, height, person):
    """
    Initializes the variables for the game

        Parameters:
            width(int) - the width of the display
            height(int) - the height of the display
            person(Person) - the person playing against the computer

    """
    super().__init__(width, height)
    pygame.display.set_caption("Texas Hold 'Em")
    self._font = pygame.font.SysFont("Segoe UI",30)
    self._smallfont = pygame.font.SysFont("Segoe UI",20)
    self._player = person
    self._player.lose(self.minWage)
    self._pot = self.minWage * 2
    if self._player.getBalance() >= 10:
      self._bet = 10
    else:
      self._bet = 0
    self._width = width
    self._height = height
    self._deck = Deck()
    self._deck.shuffle()
    self._middleCards = []
    self._aiCards = []
    self._state = 0
    self._finalMessage = ""


  def update(self):
    """ Update the game's objects """
    super().update()

    if self.getTicks() == 0:
      self._addOpening()
      self._addUserCards()
      self._addAiCards()

  def draw(self):
    """ Draw everything on the screen """
    super().draw()

    if self._state < 2:
      # Draw "Fold" Button
      x = (self._width // 8) * 2 - 50
      y = (self._height // 6) * 5
      self._drawButton(x, y, 100, 60, "Fold", self._font)

      # Draw "Check" button
      x = self._width // 2 - 50
      self._drawButton(x, y, 100, 60, "Check", self._font)

      # Draw "Raise" button
      x = (self._width // 8) * 6 - 50
      self._drawButton(x, y, 100, 60, "Raise", self._font)

      # Draw "+" button
      x += 110
      self._drawButton(x, y, 40, 25, "+", self._font)

      # Draw "-" button
      y += 35
      self._drawButton(x, y, 40, 25, "-", self._font)

      # Draw "x2" button
      y -= 35
      x += 50
      self._drawButton(x, y, 30, 60, "x2", self._smallfont)

      # Display the current bet
      x -= 160
      y -= 40
      betString = "$%d" % (self._bet)
      text = self._font.render(betString, True, BLACK)
      self._display.blit(text, (x,y))
    elif self._state == 2:
      # Display the result
      x = (self._width // 2) - 50
      y = (8 * self._height // 10)
      text = self._font.render(self._finalMessage, True, BLACK)
      self._display.blit(text, (x,y))

      if self._player.getBalance() >= self.minWage:
        x -= 120
        y += self._height // 10
        text = self._font.render("Press Space to Play Again", True, BLACK)
        self._display.blit(text, (x,y))
      else:
        x -= 120
        y += self._height // 10
        text = self._font.render("You have run out of money :(", True, BLACK)
        self._display.blit(text, (x,y))


    # Display the user's balance
    userBalance = "Balance: $%d" % (self._player.getBalance())
    text = self._font.render(userBalance, True, BLACK)
    self._display.blit(text, (25,25))

    # Display the pot
    potString = "Pot: $%d" % (self._pot)
    text = self._font.render(potString, True, BLACK)
    self._display.blit(text, (25,75))

  def mouseButtonDown(self, x, y):
    """ 
    Performs the following code when mouse button is clicked

        Parameters:
            x(int) - the x coordinate of the mouse position
            y(int) - the y coordinate of the mouse position

    """
    # Dimensions of buttons
    width = 100
    height = 60

    # Check if "Fold" button was clicked
    buttonX = (self._width // 8) * 2 - 50
    buttonY = (self._height // 6) * 5

    if buttonX <= x <= buttonX + width and buttonY <= y <= buttonY + height:
      if self._state == 0 or self._state == 1:
        self._finalMessage = "You Lose"
        self._pot = 0
        self._state = 2

    # Check if "Check" button was clicked
    buttonX = self._width // 2 - 50
    if buttonX <= x <= buttonX + width and buttonY <= y <= buttonY + height:
      if self._state == 0:
        self._state += 1

        # Add fourth card
        self._addFourthCard()

        # Reset bet
        if self._player.getBalance() >= 10:
          self._bet = 10
        else:
          self._bet = 0

      elif self._state == 1:
        self._state += 1

        # Add fifth card
        self._addFifthCard()

        # Turn AI cards
        for card in self._aiCards:
          card.flip()

        # Find the best hand value for the user
        cards = self._player.getHand() + self._middleCards
        playerCards = []
        for card in cards:
          playerCards.append(card.getNumber())
        playerBest = checkHand(playerCards)

        # Find the best hand value for the computer
        cards = self._aiCards + self._middleCards
        computerCards = []
        for card in cards:
          computerCards.append(card.getNumber())
        computerBest = checkHand(computerCards)

        # Determine the winner
        winner = compareHands(playerBest,computerBest)
        
        if winner == 0:
          self._finalMessage = "Tie Game"
          self._player.win(self._pot // 2)
          self._pot = 0
        elif winner == 1:
          self._finalMessage = "You Win!"
          self._player.win(self._pot)
          self._pot = 0
        else:
          self._finalMessage = "You Lose"
          self._pot = 0
        
    # Check if "Raise" button was clicked
    buttonX = (self._width // 8) * 6 - 50
    if buttonX <= x <= buttonX + width and buttonY <= y <= buttonY + height:
      if self._state == 0:
        self._state += 1

        # Add fourth card
        self._addFourthCard()

        # Subtract bet amount from player's balance
        if self._player.getBalance() >= self._bet:
          self._player.lose(self._bet)

        # Add 2X bet amount to pot
        self._pot += 2 * self._bet

        # Reset bet
        if self._player.getBalance() >= 10:
          self._bet = 10
        else:
          self._bet = 0

      elif self._state == 1:
        self._state += 1

        # Add fifth card
        self._addFifthCard()

        # Subtract bet amount from player's balance
        if self._player.getBalance() >= self._bet:
          self._player.lose(self._bet)

        # Add 2X bet amount to pot
        self._pot += 2 * self._bet

        # Turn AI cards
        for card in self._aiCards:
          card.flip()

        # Find the best hand value for the user
        cards = self._player.getHand() + self._middleCards
        playerCards = []
        for card in cards:
          playerCards.append(card.getNumber())
        playerBest = checkHand(playerCards)

        # Find the best hand value for the computer
        cards = self._aiCards + self._middleCards
        computerCards = []
        for card in cards:
          computerCards.append(card.getNumber())
        computerBest = checkHand(computerCards)

        # Determine the winner
        winner = compareHands(playerBest,computerBest)
        if winner == 0:
          self._finalMessage = "Tie Game"
          self._player.win(self._pot // 2)
          self._pot = 0
        elif winner == 1:
          self._finalMessage = "You Win!"
          self._player.win(self._pot)
          self._pot = 0
        else:
          self._finalMessage = "You Lose"
          self._pot = 0

    # Check if "+" button is clicked
    buttonX += 110
    if buttonX <= x <= buttonX + 40 and buttonY <= y <= buttonY + 25\
      and self._state < 2:
      if self._player.getBalance() >= self._bet + 10:
        self._bet += 10

    # Check if "-" button is clicked
    buttonY += 35
    if buttonX <= x <= buttonX + 40 and buttonY <= y <= buttonY + 25\
      and self._state < 2:
      if self._bet - 10 > 0:
        self._bet -= 10

    # Check if "x2" button is clicked
    buttonX += 50
    buttonY -= 35
    if buttonX <= x <= buttonX + 40 and buttonY <= y <= buttonY + 60\
      and self._state < 2:
      if self._player.getBalance() >= self._bet * 2:
        self._bet *= 2
      else:
        self._bet = self._player.getBalance()

  def keyDown(self, key):
    """ 
    Performs the following code when a key is pressed

        Parameters:
            key - the key being pressed

    """
    if key == pygame.K_SPACE:
      # Reset variables if user has enough money to play
      if self._player.getBalance() >= self.minWage:
        self._player.lose(self.minWage)
        self._pot = 2 * self.minWage
      else:
        self.quit()

      if self._player.getBalance() >= 10:
        self._bet = 10

      super().reset()
      self._deck.shuffle()
      self._player.setHand([])
      self._middleCards = []
      self._aiCards = []
      self._state = 0
      self._finalMessage = ""
      
  def _addOpening(self):
    """ Creates the 3 middle cards """
    # Draw 3 cards
    cards = self._deck.draw(3)
    dx = self._width // 6
    x = 2 * dx - 30
    y = self._height // 2

    # Create the middle card sprites
    for num in cards:
      card = Card(x,y,num)
      x += dx
      self._middleCards.append(card)
      self.add(card)

  def _addUserCards(self):
    """ Creates the user's cards """
    userCards = []

    # Draw 2 cards
    cards = self._deck.draw(2)
    x = (self._width // 2) - 85
    y = (self._height // 4) * 3 

    # Create player's card sprites
    for num in cards:
      card = Card(x,y,num)
      x += 100
      userCards.append(card)
      self.add(card)

    # Set the player's hands
    self._player.setHand(userCards)

  def _addAiCards(self):
    """ Creates the computer's cards """
    # Draw 2 cards
    cards = self._deck.draw(2)
    x = (self._width // 2) - 85
    y = (self._height // 4)

    # Create computer's card sprites
    for num in cards:
      card = Card(x,y,num)
      x += 100
      card.flip()
      self._aiCards.append(card)
      self.add(card)

  def _addFourthCard(self):
    """ Creates the fourth middle card """
    # Update position of middle cards
    dx = self._width // 6
    x = dx - 30
    y = self._height // 2

    for card in self._middleCards:
      card.updatePos(x, y)
      x += dx

    # Add fourth middle card
    cards = self._deck.draw(1)
    card = Card(x,y,cards[0])
    self._middleCards.append(card)
    self.add(card)

  def _addFifthCard(self):
    """ Creates the fifth middle card """
    dx = self._width // 6
    x = 5 * dx - 30
    y = self._height // 2

    # Add fifth middle card
    cards = self._deck.draw(1)
    card = Card(x,y,cards[0])
    self._middleCards.append(card)
    self.add(card)

  def _drawButton(self, x, y, width, height, buttonText, font):
    """
    Creates a button which changes color when hovered over

        Parameters:
            x(int) - the x coordinate of the left side of the button
            y(int) - the y coordinate of the top of the button 
            buttonText(string) - the text for the button

    """
    # Get the (x,y) coordinates of the mouse
    mouse = pygame.mouse.get_pos()

    # Draw outline for button
    pygame.draw.rect(self._display, BLACK, [x-1, y-1, width + 2, height + 2])

    # Color of the button changes if mouse is hovered over it
    if x <= mouse[0] <= x + width and y <= mouse[1] <= y + height:
      pygame.draw.rect(self._display, GRAY,[x,y,width,height]) 
    else:
      pygame.draw.rect(self._display, LIGHT_GRAY,[x,y,width,height])

    # Draw button text
    text = font.render(buttonText, True, BLACK)
    self._display.blit(text, (x + (width/2 - text.get_width()/2),
        y + (height/2 - text.get_height()/2)))
    