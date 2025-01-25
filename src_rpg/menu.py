from settings import *
from entity import CreatureType
class MenuRenderer:

  def __init__(self, engine):
    self.engine = engine
    self.is_menu = False
  
  def draw(self):

    # if pr.gui_button([24,24,120,30],b"Hello"):
    #   print("click")

    if pr.gui_button([24,24+30*0,120,30],b"attack"):
      #print("click")
      self.action_attack()

    if pr.gui_button([24,24+30*1,120,30],b"defence"):
      #print("click")
      self.action_defense()

    if pr.gui_button([24,24+30*2,120,30],b"skill"):
      #print("click")
      self.action_skill()

    if pr.gui_button([24,24+30*3,120,30],b"test"):
      #print("click")
      self.action_test()

    if pr.gui_button([24+160,24+30*3,120,30],b"mob attack"):
      #print("click")
      self.mob_attack()

    self.draw_debug_entities()
    #
    
  def draw_debug_entities(self):
    entities = self.engine.entity_m.entities
    party_count = 0
    for party_m in range(len(entities)):
      if entities[party_m].TYPE == CreatureType.PLAYER:
        pr.draw_text(f"Name: "+entities[party_m].name,100,200,12, pr.BLUE )
        pr.draw_text(f"HP:"+str(entities[party_m].stats.health) + "/"+ str(entities[party_m].stats.max_health),100,200+12,12, pr.BLUE )
        party_count += 1
        #pass

    oppenont_count = 0
    for party_m in range(len(entities)):
      if entities[party_m].TYPE == CreatureType.MOB:
        pr.draw_text(f"Name: "+entities[party_m].name,300,200,12, pr.RED )
        pr.draw_text(f"HP:"+str(entities[party_m].stats.health) + "/"+ str(entities[party_m].stats.max_health),300,200+12,12, pr.RED )
        oppenont_count += 1
        #pass

  def mob_attack(self):
    print("mob_attack ..")
    self.engine.entity_m.mob_attack()
    #pass

  def action_attack(self):
    print("action_attack")
    self.engine.entity_m.user_attack()
    #pass

  def action_defense(self):
    print("action_defense")
    #pass

  def action_skill(self):
    print("action_skill")
    #pass

  def action_test(self):
    print("action_test")
    self.engine.entity_m.entities_stats()
    #pass