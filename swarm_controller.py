from multiple_bot_class import PyBots
import time


if __name__ == "__main__":
  port_range = range(25565,25565+12)
  swarms = []
  for port in port_range:
    mybots = PyBots(20, '192.168.1.126', port, 1)
    mybots.loop_random(period=1)
    swarms.append(mybots)
    time.sleep(20)

  while(True):
    time.time()
