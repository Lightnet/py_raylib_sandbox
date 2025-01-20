# 
# https://www.raylib.com/cheatsheet/cheatsheet.html
# https://kenney.nl/assets/1-bit-pack
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

  texture_tile = load_texture("resources/colored-transparent_packed.png")  # Texture loading

  # reuse images in case of change the scene map
  image_tilemaps = []

  image_tilemap = load_image_from_texture(texture_tile)
  #GenImageColor
  #image_tilemap_layer01 = gen_image_color(128,128,GRAY)
  #image_tilemap_layer01 = gen_image_color(128,128,LIGHTGRAY)
  image_tilemap_layer01 = gen_image_color(128,128,BLACK)

  cols = TILEMAP_X
  print(texture_tile.width)
  # max tiles
  MAX_INDEX = 49*22
  for i in range(MAX_INDEX):
    # raylib api refs
    # Image ImageCopy(Image image); 
    # ImageCrop
    # ImageFlipHorizontal
    # ImageResize
    index = i
    #print("index:", index)
    col = index % cols
    row = math.floor( index / cols )
    p_x = col * float(texture_tile.width/TILEMAP_X)
    p_y = row * float(texture_tile.height/TILEMAP_Y)
    #print("p_x:", p_x, " p_y:", p_y)

    tmp = image_copy(image_tilemap)
    image_crop(tmp,[int(p_x),int(p_y),16,16])
    image_resize(tmp,16,16)
    image_tilemaps.append(tmp)

  #for tilemap test 128x128 pixel , 16x16 image
  mapData = [
    [0,200,843,0,0,0,0,0],
    [0,16,16,16,16,16,16,0],
    [0,16,0,0,0,0,16,0],
    [0,16,0,0,0,0,16,0],
    [0,16,0,0,0,0,0,0],
    [0,16,0,0,0,0,0,0],
    [0,16,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
  ]

  #image_draw(image_tilemap_layer01, image_tilemaps[1],[0,16,16],[0,0,16,16],WHITE)
  #image_draw(image_tilemap_layer01, tmp,[0,0,128,128],[0,16,16,16],WHITE)

  map_data_string = ""
  for y in range(len(mapData)):
    #print(y)
    map_data_string +="\n"
    for x in range(len(mapData[y])):
      #print(x)
      tile_id = mapData[y][x]
      tile_image = image_tilemaps[tile_id]
      #tilemap layer blank and draw ref 
      image_draw(image_tilemap_layer01, tile_image,[0,0,128,128],[x*16,y*16,16,16],WHITE)
      #image_draw(image_tilemap_layer01, tmp,[0,0,128,128],[0,16,16,16],WHITE)
      map_data_string += "" + str(mapData[y][x]) + ","
  print("map_data_string",map_data_string)

  #convert image to texture for gpu
  texture_tilemap = load_texture_from_image(image_tilemap_layer01)

  while not window_should_close():  # Detect window close button or ESC key

    begin_drawing()
    clear_background(RAYWHITE)

    #image_x += 0.1
    if image_x > 100:
      image_x = 0
    #print("image_x:", image_x)
    draw_text(f"image_x: {round(image_x,2)}",2,2,20,RED)
    # draw tilemap texture that been draw without need to loop render each images.
    # reason to reduce lag or slow frame rate loop?
    draw_texture(texture_tilemap,int(image_x),100,WHITE)
    end_drawing()

  # cleanup
  # images need to cleanup.
  for i in range(MAX_INDEX):
    #print("index:", i)
    unload_image(image_tilemaps[i])
    #pass

  close_window()  # Close window and OpenGL context
  
# main entery point
if __name__ == '__main__':
  main()