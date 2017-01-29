import pdb
import math

class Board:
  def __init__(self, win, filename):
    self.wall_char = '#'
    self.empty_char = ' '
    self.path_char = '.'
    self.debug = False

    self.win = win
    board_file = open(filename, 'r')
    self.board = [list(line) for line in board_file]
    self.size_y = len(self.board)
    self.size_x = len(self.board[0])

  def draw(self):
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        self.win.addstr(i, j, str(self.board[i][j]))

        if (self.debug):
          self.win.addstr(self.size_y, j, str(j)[-1])
          self.win.addstr(i, self.size_x, str(i)[-1])

    if (self.debug):
      self.win.move(i+2, 0)
      self.win.insertln()


  def move_player(self, old_pos, new_pos, player_char):
    self.board[old_pos[1]][old_pos[0]] = self.empty_char
    self.board[new_pos[1]][new_pos[0]] = player_char

  def game_over(self):
    game_over = 'Game Over!'
    x = math.floor((self.size_x / 2) - (len(game_over) / 2))
    self.win.addstr(self.size_y, int(x), game_over)

  def draw_path(self, pos):
    self.board[pos[1]][pos[0]] = self.path_char
    self.win.clear()
    self.draw()

  def clear_path(self, pos):
    self.board[pos[1]][pos[0]] = self.empty_char
    self.win.clear()
    self.draw()

  def is_wall(self, cell):
    return (self.board[cell[1]][cell[0]] == self.wall_char)

  def get_board(self):
    return self.board
