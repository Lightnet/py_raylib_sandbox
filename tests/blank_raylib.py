# 
# https://www.raylib.com/cheatsheet/cheatsheet.html
# 
# Image ImageCopy(Image image); 
# 
# https://www.raylib.com/examples/shaders/loader.html?name=shaders_texture_drawing
# 
# 
# 
from pyray import *
import math

def main():
  currentFrame = 0
  framesCounter = 0
  framesSpeed = 8
  # Initialization
  SCREEN_WIDTH = 1024
  SCREEN_HEIGHT = 720

  MAX_FRAME_SPEED = 15
  MIN_FRAME_SPEED = 1

  TILEMAP_X = 49
  TILEMAP_Y = 22

  init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "raylib [texture] example - sprite anim")

  set_target_fps(60)                 # Set our game to run at 60 frames-per-second

  #texture = load_texture("resources/colored-transparent_packed.png")  # Texture loading
  #position = Vector2(20.0, 20.0)
  #frameRec = Rectangle(0.0, 0.0, texture.width/TILEMAP_X, texture.height/TILEMAP_Y)

  #imBlank = gen_image_color(1024, 1024, BLANK)
  imBlank = gen_image_color(64, 64, RED)
  #print(":::",imBlank)
  textureBlank = load_texture_from_image(imBlank)
  unload_image(imBlank)

  # image = load_image("resources/colored-transparent_packed.png")  # Texture loading
  # image_texture = load_texture_from_image(image)
  # unload_image(image)

  while not window_should_close():  # Detect window close button or ESC key

    begin_drawing()
    clear_background(RAYWHITE)
    #draw_texture(textureBlank, 0, 0, WHITE);  # Drawing BLANK texture, all magic happens on shader
    draw_texture(textureBlank, 0, 0, WHITE);  # Drawing BLANK texture, all magic happens on shader
    #draw_texture(texture, 0, 0, WHITE);  # Drawing BLANK texture, all magic happens on shader
    #draw_texture(image_texture, 0, 0, WHITE);  # Drawing BLANK texture, all magic happens on shader
    end_drawing()

  close_window()  # Close window and OpenGL context

if __name__ == '__main__':
  main()