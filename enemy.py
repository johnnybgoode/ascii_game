from character import Character
from path import Path
import pdb

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
