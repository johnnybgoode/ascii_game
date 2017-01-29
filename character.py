class Character:
  def __init__(self, board):
    self.board = board
    self.where()

  def move(self, new_pos):
    if (self.board.is_wall(new_pos)):
      return

    self.board.move_player(self.pos, new_pos, self.player_char)
    self.pos = new_pos

  def get_pos(self):
    return self.pos

  def where(self):
    board = self.board.get_board()
    for i in range(len(board)):
      for j in range(len(board[i])):
        if (board[i][j] == self.lookup_char):
          self.pos = (j, i)
          board[i][j] = self.player_char
          return
