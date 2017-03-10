import pdb
from collections import deque

class Path:
  def __init__(self, start, goal, board):
    self.found = False
    self.start = start
    self.goal = goal
    self.board = board
    self.steps = self.board.get_size()
    self.initial_neighbors = self.board.get_open_neighbors(self.start)

    self.g_lo = 10
    self.g_hi = 14

    self.path = deque()
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

  def get_path(self):
    while not self.found and self.initial_neighbors:
      last_step = self.path_step()

    self.build_path(last_step)

    return self.path

  def path_step(self):
    current = self.min_f()

    if (current == self.goal):
      self.found = True
      return current

    # if a path is not found after n steps eliminate the first choice
    # and start over
    if (self.steps == 0):
      path = self.build_path(current)
      self.closed_cells.append(path[1])
      del self.initial_neighbors[path[1]]
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

  def build_path(self, current):
    if (self.scores[current]['parent'] == None):
      return

    self.path.appendleft(current)

    return self.build_path(self.scores[current]['parent'])

  def min_f(self):
    min_f = None

    for i in range(len(self.open_cells)):
      cell = self.open_cells[i]
      f = self.scores[cell]['g'] + self.scores[cell]['h']

      if (f < min_f or min_f == None):
        min_f = f
        min_i = i

    cell = self.open_cells[min_i]

    del self.open_cells[min_i]

    return cell


  def calc_g(self, current, neighbor):
    return self.g_hi if ((abs(current[0]) - abs(neighbor[0])) + (abs(current[1]) - abs(neighbor[1]))) > 1 else self.g_lo

  def calc_h(self, from_cell, to_cell):
    return abs(to_cell[0] - from_cell[0]) + abs(to_cell[1] - from_cell[1])
