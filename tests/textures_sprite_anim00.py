from pyray import *

def main():
  # Initialization
  SCREEN_WIDTH = 800
  SCREEN_HEIGHT = 450

  init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "raylib [texture] example - sprite anim")

  scarfy = load_texture("resources/scarfy.png")  # Texture loading

  frame_width = scarfy.width / 6
  frame_height = scarfy.height

  # Source rectangle (part of the texture to use for drawing)
  source_rec = Rectangle(0, 0, frame_width, frame_height)

  # Destination rectangle (screen rectangle where drawing part of texture)
  dest_rec = Rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, frame_width*2, frame_height*2)

  # Origin of the texture (rotation/scale point), it's relative to destination rectangle size
  origin = Vector2(frame_width, frame_height)

  # Main game loop
  while not window_should_close():  # Detect window close button or ESC key
    begin_drawing()

    clear_background(RAYWHITE)


    draw_texture(scarfy, int(SCREEN_WIDTH/2 - scarfy.width/2), int(SCREEN_HEIGHT/2 - scarfy.height/2), WHITE)

    draw_text("this IS a texture loaded from an image!", 300, 370, 10, GRAY)

    end_drawing()

  # De-Initialization
  close_window()  # Close window and OpenGL context















if __name__ == '__main__':
    main()