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

  #need to set in case of animation snyc
  set_target_fps(60)                 # Set our game to run at 60 frames-per-second
  #texture = load_texture("resources/scarfy.png")  # Texture loading
  texture = load_texture("resources/colored-transparent_packed.png")  # Texture loading

  position = Vector2(20.0, 20.0)
  frameRec = Rectangle(0.0, 0.0, texture.width/TILEMAP_X, texture.height/TILEMAP_Y)

  """
    textureTileMapIdx(index){
      const cols = this.cols;
      const rows = this.rows;
      const col = index % cols;
      const row = Math.floor( index / cols );

      this.mapTexture.offset.x = col / cols;
      this.mapTexture.offset.y = 1 - ( ( 1 + row ) / rows );
    }
  """
  index = 0
  cols = TILEMAP_X
  rows = TILEMAP_Y

  while not window_should_close():  # Detect window close button or ESC key

    framesCounter += 1

    if framesCounter >= 60/framesSpeed:
      framesCounter = 0
      currentFrame += 1
      #index += 1
      if currentFrame > 5: 
        currentFrame = 0
      if index > 1000:
        index = 0
      # 
      #frameRec.x = float(currentFrame) * float(texture.width/TILEMAP_X)
    # Control index tile map for image
    if (is_key_pressed(KeyboardKey.KEY_RIGHT)):
      index += 1
    elif is_key_pressed(KeyboardKey.KEY_LEFT):
      index -= 1

    if (is_key_pressed(KeyboardKey.KEY_UP)):
      index -= 49
      if index < 0:
        index = 0
    if (is_key_pressed(KeyboardKey.KEY_DOWN)):
      index += 49

    if framesSpeed > MAX_FRAME_SPEED:
      framesSpeed = MAX_FRAME_SPEED
    elif framesSpeed < MIN_FRAME_SPEED:
      framesSpeed = MIN_FRAME_SPEED

    col = index % cols # index divide by columns and no remainder .by block image width tile for x
    row = math.floor( index / cols ) # index divide by columns for y or height for rows

    frameRec.x = col * float(texture.width/TILEMAP_X) # index col, width tile / number tiles cols
    frameRec.y = row * float(texture.height/TILEMAP_Y) # index row, height tile / number tiles rows

    begin_drawing()

    clear_background(RAYWHITE)
    #sprite
    draw_rectangle_lines(20, 20, int(frameRec.width), int(frameRec.height), RED)
    draw_texture_rec(texture, frameRec, position, WHITE)

    draw_rectangle_lines(20 + int(frameRec.x), 40 + int(frameRec.y), int(frameRec.width), int(frameRec.height), RED)
    
    draw_texture(texture, 20, 40, WHITE)

    draw_text(f"Index: {index}", 2, 0, 10, DARKGRAY)
    draw_text(f"Cols: {col}", 100, 0, 10, DARKGRAY)
    draw_text(f"Rows: {row}", 180, 0, 10, DARKGRAY)

    end_drawing()

  # De-Initialization
  unload_texture(texture)
  
  close_window()  # Close window and OpenGL context

if __name__ == '__main__':
  main()