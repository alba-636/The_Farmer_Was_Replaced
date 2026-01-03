from __builtins__ import *
from common import *

quick_print("Hello, World")

upgrade = Unlocks.Speed
quick_print(upgrade, get_cost(upgrade), num_unlocked(upgrade))

def try_unlock(upgrade):
    needs = get_cost(upgrade)
    if needs == None:
        return
    can_unlock = True
    for item in needs:
        if num_items(item) < needs[item]:
            can_unlock = False
    if can_unlock:
        unlock(Unlocks.Speed)

while True:
    
    try_unlock(Unlocks.Speed)

    harvest()