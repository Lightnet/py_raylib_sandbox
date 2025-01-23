# https://www.geeksforgeeks.org/enum-in-python/

from settings import * 
from enum import Enum

class Stats:
  def __init__(self):
    self.health = 100
    self.max_health = 100
    self.attack = 2
    self.defense = 1
    self.str = 1
    self.agi = 1
    self.vit = 1
    pass


class Job:
  def __init__(self,name):
    self.name = name
    self.stats = Stats()
    pass

class CreatureType(Enum):
  NONE = 0
  SPECTATOR = 1
  PLAYER = 2
  NPC = 3
  BEAST = 4
  MOB = 5
  BOSS = 6

class Creature:
  def __init__(self,name, _type=CreatureType['NONE'] ):
    self.name = name
    self.stats = Stats()
    self.TYPE = _type

  def __repr__(self):
    
    return f"""Name: {self.name}
Stats:
  hp:{self.stats.health}
  hpMax:{self.stats.max_health}
  attack:{self.stats.attack}
  defense:{self.stats.defense}
"""

class Entity_Management:
  #
  def __init__(self, engine):
    self.engine = engine
    self.entities = []
    #test
    self.test_add_entities()

  def test_add_entities(self):

    player = Creature("Player",CreatureType.PLAYER)
    print(player)
    # print(player.name)
    # print("health: ",player.stats.health)
    # print("TYPE: ",player.TYPE)
    self.entities.append(player)

    enemy_opponent = Creature("Enemy",CreatureType.MOB)
    print(enemy_opponent)
    # print(enemy_opponent.name)
    # print("health: ",enemy_opponent.stats.health)
    # print("TYPE: ",enemy_opponent.TYPE)
    self.entities.append(enemy_opponent)

    print("self.entities: ", self.entities)

    pass
  # 
  def user_attack(self):
    current_player = None
    current_opponent = None
    for i in range(len(self.entities)):
      if self.entities[i].TYPE == CreatureType.PLAYER:
        print("FOUND PLAYER")
        current_player = self.entities[i]
        break
    for i in range(len(self.entities)):
      if self.entities[i].TYPE == CreatureType.MOB:
        print("FOUND OPPENONT")
        current_opponent = self.entities[i]
        break

    current_opponent.stats.health -= 1

  #pass

  def entities_stats(self):
    for i in range(len(self.entities)):
      print("Entity: ", self.entities[i])

  def mob_attack(self):
    pass

  #
  def create_creature(self):
    pass

if __name__ == '__main__':
  print("test")
  # print("test", CreatureType.NONE)
  
  # print("test", CreatureType.PLAYER)
  print("test", CreatureType['PLAYER'])
  # testType = CreatureType.NONE
  # print("testType", testType)