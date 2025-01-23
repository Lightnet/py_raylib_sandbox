from settings import *

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
    #pass

  def action_attack(self):
    print("action_attack")
    self.engine.entity_m.user_attack()
    pass

  def action_defense(self):
    print("action_defense")
    pass

  def action_skill(self):
    print("action_skill")
    pass

  def action_test(self):
    print("action_test")
    self.engine.entity_m.entities_stats()
    pass