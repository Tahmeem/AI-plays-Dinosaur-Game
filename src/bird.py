from obstacle import Obstacle
class Bird(Obstacle):
    def __init__(self, image):
        self.image = image
        super().__init__(image)
        self.imageRect.y = 250