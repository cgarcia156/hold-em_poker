##
# Author : Christian Garcia
# Project: Poker Game (Texas Hold 'Em)
#
from pokergame import PokerGame
from person import Person

def main():
  # Set the dimensions
  WIDTH, HEIGHT = 800, 600
  # Create a player with a starting balance of $1000
  player = Person(1000)
  # Run the game
  game = PokerGame(WIDTH, HEIGHT, player)
  game.run()

# Start the program
main()