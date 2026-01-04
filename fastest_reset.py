from __builtins__ import *
from common import *

quick_print("Hello, World")

upgrades_order = [
    { "upgrade": Unlocks.Speed, "num": 1 },
    { "upgrade": Unlocks.Expand, "num": 1 },
    { "upgrade": Unlocks.Plant, "num": 1 },
    { "upgrade": Unlocks.Speed, "num": 2 },
    { "upgrade": Unlocks.Carrots, "num": 1 },
    { "upgrade": Unlocks.Speed, "num": 3 },
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

    need = get_cost_of(upgrade)
    if need != None:
        return need

    result = unlock(upgrade)
    if result == True:
        upgrades_order.pop(0)
        quick_print("Unlocked", upgrade, num)

def item_to_entitie(item):
    map = {
        Items.Carrot: Entities.Carrot,
    }
    if item not in map:
        return item
    return map[item]

def get_cost_of(item, amount = 1):
    denied_list = [None, Items.Hay, Items.Wood]
    if item in denied_list:
        return None

    needs = get_cost(item_to_entitie(item))
    if needs == None:
        return None
    for item in needs:
        total_amount = needs[item] * amount
        if num_items(item) < total_amount:
            return (item, total_amount)
    return None

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
        plant(Entities.Bush)

# def farm_carrots():
#     if get_ground_type()

need = None
while True:
    if num_unlocked(Unlocks.Leaderboard) > 0:
        break

    need = try_unlock()
    if need == None:
        continue
    (item, amount) = need
    # Some resources needs other resources to be planted.
    need = get_cost_of(item, amount)
    if need != None:
        (item, amount) = need

    if item == Items.Hay:
        farm_hay()
    elif item == Items.Wood:
        farm_wood()
    else:
        quick_print("Needed:", item, amount)

    