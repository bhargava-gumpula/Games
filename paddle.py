# Paddle class handles paddle movement and bouncing the ball
class Paddle:
   def __init__(self, canvas, speed = 70):
      self.speed = speed
      self.x1 = 400
      self.y1 = 700
      self.x2 = 550
      self.y2 = 730
      self.canvas = canvas
      
   def movepaddle(self,event):
         if event.keysym == 'Left':
           if (self.x1 >= self.speed):
              self.x1 =  self.x1 - self.speed
              self.x2 = self.x2 - self.speed
              self.canvas.move(self.paddle ,-self.speed,0)
         if event.keysym == 'Right':
           if (self.x2 <= 950 - self.speed):
              self.x2 =  self.x2 + self.speed
              self.x1 = self.x1 + self.speed
              self.canvas.move(self.paddle ,self.speed,0)
         if event.keysym == 'Down':
            sys.exit()
   def draw(self):
      self.paddle = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill='blue')
      
      self.canvas.itemconfig(self.paddle, outline = 'black')
