import pygame
dinocolour = 0,0,0
DINOHEIGHT = 40
DINOWIDTH = 20

#Images
dinosaurImage = [pygame.image.load('./Assets/Dino/DinoRun1.png'),pygame.image.load('./Assets/Dino/DinoRun2.png')]
jumpImg = pygame.image.load('./Assets/Dino/DinoJump.png')
duckImg = [pygame.image.load('./Assets/Dino/DinoDuck1.png'),pygame.image.load('./Assets/Dino/DinoDuck2.png')]
class Dinosaur:
  def __init__(self, surfaceHeight):
    self.x = 10
    self.y = 295
    self.yDuck = 325

    self.duckImg = duckImg
    self.jumping = jumpImg
    self.RunImg = dinosaurImage

    self.stepIndex = 0
    self.duck = False
    self.jumpBool = False
    self.run = True
    self.Img = dinosaurImage[0]
    self.dinoRect = self.Img.get_rect()

    self.yvelocity = 8.5
    self.height = DINOHEIGHT
    self.width = DINOWIDTH
    self.surfaceHeight = surfaceHeight

  def jump(self):
    self.Img = self.jumping

    if(self.jumpBool):
      self.dinoRect.y -= self.yvelocity * 4
      self.yvelocity -= 0.8
    if self.yvelocity < -8.5:
      self.jumpBool = False
      self.yvelocity = 8.5

  def duckFunc(self):
    self.Img = self.duckImg[self.stepIndex // 5]
    self.dinoRect = self.Img.get_rect()
    self.dinoRect.x = self.x
    self.dinoRect.y = self.yDuck
    self.stepIndex += 1

  def runFunc(self):
    self.Img = self.RunImg[self.stepIndex//5]
    self.dinoRect = self.Img.get_rect()
    self.dinoRect.x = self.x
    self.dinoRect.y = self.y
    self.stepIndex += 1

  def update(self, userInput):
    if self.jumpBool:
      self.jump()
    if self.duck:
      self.duckFunc()
    if self.run:
      self.runFunc()
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
    if self.stepIndex >= 10:
      self.stepIndex = 0

  def draw(self,display):
    display.blit(self.Img,(self.dinoRect.x,self.dinoRect.y))