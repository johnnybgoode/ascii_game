class Board:
  def __init__(self, filename):
    self.wall_char = '#'
    self.empty_char = ' '

    board_file = open(filename, 'r')
    self.board = [list(line) for line in board_file]
    self.size_y = len(self.board)
    self.size_x = len(self.board[0])
    self.directions = [
        (-1, -1),
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
      ]

  def move_player(self, old_pos, new_pos, player_char):
    if (self.is_wall(new_pos)):
      return False

    self.set_cell(old_pos, self.empty_char)
    self.set_cell(new_pos, player_char)

    return True

  def get_open_neighbors(self, cell):
    neighbors = []
    for dir in self.directions:
      neighbor = (cell[0] + dir[0], cell[1] + dir[1])
      if (self.is_wall(neighbor)):
        continue

      neighbors.append(neighbor)

    return neighbors


  def set_cell(self, cell, char):
    self.board[cell[1]][cell[0]] = char

  def is_wall(self, cell):
    return (self.board[cell[1]][cell[0]] == self.wall_char)

  def is_open(self, cell):
    return self.board[cell[1]][cell[0]] == self.empty_char

  def get_size(self):
    return self.size_x * self.size_y

  def get_board(self):
    return self.board
