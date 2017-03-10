from __future__ import division
import curses
from game import Game

def main(win):
  game = Game(win)
  game.spawn(5)
  game.play()
  #win.addstr(board.size_y + 2, 0, 'Score: ' + str(score))

curses.wrapper(main)
