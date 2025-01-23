from settings import *

from map_renderer import MapRenderer
from menu import MenuRenderer
from input_handler import InputHandler
from entity import Entity_Management

class Engine:
  def __init__(self, app):
    self.app = app
    self.map_renderer = MapRenderer(self)
    self.menu_renderer = MenuRenderer(self)
    self.input_handler = InputHandler(self)
    self.entity_m = Entity_Management(self)
    #pass

  def update(self):
    pass

  def draw_2d(self):
    self.map_renderer.draw()
    self.menu_renderer.draw()
    #pass

  def draw_3d(self):

    self.input_handler.update()
    #pass

  def draw(self):
    pr.begin_drawing()
    #
    pr.clear_background(pr.RAYWHITE)
    #pr.clear_background(pr.RAYWHITE)
    #
    self.draw_2d()
    self.draw_3d()
    #
    pr.end_drawing()