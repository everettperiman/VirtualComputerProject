from multiple_bot_class import PyBots
import time
import sys

if __name__ == "__main__":
  bots = int(sys.argv[1])
  ip = sys.argv[2]
  port = int(sys.argv[3])
  delay = int(sys.argv[4])
  period = int(sys.argv[5])

  mybots = PyBots(bots, ip, port, delay)
  mybots.loop_random(period=period)
