from pyray import *


class App:

  def __init__(self):
    self.currentFrame = 0
    self.framesCounter = 0
    self.framesSpeed = 15
    #pass

  def run(self):
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
    source_rec = Rectangle(0, 0, frame_width, frame_height)

    # Destination rectangle (screen rectangle where drawing part of texture)
    dest_rec = Rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, frame_width*2, frame_height*2)

    frameRec = Rectangle(0.0, 0.0, scarfy.width/6, scarfy.height)

    # Origin of the texture (rotation/scale point), it's relative to destination rectangle size
    origin = Vector2(frame_width, frame_height)

    position = Vector2(350.0, 280.0)

    #currentFrame = 0
    #self.framesCounter = 0
    #framesSpeed = 8

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key

      self.framesCounter += 1
      #print("framesCounter: ", self.framesCounter, " currentFrame: ", self.currentFrame)
      #print("currentFrame: ", self.currentFrame)
      #if self.framesCounter >= (60/self.framesSpeed):
      print("F:", 60/10000)
      if self.framesCounter >= 60/self.framesSpeed:
        self.framesCounter = 0
        self.currentFrame += 1
        if self.currentFrame > 5: 
          self.currentFrame = 0
         
        frameRec.x = float(self.currentFrame) * float(scarfy.width/6)
      # Control speed animation
      if (is_key_pressed(KeyboardKey.KEY_RIGHT)):
        self.framesSpeed += 1
      elif is_key_pressed(KeyboardKey.KEY_LEFT):
        self.framesSpeed -= 1
      print("framesSpeed: ", self.framesSpeed, " :", (60*self.framesSpeed))
      # if framesSpeed > MAX_FRAME_SPEED:
      #   framesSpeed = MAX_FRAME_SPEED
      # elif framesSpeed < MIN_FRAME_SPEED:
      #   framesSpeed = MIN_FRAME_SPEED
      
      #print("framesSpeed: ",framesSpeed)
      begin_drawing()

      clear_background(RAYWHITE)

      #DrawRectangleLines(15, 40, scarfy.width, scarfy.height, LIME);
      draw_rectangle_lines(15, 40, scarfy.width, scarfy.height, LIME)
      #draw_rectangle_lines(15 , 40, scarfy.width, scarfy.height, RED)

      draw_texture(scarfy, int(SCREEN_WIDTH/2 - scarfy.width/2), int(SCREEN_HEIGHT/2 - scarfy.height/2), WHITE)

      draw_texture_rec(scarfy, frameRec,position,WHITE)


      draw_text("this IS a texture loaded from an image!", 300, 370, 10, GRAY)

      end_drawing()

    # De-Initialization
    close_window()  # Close window and OpenGL context

if __name__ == '__main__':
  #main()
  app = App()
  app.run()