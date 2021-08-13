import pygame, random
from dinosaur import Dinosaur
import tkinter.messagebox
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
highScore = 0

root = tkinter.Tk()
root.withdraw()
def main(highScore):
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
                if score > highScore:
                    highScore = score
                main(highScore)

        score = pointFunc(score, gameSpeed)[0]
        font = pygame.font.SysFont(None, 24)
        scoreReader = font.render(f"Score: {score}", True, (0, 0, 0))
        scoreRect = scoreReader.get_rect()
        scoreRect.center = (550, 40)
        display.blit(scoreReader, scoreRect)
        highScoreReader = font.render(f"High: {highScore}", True, (0, 0, 0))
        highScoreRect = highScoreReader.get_rect()
        highScoreRect.center = (460, 40)
        display.blit(highScoreReader, highScoreRect)

        pygame.draw.rect(display, black, [0, groundHeight, width, 20])

        clock.tick(30)
        pygame.display.update()
if __name__ == '__main__':
    main(highScore)