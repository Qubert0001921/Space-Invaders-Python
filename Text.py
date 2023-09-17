from Hittable import Hittable


class Text(Hittable):
    def __init__(self, font, content, color):
        super().__init__()
        self.font = font
        self.color = color
        self.content = content

    def get_font(self, antialias):
        return self.font.render(self.content, antialias, self.color)

