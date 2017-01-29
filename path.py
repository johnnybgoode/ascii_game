import pdb

class Path:
  def __init__(self, start, end, steps, board):
    self.path = []

    self.start = start
    self.end = end
    self.steps = steps
    self.board = board

    self.open_cells = {}
    self.closed_cells = []

    self.g_lo = 10
    self.g_hi = 12

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

  def get_path(self):
    self.path_step(self.start, self.end)

    return self.path

  def path_step(self, start, end):
    next_steps = []

    if (self.steps == 0):
      return

    for direction in self.directions:
      cell = (start[0] + direction[0], start[1] + direction[1])

      if (cell == end):
        self.path.append(cell)
        return

      if (self.board.is_wall(cell)):
        self.closed_cells.append(cell)

      if (cell in self.closed_cells):
        continue

      next_steps.append(cell)

      self.open_cells[cell] = {
        'parent': start,
        'g': self.calc_g(direction, start),
        'h': self.calc_h(cell, self.end),
      }


    cell = self.min_f(next_steps)

    # @todo preserve scores to allow path to be modified by
    # following iterations
    #
    #if (start in self.open_cells and cell in self.open_cells):
    #  if (self.open_cells[cell]['parent'] == self.open_cells[start]['parent']):
    #    self.path.pop()
    #    del self.open_cells[start]
    #    #self.board.clear_path(start)

    self.closed_cells.append(start)

    if (start in self.open_cells):
      del self.open_cells[start]

    self.path.append(cell)
    self.board.draw_path(cell)

    self.steps -= 1

    return self.path_step(cell, end)

  def min_f(self, cells):
    min_f = None
    ret_cell = None

    for cell in cells:
      f = self.open_cells[cell]['g'] + self.open_cells[cell]['h']
      if (min_f == None or f < min_f):
        min_f = f
        ret_cell = cell

    return ret_cell


  def calc_g(self, cell, parent):
    g = self.g_lo if ((abs(cell[0]) + abs(cell[1])) > 1) else self.g_hi

    return self.open_cells[parent]['g'] + g if (parent in self.open_cells) else g

  def calc_h(self, from_cell, to_cell):
    return abs(to_cell[0] - from_cell[0]) + abs(to_cell[1] - from_cell[1])
