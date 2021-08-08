import pygame
from dinosaur import Dinosaur
from points import points as pointFunc
pygame.init()

size = width, height = 640, 480
display = pygame.display.set_mode(size)

groundHeight = height - 100
dinosaur = Dinosaur(groundHeight)

#Images
cactus = pygame.image.load('./Assets/Cactus.png')
bird = pygame.image.load('./Assets/Bird1.png')


score = 0
gameSpeed = 15

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

    score = pointFunc(score, gameSpeed)[0]
    font = pygame.font.SysFont(None, 24)
    scoreReader = font.render(f"Score: {score}", True, (0, 0, 0))
    scoreRect = scoreReader.get_rect()
    scoreRect.center = (550, 40)
    display.blit(scoreReader, scoreRect)

    pygame.draw.rect(display, black, [0, groundHeight, width, 20])

    clock.tick(30)
    pygame.display.update()
