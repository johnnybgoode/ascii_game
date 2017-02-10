class Game:
  def __init__(self):
    self.score = 0
    self.over = False

  def set_board(self, board):
    self.board = board

  def set_player(self, player):
    self.player = player

  def set_enemies(self, enemies):
    self.enemies = enemies

