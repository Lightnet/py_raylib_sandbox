# 
# https://www.raylib.com/cheatsheet/cheatsheet.html
# 
# Image ImageCopy(Image image); 
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

  image_x = 0
  image_y = 0

  init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "raylib [texture] example - sprite anim")

  set_target_fps(60)                 # Set our game to run at 60 frames-per-second

  texture = load_texture("resources/colored-transparent_packed.png")  # Texture loading
  position = Vector2(20.0, 20.0)
  frameRec = Rectangle(0.0, 0.0, texture.width/TILEMAP_X, texture.height/TILEMAP_Y)

  imBlank = gen_image_color(64, 64, RED)
  #textureBlank = load_texture_from_image(imBlank)
  

  im32 = gen_image_color(32, 32, BLUE)
  #textureBlank02 = load_texture_from_image(im32)

  image_draw(imBlank,im32,[0,0,32,32],[0,32,32,32],WHITE)
  textureBlank01 = load_texture_from_image(imBlank)

  unload_image(imBlank)
  unload_image(im32)

  while not window_should_close():  # Detect window close button or ESC key


    begin_drawing()
    clear_background(RAYWHITE)

    #draw_texture(textureBlank, 0, 0, WHITE)  # Drawing BLANK texture, all magic happens on shader
    #draw_texture(textureBlank02, 64, 0, WHITE)

    image_x += 0.1
    if image_x > 100:
      image_x = 0
    print("image_x:", image_x)

    draw_texture(textureBlank01, int(image_x), 0, WHITE)

    end_drawing()

  close_window()  # Close window and OpenGL context



if __name__ == '__main__':
  main()