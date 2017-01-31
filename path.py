import pdb
from collections import deque

class Path:
  def __init__(self, start, end, steps, board):
    self.path = deque()
    self.basic_path = []

    self.start = start
    self.goal = end
    self.steps = steps
    self.board = board
    self.steps = self.board.get_size()
    self.found = False

    self.scores = {
      self.start: {
        'parent': None,
        'g': 0,
        'h': 0
      }
    }

    self.open_cells = [
      self.start
    ]
    self.closed_cells = []

    self.g_lo = 10
    self.g_hi = 14

  def get_path(self):
    while not self.found:
      last_step = self.path_step()

    self.build_path(self.start, last_step)

    return self.path

  def path_step(self):
    current = self.min_f()

    if (current == self.goal):
      self.found = True
      return current

    # if a path is not found after n steps eliminate the first choice
    # and start over
    if (self.steps == 0):
      self.closed_cells.append(self.build_path(self.start, current)[1])
      return

    for neighbor in self.board.get_open_neighbors(current):
      if neighbor in self.closed_cells:
        continue

      g = self.scores[current]['g'] + self.calc_g(current, neighbor)

      if (neighbor not in self.scores or g < self.scores[neighbor]['g']):
        self.open_cells.append(neighbor)

        self.scores[neighbor] = {
          'parent': current,
          'g': g,
          'h': self.calc_h(neighbor, self.goal),
        }

    self.steps -= 1

    return self.path_step()

  def build_path(self, start, current):
    if (current == start):
      return

    self.path.appendleft(current)
    self.board.draw_path(current)

    return self.build_path(start, self.scores[current]['parent'])

  def min_f(self):
    min_f = None
    min_cell = None

    for i in range(len(self.open_cells)):
      cell = self.open_cells[i]
      f = self.scores[cell]['g'] + self.scores[cell]['h']

      if (min_f == None or f < min_f):
        min_f = f
        min_i = i

    cell = self.open_cells[i]

    del self.open_cells[i]

    return cell


  def calc_g(self, current, neighbor):
    return self.g_hi if ((abs(current[0]) - abs(neighbor[0])) + (abs(current[1]) - abs(neighbor[1]))) > 1 else self.g_lo

  def calc_h(self, from_cell, to_cell):
    return abs(to_cell[0] - from_cell[0]) + abs(to_cell[1] - from_cell[1])
