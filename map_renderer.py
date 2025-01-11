from settings import *

class MapRenderer:
  def __init__(self, engine):
    self.engine = engine
    
  def draw(self):
    pass

  @staticmethod
  def get_bounds(segments: list[tuple[vec2]]):
    pass