import random, math, time

from board import Board
from player import Player
from enemy import Enemy

class Game:
  def __init__(self, win):
    self.board = Board("board.txt")
    self.framerate = 60 # frames per second
    self.frame = 1.0 / float(self.framerate)
    self.ticks = 0
    self.seconds = 0
    self.over = False
    self.win = win;

    self.win.nodelay(True)

    self.player = Player(self.board)
    self.enemies = []

  def play(self):
    self.draw()

    key = 0

    while key != ord('q') and not self.over:
      key = self.win.getch()

      if key > 0:
        self.player.move(chr(key))

      for enemy in self.enemies:
        enemy.move(self.player.get_pos())

      self.draw()

      for enemy in self.enemies:
        if (self.player.get_pos() == enemy.get_pos()):
          self.over = True
          self.show_message('Game Over', (0,2))
          break

      self.show_message('Score: ' + str(self.seconds))

      self.tick()


    while key != ord('q'):
      key = self.win.getch();

  def tick(self):
    self.ticks += 1

    if (self.ticks % self.framerate == 0):
      self.seconds += 1
      self.ticks = 0

    time.sleep(self.frame)

  def spawn(self, n):
    i = 0;
    while i < n:
      enemy = Enemy(self.board, 60)
      if not enemy.get_pos():
        del enemy
        continue
      self.enemies.append(enemy)
      i += 1

  def draw(self):
    board = self.board.get_board()
    for i in range(self.board.size_y):
      for j in range(self.board.size_x):
        self.win.addstr(i, j, str(board[i][j]))
    self.win.refresh()

  def show_message(self, message, offset = (0,0)):
    self.win.move(self.board.size_y + 1, 0)
    self.win.clrtoeol()

    x = math.floor((self.board.size_x / 2) - (len(message) / 2))
    x += offset[0]
    y = self.board.size_y + offset[1]
    self.win.addstr(self.board.size_y, int(x), str(message))
