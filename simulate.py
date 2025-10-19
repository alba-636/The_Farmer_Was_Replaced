from __builtins__ import *
from common import *

def stats(filename = "leaderboard", simGlobals = {}):
  simUnlocks = Unlocks
  simItems = { Items.Power: 1000000000 }
  seed = -1
  speedup = 9999

  times = []

  for _ in range(100):
    time = simulate(filename, simUnlocks, simItems, simGlobals, seed, speedup)
    times.append(time)

  quick_print("Avg:", secondsToString(sum(times) / len(times)))
  quick_print("Min:", secondsToString(minOf(times)))
  quick_print("Max:", secondsToString(maxOf(times)))


# tests=[3, 4, 5, 6, 7, 8, 9, 10, 11]
# for i in range(30):
#   param = ((i) / 100)+0.1

#   quick_print("Testing:", param)
#   stats("main", { "param": param })
#   quick_print("")
  
# stats("farm")

