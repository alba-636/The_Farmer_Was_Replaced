# From: Alba-636
# Leaderboard: Hay
# Best time: 01:53:631
# At: 2025-10-19

# Avg: 1:53.49
# Min: 1:52.96
# Max: 1:54.28

from __builtins__ import *
from common import *

set_world_size(30)

def farm(initialX, initialY, index):
  def defaultMoves():
    move(North)
    plant(Entities.Bush)
    move(North)
    plant(Entities.Bush)
    move(North)
    plant(Entities.Bush)
    move(North)
    move(East)
    plant(Entities.Bush)
    move(East)
    plant(Entities.Bush)
    move(East)
    plant(Entities.Bush)
    move(East)
    plant(Entities.Bush)
    move(South)
    plant(Entities.Bush)
    move(South)
    plant(Entities.Bush)
    move(South)
    plant(Entities.Bush)
    move(South)
    plant(Entities.Bush)
    move(West)
    plant(Entities.Bush)
    move(West)
    plant(Entities.Bush)
    move(West)
    plant(Entities.Bush)
    move(North)
    plant(Entities.Bush)
    move(North)
    plant(Entities.Bush)
    move(North)
    plant(Entities.Bush)
    move(East)
    plant(Entities.Bush)
    move(East)
    plant(Entities.Bush)
    move(South)
    move(South)
    plant(Entities.Bush)
    move(West)
    plant(Entities.Bush)
    move(North)

  def moves2():
    move(North)
    plant(Entities.Bush)
    move(North)
    plant(Entities.Bush)
    move(North)
    plant(Entities.Bush)
    move(North)
    move(East)
    plant(Entities.Bush)
    move(East)
    plant(Entities.Bush)
    move(North)
    plant(Entities.Bush)
    move(East)
    plant(Entities.Bush)
    move(South)
    plant(Entities.Bush)
    move(East)
    plant(Entities.Bush)
    move(South)
    plant(Entities.Bush)
    move(South)
    plant(Entities.Bush)
    move(South)
    plant(Entities.Bush)
    move(South)
    plant(Entities.Bush)
    move(West)
    plant(Entities.Bush)
    move(West)
    plant(Entities.Bush)
    move(West)
    plant(Entities.Bush)
    move(North)
    plant(Entities.Bush)
    move(North)
    plant(Entities.Bush)
    move(North)
    plant(Entities.Bush)
    move(East)
    plant(Entities.Bush)
    move(East)
    plant(Entities.Bush)
    move(South)
    move(South)
    plant(Entities.Bush)
    move(West)
    plant(Entities.Bush)
    move(North)

  def moves1():
    move(North)
    plant(Entities.Bush)
    move(North)
    plant(Entities.Bush)
    move(North)
    plant(Entities.Bush)
    move(North)
    move(East)
    plant(Entities.Bush)
    move(East)
    plant(Entities.Bush)
    move(East)
    plant(Entities.Bush)
    move(East)
    plant(Entities.Bush)
    move(East)
    move(South)
    plant(Entities.Bush)
    move(South)
    plant(Entities.Bush)
    move(South)
    plant(Entities.Bush)
    move(South)
    move(West)
    plant(Entities.Bush)
    move(West)
    plant(Entities.Bush)
    move(West)
    plant(Entities.Bush)
    move(West)
    plant(Entities.Bush)
    move(North)
    plant(Entities.Bush)
    move(North)
    plant(Entities.Bush)
    move(North)
    plant(Entities.Bush)
    move(East)
    plant(Entities.Bush)
    move(East)
    plant(Entities.Bush)
    move(East)
    plant(Entities.Bush)
    move(South)
    plant(Entities.Bush)
    move(South)
    plant(Entities.Bush)
    move(West)
    plant(Entities.Bush)
    move(West)
    plant(Entities.Bush)
    move(North)

  goToPosition(initialX, initialY)

  if index == 31:
    moves1()
  elif index in [29, 28, 27, 26]:
    moves2()
  else:
    defaultMoves()

  step = 0
  while True:
    plantType, (_, _) = get_companion()
    if can_harvest():
      harvest()
      if num_items(Items.Hay) >= 2000000000:
        break
    elif plantType != Entities.Bush:
      harvest()
    else:
      if get_water() < 0.67:
        use_item(Items.Water, 4)
      if step == 0:
        move(East)
        step = 1
      else:
        move(West)
        step = 0

def drone0():
  farm(0,0,0)
def drone1():
  farm(5,0,1)
def drone2():
  farm(10,0,2)
def drone3():
  farm(15,0,3)
def drone4():
  farm(20,0,4)
def drone5():
  farm(25,0,5)
def drone6():
  farm(0,5,6)
def drone7():
  farm(5,5,7)
def drone8():
  farm(10,5,8)
def drone9():
  farm(15,5,9)
def drone10():
  farm(20,5,10)
def drone11():
  farm(25,5,11)
def drone12():
  farm(0,10,12)
def drone13():
  farm(5,10,13)
def drone14():
  farm(10,10,14)
def drone15():
  farm(15,10,15)
def drone16():
  farm(20,10,16)
def drone17():
  farm(25,10,17)
def drone18():
  farm(0,15,18)
def drone19():
  farm(5,15,19)
def drone20():
  farm(10,15,20)
def drone21():
  farm(15,15,21)
def drone22():
  farm(20,15,22)
def drone23():
  farm(25,15,23)
def drone24():
  farm(0,20,24)
def drone25():
  farm(5,20,25)
def drone26():
  farm(10,20,26)
def drone27():
  farm(15,20,27)
def drone28():
  farm(20,20,28)
def drone29():
  farm(25,20,29)
def drone30():
  farm(0,25,30)
def drone31():
  farm(5,25,31)

spawn_drone(drone0)
spawn_drone(drone1)
spawn_drone(drone2)
spawn_drone(drone3)
spawn_drone(drone4)
spawn_drone(drone5)
spawn_drone(drone6)
spawn_drone(drone7)
spawn_drone(drone8)
spawn_drone(drone9)
spawn_drone(drone10)
spawn_drone(drone11)
spawn_drone(drone12)
spawn_drone(drone13)
spawn_drone(drone14)
spawn_drone(drone15)
spawn_drone(drone16)
spawn_drone(drone17)
spawn_drone(drone18)
spawn_drone(drone19)
spawn_drone(drone20)
spawn_drone(drone21)
spawn_drone(drone22)
spawn_drone(drone23)
spawn_drone(drone24)
spawn_drone(drone25)
spawn_drone(drone26)
spawn_drone(drone27)
spawn_drone(drone28)
spawn_drone(drone29)
spawn_drone(drone30)
drone31()
