import curses
from board import Board
from player import Player
from enemy import Enemy

def main(win):
  board = Board(win, 'board.txt')

  game_over = False
  score = 0

  player = Player(board)
  enemies = [
    Enemy(board, 9),
    Enemy(board, 8),
  ]

  win.clear()
  board.draw()
  win.addstr(board.size_y + 2, 0, 'Score: ' + str(score))

  key = 0

  while key != ord('q') and not game_over:
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
        game_over = True
        break

    score += 1

  while key != ord('q'):
    key = win.getch()

curses.wrapper(main)
