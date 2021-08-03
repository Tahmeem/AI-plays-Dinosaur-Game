import pygame
dinocolour = 0,0,0
DINOHEIGHT = 40
DINOWIDTH = 20

#Images
dinosaurImage = pygame.image.load('./Assets/Dino/DinoRun1.png')
jumpImg = pygame.image.load('./Assets/Dino/DinoJump.png')
duckImg = pygame.image.load('./Assets/Dino/DinoDuck1.png')
class Dinosaur:
  def __init__(self, surfaceHeight):
    self.x = 60
    self.y = 0

    self.duckImg = duckImg
    self.jumping = jumpImg

    self.duck = False
    self.jumpBool = False
    self.run = True
    self.Img = dinosaurImage


    self.yvelocity = 0
    self.height = DINOHEIGHT
    self.width = DINOWIDTH
    self.surfaceHeight = surfaceHeight
  def jump(self):
    if(self.y == 0):
      self.yvelocity = 300
  def update(self, userInput):
    if self.jumpBool:
      self.jump()
    if self.duck:
      self.duck()
    if self.run:
      self.run()
    if userInput[pygame.K_SPACE] and not self.jumpBool:
      self.duck = False
      self.jumpBool = True
      self.run = False
    elif userInput[pygame.K_DOWN] and not self.jumpBool:
      self.duck = True
      self.jumpBool = False
      self.run = False
    elif not (self.jumpBool or userInput[pygame.K_DOWN]):
      self.duck = False
      self.jumpBool = False
      self.run = True

  def draw(self,display):
    pygame.draw.rect(display,dinocolour,[self.x,self.surfaceHeight-self.y-self.height,self.width,self.height])