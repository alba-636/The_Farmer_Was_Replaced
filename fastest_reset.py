from __builtins__ import *
from common import *

quick_print("Hello, World")

upgrades_order = [
    { "upgrade": Unlocks.Speed, "num": 1 },
    { "upgrade": Unlocks.Expand, "num": 1 },
    { "upgrade": Unlocks.Plant, "num": 1 },
    { "upgrade": Unlocks.Speed, "num": 2 },
]

def try_unlock():
    if len(upgrades_order) == 0:
        return
    upgrade_dict = upgrades_order[0]
    upgrade = upgrade_dict["upgrade"]
    num = upgrade_dict["num"]

    if num_unlocked(upgrade) >= num:
        upgrades_order.pop(0)
        return

    needs = get_cost(upgrade)
    if needs == None:
        return
    for item in needs:
        if num_items(item) < needs[item]:
            return (item, needs[item])

    result = unlock(upgrade)
    if result == True:
        upgrades_order.pop(0)
        quick_print("Unlocked", upgrade, num)

# Function to farm a specific resources.
def farm_hay():
    if get_ground_type() != Grounds.Grassland:
        till()
    if can_harvest():
        harvest()

def farm_wood():
    if get_ground_type() != Grounds.Grassland:
        till()

    if can_harvest():
        harvest()
        plant(Entities.Tree)

need = None
while True:
    if num_unlocked(Unlocks.Leaderboard) > 0:
        break

    need = try_unlock()

    if need == None:
        continue

    if need[0] == Items.Hay:
        farm_hay()
    elif need[0] == Items.Wood:
        farm_wood()

    