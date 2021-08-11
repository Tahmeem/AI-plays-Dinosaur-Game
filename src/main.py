import pygame, random
from dinosaur import Dinosaur
from obstacle import Obstacle
from Cactus import Cactus
from bird import Bird
from points import points as pointFunc
pygame.init()

size = width, height = 640, 480
display = pygame.display.set_mode(size)

groundHeight = height - 100
dinosaur = Dinosaur(groundHeight)

#Images
cactus = pygame.image.load('./Assets/Cactus.png')
bird = pygame.image.load('./Assets/Bird1.png')



#Colors
grey = 169, 169, 169
black = 0, 0, 0
white = 255, 255, 255


clock = pygame.time.Clock()
obstacles = []
def main():
    score = 0
    gameSpeed = 15
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill(white)
        userInput = pygame.key.get_pressed()

        dinosaur.draw(display)
        dinosaur.update(userInput)

        if len(obstacles) == 0:
            randomNumber = random.randint(0,1)
            if randomNumber == 0:
                obstacles.append(Cactus(cactus))
            elif randomNumber == 1:
                obstacles.append(Bird(bird))

        for obstacle in obstacles:
            obstacle.draw(display)
            obstacle.update(gameSpeed,obstacles)
            if dinosaur.dinoRect.colliderect(obstacle.imageRect):
                main()


        score = pointFunc(score, gameSpeed)[0]
        font = pygame.font.SysFont(None, 24)
        scoreReader = font.render(f"Score: {score}", True, (0, 0, 0))
        scoreRect = scoreReader.get_rect()
        scoreRect.center = (550, 40)
        display.blit(scoreReader, scoreRect)

        pygame.draw.rect(display, black, [0, groundHeight, width, 20])

        clock.tick(30)
        pygame.display.update()
if __name__ == '__main__':
    main()