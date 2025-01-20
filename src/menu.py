from settings import *

class MenuRenderer:
  def __init__(self, engine):
    self.engine = engine
  
  def draw(self):
    if pr.gui_button([24,24,120,30],b"Hello"):
      print("click")
    #pass