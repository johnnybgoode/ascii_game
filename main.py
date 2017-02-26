import curses
import threading, time, Queue

import pdb

from board import Board
from player import Player
from enemy import Enemy
from game import Game

def main(win):
  board = Board(win, 'board.txt')

  player = Player(board)
  enemies = [
    Enemy(board, 9),
    Enemy(board, 8),
  ]

  game = Game()
  game.set_board(board)
  game.set_player(player)
  game.set_enemies(enemies)
  game.win = win

  win.nodelay(True)
  win.clear()
  board.draw()
  win.addstr(board.size_y + 2, 0, 'Score: ' + str(game.score))

  commands = Queue.Queue(0)

  def control(commands, game):
    while not game.over:
      command = game.win.getch()
      if command < 0:
        continue

      command = chr(command)
      commands.put(command)

      #game.score += 1

  def enemies(game):
    while not game.over:
      for enemy in game.enemies:
        enemy.move(game.player.get_pos())

      time.sleep(0.4)

  def display(commands, game):
    while not game.over:
      game.win.clear()

      try:
        command = commands.get(False)
      except Queue.Empty, e:
        command = ""

      if command == 'q':
        game.over = True
        break

      game.player.move(command)

      game.win.addstr(game.board.size_y + 4, 0, 'Input: "' + str(command) + '"')

      for enemy in game.enemies:
        if (game.player.get_pos() == enemy.get_pos()):
          game.board.game_over()
          game.over = True
          break

      game.board.draw()
      game.win.refresh()
      #win.addstr(game.board.size_y + 2, 0, 'Score: ' + str(game.score))

      time.sleep(0.2)

  displayer = threading.Thread(None, display, None, (commands, game), {})

  controler = threading.Thread(None, control, None, (commands, game), {})

  ai = threading.Thread(None, enemies, None, (game,), {})

  displayer.start()
  controler.start()
  ai.start()

  if (game.over):
    win.nodelay(False)

    key = 0
    while chr(key) != 'q':
      key = win.getch()

curses.wrapper(main)
