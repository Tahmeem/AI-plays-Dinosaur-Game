import pygame
dinoColor = 0, 0, 0
dinoHeight = 40
dinoWidth = 20
class Dinosaur:
    def __init__(self):
        self.x = 60,
        self.y = 0,
        self.yVelocity = 0,
        self.height = dinoHeight,
        self.width = dinoWidth,

    def jump(self):
        if self.y == 0:
            self.yVelocity = 300
    def update(self,timeChange):
        self.yVelocity += -500 * timeChange
        self.y = self.yVelocity * timeChange
        if self.y < 0:
            self.y = 0
            self.yVelocity = 0
