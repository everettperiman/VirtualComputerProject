from javascript import require, On
import time
from random import randint
mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')
tpsPlugin = require('mineflayer-tps')(mineflayer)

RANGE_GOAL = 1
BOT_USERNAME = 'tps_bot'

def create_bot(username):
  username = str(username)
  bot = mineflayer.createBot({
    'host': '192.168.1.126',
    'port': 25570,
    'username': username
  })
  bot.loadPlugin(pathfinder.pathfinder)
  bot.loadPlugin(tpsPlugin)
  return bot

def attackEntity(bot):
    entity = bot.nearestEntity()
    if(not entity):
      bot.chat('No Entities')
    else:
      bot.chat('Attacking')
      bot.attack(entity)
    
def printTPS(bot):
  print(bot.getTps())

def moveBot(bot, direction):
  print(direction)
  try:
    bot.setControlState(direction, True)
  except:
    pass

def randomMoveBot(bot):
  options = ['forward', 'back', 'left', 'right']
  option = randint(0,3)
  moveBot(bot,options[option])

def cycle_bots(bot):
  pass

if __name__ == "__main__":
  bot_names = [i for i in range(20)]
  print(bot_names)
  bot_list = []
  for i in bot_names:
    new_bot = create_bot(i)
    bot_list.append(new_bot)
  while(True):
    for i in bot_list:
      randomMoveBot(i)
      #printTPS(i)
    time.sleep(10)
    