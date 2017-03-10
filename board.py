import math

class Board:
  def __init__(self, win, filename):
    self.wall_char = '#'
    self.empty_char = ' '
    self.path_char = '.'
    self.show_grid = True

    self.win = win
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

  def draw(self):
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        self.win.addstr(i, j, str(self.board[i][j]))

        if (self.show_grid):
          self.win.addstr(self.size_y, j, str(j)[-1])
          self.win.addstr(i, self.size_x, str(i)[-1])

    if (self.show_grid):
      self.win.move(i+2, 0)
      self.win.insertln()


  def move_player(self, old_pos, new_pos, player_char):
    if (self.is_wall(new_pos)):
      return False

    self.draw_cell(old_pos, self.empty_char)
    self.draw_cell(new_pos, player_char)

    return True

  def get_open_neighbors(self, cell):
    neighbors = []
    for direction in self.directions:
      neighbor = (cell[0] + direction[0], cell[1] + direction[1])
      if (self.is_wall(neighbor)):
        continue

      neighbors.append(neighbor)

    return neighbors

  def show_message(self, message):
    self.win.move(self.size_y + 1, 0)
    self.win.clrtoeol()

    x = math.floor((self.size_x / 2) - (len(message) / 2))
    self.win.addstr(self.size_y, int(x), str(message))

  def draw_path(self, cell):
    # don't draw paths over player
    if (self.board[cell[1]][cell[0]] == self.empty_char):
      self.draw_cell(cell, self.path_char)

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

  #deprecated
  def draw_cell(self, cell, char):
    self.win.addstr(cell[1], cell[0], str(char))

