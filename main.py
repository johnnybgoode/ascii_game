from __future__ import division
import curses, math, time
from board import Board
from player import Player
from enemy import Enemy

def main(win):
  win.nodelay(True)

  board = Board(win, 'board.txt')

  frame = 1/60
  game_over = False
  score = 0

  player = Player(board)
  enemies = [
    Enemy(board, 60),
    Enemy(board, 65),
  ]

  win.clear()
  board.draw()
  win.addstr(board.size_y + 2, 0, 'Score: ' + str(score))

  key = 0

  while key != ord('q') and not game_over:
    key = win.getch()

    if (key > 0):
      player.move(chr(key))

    for enemy in enemies:
      enemy.move(player.get_pos())

    win.erase()
    board.draw()
    win.addstr(board.size_y + 2, 0, 'Score: ' + str(int(math.floor(score))))
    win.refresh()

    for enemy in enemies:
      if (player.get_pos() == enemy.get_pos()):
        board.game_over()
        game_over = True
        break

    score += frame
    time.sleep(frame)

  while key != ord('q'):
    key = win.getch()

curses.wrapper(main)
