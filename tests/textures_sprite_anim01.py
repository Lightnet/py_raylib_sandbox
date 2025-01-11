from pyray import *

# currentFrame = 0
# framesCounter = 0
# framesSpeed = 8
def main():
    # global currentFrame
    # global framesCounter
    # global framesSpeed
    currentFrame = 0
    framesCounter = 0
    framesSpeed = 8
    # Initialization
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 450

    MAX_FRAME_SPEED = 15
    MIN_FRAME_SPEED = 1

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "raylib [texture] example - sprite anim")

    #need to set in case of animation snyc
    set_target_fps(60)                 # Set our game to run at 60 frames-per-second

    scarfy = load_texture("resources/scarfy.png")  # Texture loading

    frame_width = scarfy.width / 6
    frame_height = scarfy.height

    # Source rectangle (part of the texture to use for drawing)
    #source_rec = Rectangle(0, 0, frame_width, frame_height)

    # Destination rectangle (screen rectangle where drawing part of texture)
    #dest_rec = Rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, frame_width*2, frame_height*2)

    frameRec = Rectangle(0.0, 0.0, scarfy.width/6, scarfy.height)

    # Origin of the texture (rotation/scale point), it's relative to destination rectangle size
    #origin = Vector2(frame_width, frame_height)

    position = Vector2(350.0, 280.0)

    #currentFrame = 0
    #self.framesCounter = 0
    #framesSpeed = 8

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key

      framesCounter += 1
      #print("framesCounter: ", self.framesCounter, " currentFrame: ", self.currentFrame)
      #print("currentFrame: ", self.currentFrame)
      #if self.framesCounter >= (60/self.framesSpeed):
      #print("F:", 60/10000)
      if framesCounter >= 60/framesSpeed:
        framesCounter = 0
        currentFrame += 1
        if currentFrame > 5: 
          currentFrame = 0
         
        frameRec.x = float(currentFrame) * float(scarfy.width/6)
      # Control speed animation
      if (is_key_pressed(KeyboardKey.KEY_RIGHT)):
        framesSpeed += 1
      elif is_key_pressed(KeyboardKey.KEY_LEFT):
        framesSpeed -= 1
      #print("framesSpeed: ", framesSpeed, " :", (60*framesSpeed))
      if framesSpeed > MAX_FRAME_SPEED:
        framesSpeed = MAX_FRAME_SPEED
      elif framesSpeed < MIN_FRAME_SPEED:
        framesSpeed = MIN_FRAME_SPEED
      
      #print("framesSpeed: ",framesSpeed)
      begin_drawing()

      clear_background(RAYWHITE)

      #DrawRectangleLines(15, 40, scarfy.width, scarfy.height, LIME);
      #draw_rectangle_lines(15 , 40, scarfy.width, scarfy.height, RED)
      draw_rectangle_lines(15, 40, scarfy.width, scarfy.height, LIME)
      draw_rectangle_lines(15 + int(frameRec.x), 40 + int(frameRec.y), int(frameRec.width), int(frameRec.height), RED)
      draw_text("FRAME SPEED: ", 165, 210, 10, DARKGRAY)
      draw_text(f" FPS {framesSpeed}", 575, 210, 10, DARKGRAY) #format string
      draw_text("PRESS RIGHT/LEFT KEYS to CHANGE SPEED!", 290, 240, 10, DARKGRAY)

      for i in range(MAX_FRAME_SPEED):
        if i < framesSpeed:
          draw_rectangle(250 + 21*i, 205, 20, 20, RED)
        draw_rectangle_lines(250 + 21*i, 205, 20, 20, MAROON)


      draw_texture(scarfy, 15, 40, WHITE)
      #draw_texture(scarfy, int(SCREEN_WIDTH/2 - scarfy.width/2), int(SCREEN_HEIGHT/2 - scarfy.height/2), WHITE)

      draw_texture_rec(scarfy, frameRec, position,WHITE)


      draw_text("(c) Scarfy sprite by Eiden Marsal", SCREEN_WIDTH - 200, SCREEN_HEIGHT - 20, 10, GRAY)
      #draw_text("this IS a texture loaded from an image!", 300, 370, 10, GRAY)

      end_drawing()

    # De-Initialization
    unload_texture(scarfy)

    close_window()  # Close window and OpenGL context

if __name__ == '__main__':
    main()