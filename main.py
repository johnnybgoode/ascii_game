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
      if (command < 0):
        continue

      command = chr(command)
      commands.put(command)

      if command == 'q':
        game.over = True
        break

  def ai(commands, game):
    while not game.over:
      for enemy in game.enemies:
        enemy.move(game.player.get_pos())

      time.sleep(2)

  def display(commands, game):
    while not game.over:
      try:
        command = commands.get(False)
      except Queue.Empty, e:
        command = ""

      game.win.addstr(game.board.size_y +4, 0, command)

      if command == 'q':
        game.over = True
        break

      game.player.move(command)

      #game.score += 1

      #for enemy in game.enemies:
      #  if (game.player.get_pos() == enemy.get_pos()):
      #    game.board.game_over()
      #    game.over = True
      #    break

      game.win.clear()
      game.board.draw()
      win.addstr(game.board.size_y + 2, 0, 'Score: ' + str(game.score))

      time.sleep(1)

  #while key != ord('q') and not game_over:
  #  key = win.getch()
  #  if (key < 0):
  #    key = 0


  #  #time.sleep(2)

  #  for enemy in enemies:
  #    enemy.move(player.get_pos())

  #  win.clear()
  #  board.draw()
  #  win.addstr(board.size_y + 2, 0, 'Score: ' + str(score))

  #  for enemy in enemies:
  #    if (player.get_pos() == enemy.get_pos()):
  #      board.game_over()
  #      game_over = True
  #      break

  #  score += 1

  #pdb.set_trace()
  # then start the two threads
  displayer = threading.Thread(None, # always to None since the ThreadGroup class is not implemented yet
                              display, # the function the thread will run
                              None, # doo, don't remember and too lazy to look in the doc
                              (commands, game), # *args to pass to the function
                               {}) # **kwargs to pass to the function

  controler = threading.Thread(None, control, None, (commands, game), {})

  aier = threading.Thread(None, ai, None, (game,), {})

  displayer.start()
  controler.start()
  aier.start()

curses.wrapper(main)
