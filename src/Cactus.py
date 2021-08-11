from obstacle import Obstacle
class Cactus(Obstacle):
    def __init__(self, image):
        self.image = image
        super().__init__(image)
        self.imageRect.y = 325
