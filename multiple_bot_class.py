from javascript import require, On
import time
from random import randint
mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')
tpsPlugin = require('mineflayer-tps')(mineflayer)

class PyBots():
  def  __init__(self, group_size, serverip, serverport, spawndelay=0):
    bot_list = self.create_bots(serverip, serverport, group_size, spawndelay)
    self.bots = bot_list

  def create_bots(self, ip, port, size, sleep):
    bot_list = []
    for botID in range(size):
      bot = self.create_bot(ip, port, botID)
      bot_list.append(bot)
      self.wait_on_spawn(bot)
      time.sleep(sleep)
    return bot_list

  def wait_on_spawn(self, bot):
      while(True):
        if(not bot.player):
          time.sleep(1)
        else:
          break

  def create_bot(self, ip, port, name):
    name = str(name)
    port = int(port)
    ip = str(ip)
    bot = mineflayer.createBot({
      'host': ip,
      'port': port,
      'username': name
    })
    bot.loadPlugin(pathfinder.pathfinder)
    return bot

  def random_move_swarm(self):
    for bot in self.bots:
      direction = self.random_direction()
      self.move_bot(bot, direction)

  def move_bot(self, bot, direction):
    #print(direction)
    try:
      bot.setControlState(direction, True)
    except:
      print(direction)
      pass

  def random_direction(self):
    options = ['forward', 'back', 'left', 'right']
    option = randint(0,3)
    return options[option]

  def loop_random(self, period=10):
    while(True):
      self.random_move_swarm()
      time.sleep(period)