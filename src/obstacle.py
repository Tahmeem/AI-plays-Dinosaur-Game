
screenWidth = 640
class Obstacle:
    def __init__(self, image,):
        self.image = image
        self.imageRect = self.image.get_rect()
        self.imageRect.x = screenWidth

    def update(self,obstacles):
        if self.imageRect.x < -screenWidth:
            obstacles.pop()
    def draw(self,display):
        display.blit(self.image, self.imageRect)