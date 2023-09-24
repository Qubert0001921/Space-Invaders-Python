from Hittable import Hittable


class Renderable(Hittable):
    def __init__(self, width, height, pos):
        super().__init__()
        self.width = width
        self.height = height
        self.pos = pos

    def draw(self, surface):
        pass
