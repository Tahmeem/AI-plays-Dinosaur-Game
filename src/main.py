import pygame
pygame.init()

size = width, height = 840, 680
display = pygame.display.set_mode(size)
cactusImage = pygame.image.load('../Assets/Cactus.png')
groundHeight = height - 400
xPos = 0
yPos = 0

#Colors
grey = 169, 169, 169
black = 0, 0, 0
white = 255, 255, 255

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    #display.blit(cactusImage, (50, 50))
    display.fill(grey)
    pygame.draw.rect(display, black, [0, 400, width, 20])
    xPos += 1
    yPos += 1
    pygame.display.update()