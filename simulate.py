from __builtins__ import *
from common import *

def stats(filename, simGlobals = {}):
  simUnlocks = {} # Unlocks
  simItems = {} # { Items.Power: 1000000000 }
  seed = -1
  speedup = 1

  times = []

  for _ in range(1):
    time = simulate(filename, simUnlocks, simItems, simGlobals, seed, speedup)
    times.append(time)

  quick_print("Avg:", secondsToString(sum(times) / len(times)))
  quick_print("Min:", secondsToString(minOf(times)))
  quick_print("Max:", secondsToString(maxOf(times)))


# tests = [32]
# for i in range(10):
#   param = i+8 # ((i+1) / 100)+0.6

#   quick_print("Testing:", param)
#   stats("main", { "param": param })
#   quick_print("")
  
stats("fastest_reset")

