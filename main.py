# 
# Main Entry Point
# 
# 
# https://www.youtube.com/watch?v=vdNrNCqT8No
# 
# https://electronstudio.github.io/raylib-python-cffi/pypr.html
# 
# 
# 
from settings import *
from engine import Engine

class App:
  
  def __init__(self):

    pr.init_window(WIN_WIDTH,WIN_HEIGHT, "BSP Engine")
    pr.set_target_fps(60)
    self.dt = 0.0
    self.engine = Engine(app=self)

  def run(self):
    while not pr.window_should_close():
      self.dt = pr.get_frame_time()
      self.engine.draw()

      # pr.begin_drawing()
      # pr.clear_background(pr.RAYWHITE)
      # pr.end_drawing()
      #pass
    #

    pr.close_window()

  def cleanup(self):
    pass

if __name__ == '__main__':
  app = App()
  app.run()