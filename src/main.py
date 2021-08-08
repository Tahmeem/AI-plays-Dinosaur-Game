import pygame
from dinosaur import Dinosaur
pygame.init()

size = width, height = 640, 480
display = pygame.display.set_mode(size)

groundHeight = height - 100
dinosaur = Dinosaur(groundHeight)

#Images
cactus = pygame.image.load('./Assets/Cactus.png')
bird = pygame.image.load('./Assets/Bird1.png')


lastFrame = pygame.time.get_ticks()

#Colors
grey = 169, 169, 169
black = 0, 0, 0
white = 255, 255, 255

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    display.fill(white)
    userInput = pygame.key.get_pressed()
    dinosaur.draw(display)
    dinosaur.update(userInput)
    clock.tick(30)
    pygame.draw.rect(display, black, [0, groundHeight, width, 20])
    pygame.display.update()