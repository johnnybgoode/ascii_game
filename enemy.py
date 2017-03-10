from character import Character
from path import Path
import random

class Enemy(Character):
  def __init__(self, board, level):
    self.lookup_char = 'E'
    self.player_char = '*'
    self.level = level
    self.delay = level

    Character.__init__(self, board)

  def move(self, player_pos):
    self.delay -= 1

    if (self.delay == 0):
      path = Path(self.pos, player_pos, self.board)

      path = path.get_path()

      new_pos = path[0]

      Character.move(self, new_pos)

      self.delay = self.level

  def get_path(self, player_pos):
    board = self.board.get_board()
    open_cells = {}
    closed_cells = []

    return move_step(player_pos)

  def where(self):
    board = self.board.get_board()
    i = 0
    max_tries = 13
    x = random.randint(1, len(board[0]) - 1)
    y = random.randint(1, len(board) - 1)

    while True:
      if (i >= max_tries):
        break

      if self.board.is_open((x, y)):
        self.pos = (x, y)
        self.board.draw_cell(self.pos, self.player_char)
        return

      if x < (len(board[0]) - 1):
        x += 1
      elif y < len(board):
        x = 1
        y += 1
      else:
        break

      i += 1

    self.pos = False
