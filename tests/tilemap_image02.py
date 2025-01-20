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

  texture_tile = load_texture("resources/colored-transparent_packed.png")  # Texture loading
  # position = Vector2(20.0, 20.0)
  # frameRec = Rectangle(0.0, 0.0, texture.width/TILEMAP_X, texture.height/TILEMAP_Y)


  # imBlank = gen_image_color(64, 64, RED)
  # #textureBlank = load_texture_from_image(imBlank) #test
  # im32 = gen_image_color(32, 32, BLUE)
  # #textureBlank02 = load_texture_from_image(im32) #test

  # image_draw(imBlank,im32,[0,0,32,32],[0,32,32,32],WHITE)
  # textureBlank01 = load_texture_from_image(imBlank)

  # unload_image(imBlank)
  # unload_image(im32)

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
    # Image ImageCopy(Image image); 
    # ImageCrop
    # ImageFlipHorizontal
    # ImageResize
    index = i
    print("index:", index)
    col = index % cols
    row = math.floor( index / cols )
    p_x = col * float(texture_tile.width/TILEMAP_X)
    p_y = row * float(texture_tile.height/TILEMAP_Y)
    #print("p_x:", p_x, " p_y:", p_y)

    tmp = image_copy(image_tilemap)
    image_crop(tmp,[int(p_x),int(p_y),16,16])
    image_resize(tmp,16,16)
    image_tilemaps.append(tmp)
  #   #pass

  # # Test draw image over lay tile map
  # tmp = image_copy(image_tilemap)
  # image_crop(tmp,[16,0,16,16])
  # image_resize(tmp,16,16)
  # image_tilemaps.append(tmp)

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

  # image_draw(image_tilemap_layer01,image_tilemaps[0],[0,0,16,16],[0,0,16,16],WHITE)
  #image_draw(image_tilemap_layer01,image_tilemaps[1],[0,0,16,16],[0,0,16,16],WHITE)
  #image_draw(image_tilemap_layer01, image_tilemaps[0],[0,16,16],[0,0,16,16],WHITE)
  #image_draw(image_tilemap_layer01, tmp,[0,0,128,128],[0,16,16,16],WHITE)

  map_data_string = ""
  for y in range(len(mapData)):
    #print(y)
    map_data_string +="\n"
    for x in range(len(mapData[y])):
      #print(x)
      tile_id = mapData[y][x]
      tile_image = image_tilemaps[tile_id]
      image_draw(image_tilemap_layer01, tile_image,[0,0,128,128],[x*16,y*16,16,16],WHITE)

      #image_draw(image_tilemap_layer01, tmp,[0,0,128,128],[0,16,16,16],WHITE)
      map_data_string += "" + str(mapData[y][x]) + ","
  print("map_data_string",map_data_string)


  texture_tilemap = load_texture_from_image(image_tilemap_layer01)

  #texture_tmp = load_texture_from_image(tmp)

  while not window_should_close():  # Detect window close button or ESC key


    begin_drawing()
    clear_background(RAYWHITE)

    #draw_texture(textureBlank, 0, 0, WHITE)  # Drawing BLANK texture, all magic happens on shader
    #draw_texture(textureBlank02, 64, 0, WHITE)

    #image_x += 0.1
    if image_x > 100:
      image_x = 0
    #print("image_x:", image_x)
    draw_text(f"image_x: {round(image_x,2)}",2,2,20,RED)


    draw_texture(texture_tilemap,int(image_x),100,GRAY)
    #draw_texture(texture_tmp, 0,80,WHITE)

    #draw_texture(texture_tile, int(image_x), 0, WHITE)
    #draw_texture(textureBlank01, int(image_x), 0, WHITE)

    end_drawing()

  close_window()  # Close window and OpenGL context



if __name__ == '__main__':
  main()