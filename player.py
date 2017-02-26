from character import Character

class Player(Character):
  def __init__(self, board):
    self.lookup_char = '@'
    self.player_char = '@'
    self.directions = {
      'a': '<',
      'd': '>',
      'w': '^',
      's': 'v',
    }
    Character.__init__(self, board)

  def move(self, key):
    new_x = self.pos[0]
    new_y = self.pos[1]

    if (key not in self.directions):
      return

    if (key == 'a'):
      new_x -= 1

    elif (key == 'd'):
      new_x += 1

    elif (key == 's'):
      new_y += 1

    elif (key == 'w'):
      new_y -= 1

    self.player_char = self.directions[key]

    Character.move(self, (new_x, new_y))

