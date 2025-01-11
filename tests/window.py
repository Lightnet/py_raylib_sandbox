# 
# https://electronstudio.github.io/raylib-python-cffi/pyray.html
# https://electronstudio.github.io/raylib-python-cffi/raylib.html
# 
from pyray import *
#import pyray as pr
#from pyray.raygui import *
#from pyray import raylib
#print(dir(raylib))
#print(dir(pr))


def init_game():

  showMessageBox = False

  camera = ffi.new("struct Camera3D *", [[18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0])

  init_window(800, 450, "Hello")

  while not window_should_close():
      begin_drawing()
      clear_background(WHITE)
      draw_text("Hello world", 190, 200, 20, VIOLET)

      # if raylib.GuiButton([24, 24, 120, 30], b"#191#Show Message"):
      #     print("click...")
      if gui_button([24, 24, 120, 30], b"#191#Show Message"):
        print("click...")

      end_drawing()
  close_window()

def main():
    print("Hello World!")
    init_game()

if __name__ == "__main__":
    main()