import os, sys, time
import curses

sys.path.append(os.path.abspath('./lib'))

from board import Board
from player import Player
from enemy import Enemy

def main(win):
  win.clear()
  board = Board(win, 'board.txt')

  score = 0

  player = Player(board)
  enemies = [
    Enemy(board, 9),
    Enemy(board, 8),
  ]

  board.draw()
  key = 0

  while key != ord('q'):
    key = win.getch()

    player.move(chr(key))

    for enemy in enemies:
      enemy.move(player.get_pos())

    win.clear()

    board.draw()

    win.addstr(board.size_y + 2, 0, 'Score: ' + str(score))

    for enemy in enemies:
      if (player.get_pos() == enemy.get_pos()):
        board.game_over()
        break

    score += 1

  while key != ord('q'):
    key = win.getch()

curses.wrapper(main)
