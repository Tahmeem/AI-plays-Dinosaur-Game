import pygame, random
from dinosaur import Dinosaur
from Cactus import Cactus
from bird import Bird
from points import points as pointFunc

pygame.init()

size = width, height = 640, 480

groundHeight = height - 100
dinosaur = Dinosaur(groundHeight)

#Images
cactus = pygame.image.load('./Assets/Cactus.png')
bird = pygame.image.load('./Assets/Bird1.png')



#Colors
grey = 169, 169, 169
black = 0, 0, 0
white = 255, 255, 255


obstacles = []


class game:
    def __init__(self,highScore):
        self.highScore = highScore
        self.reward = 0
        self.gameOver = False
        self.score = 0
        self.display = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        self.score = 0
        obstacles = []

    def collision(self,obstacle):
        if dinosaur.dinoRect.colliderect(obstacle.imageRect):
            return True
        return False

    def playing(self,action):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        self.display.fill(white)
        #userInput = pygame.key.get_pressed()

        dinosaur.draw(self.display)
        dinosaur.update(action)

        if len(obstacles) == 0:
            randomNumber = random.randint(0,1)
            if randomNumber == 0:
                obstacles.append(Cactus(cactus))
            elif randomNumber == 1:
                obstacles.append(Bird(bird))

        for obstacle in obstacles:
            obstacle.draw(self.display)
            obstacle.update(obstacles)
            if self.collision(obstacle):
                self.reward -= 10
                self.gameOver = True
                if self.score > self.highScore:
                    self.highScore = self.score
                return self.reward,self.gameOver,self.score

        score = pointFunc(self.score,self.reward)[0]
        reward = score
        font = pygame.font.SysFont(None, 24)
        scoreReader = font.render(f"Score: {score}", True, (0, 0, 0))
        scoreRect = scoreReader.get_rect()
        scoreRect.center = (550, 40)
        self.display.blit(scoreReader, scoreRect)
        highScoreReader = font.render(f"High: {self.highScore}", True, (0, 0, 0))
        highScoreRect = highScoreReader.get_rect()
        highScoreRect.center = (460, 40)
        self.display.blit(highScoreReader, highScoreRect)

        pygame.draw.rect(self.display, black, [0, groundHeight, width, 20])

        self.clock.tick(30)
        pygame.display.update()
        return self.reward, self.gameOver, self.score
