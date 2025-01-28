from settings import *
from entity import CreatureType

class MenuRenderer:

  def __init__(self, engine):
    self.engine = engine
    self.is_menu = False
  
  def draw(self):

    # if pr.gui_button([24,24,120,30],b"Hello"):
    #   print("click")
    self.draw_current_turn()
    self.menu_battle()
    self.draw_debug_entities()
    #

  def menu_battle(self):
    # if pr.gui_button([24,24+30*0,120,30],b"attack"):
    #   #print("click")
    #   self.action_attack()
    menu_height = WIN_HEIGHT - 30*4 - 4
    if pr.gui_button([24,menu_height,120,30],b"Attack"):
      #print("click")
      self.action_attack()

    menu_height = WIN_HEIGHT - 30*3 - 4
    if pr.gui_button([24,menu_height,120,30],b"Defend"):
      #print("click")
      self.action_defense()

    menu_height = WIN_HEIGHT - 30*2 - 4
    if pr.gui_button([24,menu_height,120,30],b"Skill(s)"):
      #print("click")
      self.action_skill()

    menu_height = WIN_HEIGHT - 30*1 - 4
    if pr.gui_button([24,menu_height,120,30],b"Test"):
      #print("click")
      self.action_test()

    menu_width = WIN_WIDTH - 120*1-4
    menu_height = WIN_HEIGHT - 30*1-4
    if pr.gui_button([menu_width,menu_height,120,30],b"mob attack"):
      #print("click")
      self.mob_attack()

    
  def draw_debug_entities(self):
    entities = self.engine.entity_m.entities
    party_count = 0
    for party_m in range(len(entities)):
      if entities[party_m].TYPE == CreatureType.PLAYER:
        # pr.draw_text(f"Name: "+entities[party_m].name,100,200,12, pr.BLUE )
        # pr.draw_text(f"HP:"+str(entities[party_m].stats.health) + "/"+ str(entities[party_m].stats.max_health),100,200+12,12, pr.BLUE )
        # pr.draw_text(f"TP:"+str(entities[party_m].stats.tp) + "/"+ str(entities[party_m].stats.tp_cap),100,200+12*2,12, pr.BLUE )
        self.draw_text_entity_info(entities[party_m], 20, 20 )
        party_count += 1
        #pass

    oppenont_count = 0
    oppenont_pos_x = WIN_WIDTH - 200
    oppenont_pos_y = WIN_HEIGHT - 200
    for party_m in range(len(entities)):
      if entities[party_m].TYPE == CreatureType.MOB:
        # pr.draw_text(f"Name: "+entities[party_m].name,300,200,12, pr.RED )
        # pr.draw_text(f"HP:"+str(entities[party_m].stats.health) + "/"+ str(entities[party_m].stats.max_health),300,200+12,12, pr.RED )

        self.draw_text_entity_info(entities[party_m], oppenont_pos_x, 20, pr.RED )
        oppenont_count += 1
        #pass

  def draw_current_turn(self):
    pr.draw_text(f"Current Turn: ", 4 , 4, 12, pr.GRAY )

  def draw_text_entity_info(self, _entity, _x, _y, _color=pr.BLUE):
    pr.draw_text(f"Name: "+_entity.name,_x, _y,12, _color )
    pr.draw_text(f"HP:"+str(_entity.stats.health) + "/"+ str(_entity.stats.max_health),_x,_y+12,12, _color )
    pr.draw_text(f"TP:"+str(_entity.stats.tp) + "/"+ str(_entity.stats.tp_cap),_x,_y+12*2,12, _color )
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