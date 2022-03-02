from javascript import require, On
import time
from random import randint
mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')
tpsPlugin = require('mineflayer-tps')(mineflayer)

RANGE_GOAL = 1
BOT_USERNAME = 'tps_bot'

def create_bot(username, port):
  username = str(username)
  bot = mineflayer.createBot({
    'host': '192.168.1.126',
    'port': port,
    'username': username
  })
  bot.loadPlugin(pathfinder.pathfinder)
  bot.loadPlugin(tpsPlugin)
  return bot

def printTPS(bot, port):
  tps = bot.getTps()
  print("TPS: {} Port: {}".format(tps, port))

if __name__ == "__main__":
  port_min = 25565
  port_max = 25565+12
  port_range = list(range(port_min, port_max))

  bot_name = "tps_monitor"
  bot_list = []

  for port in port_range:
    new_bot = create_bot(bot_name, port)
    bot_list.append(new_bot)

  reading_number = 0
  while(True):
    for index, bot in enumerate(bot_list):
      printTPS(bot, port=port_range[index])
    reading_number = reading_number + 1
    print("****Reading #{}****".format(reading_number))
    time.sleep(1)
    