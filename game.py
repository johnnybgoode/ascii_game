from __future__ import division
import time
import pdb
from board import Board
from player import Player
from enemy import Enemy

class Game:
  def __init__(self, win):
    self.board = Board(win, "board.txt")
    self.framerate = 1/60
    self.over = False
    self.score = 0
    self.win = win;

    self.win.nodelay(True)

    self.player = Player(self.board)
    self.enemies = []

  def play(self):
    win = self.win

    self.board.draw()

    key = 0

    while key != ord('q') and not self.over:
      key = win.getch()

      if key > 0:
        self.player.move(chr(key))

      for enemy in self.enemies:
        enemy.move(self.player.get_pos())

      win.refresh()

      for enemy in self.enemies:
        if (self.player.get_pos() == enemy.get_pos()):
          self.over = True
          break

      self.score += self.framerate

      time.sleep(self.framerate)

    while key != ord('q'):
      key = win.getch();

  def spawn(self, n):
    i = 0;
    while i < n:
      enemy = Enemy(self.board, 60)
      if not enemy.get_pos():
        del enemy
        continue
      self.enemies.append(enemy)
      i += 1

