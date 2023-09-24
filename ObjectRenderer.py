from Position import Position
from Text import Text


class ObjectRenderer(object):
    def __init__(self, x, y, surface, horizontal=True):
        self.x = x
        self.y = y
        self.horizontal = horizontal
        self.surface = surface

    # def render_object(self, obj, x_margin, y_margin):
    #     if not self.horizontal:
    #         x = self.x + x_margin
    #     else:
    #         self.x += x_margin
    #         x = self.x
    #     y = self.y + y_margin
    #
    #     obj.draw(self.surface, (x, y))
    #     if self.horizontal:
    #         self.x += obj.width
    #     else:
    #         self.y += obj.height
    #
    #     return Position(x, y)

    def render(self, text, x_margin, y_margin):
        if not self.horizontal:
            x = self.x + x_margin
        else:
            self.x += x_margin
            x = self.x
        y = self.y + y_margin

        self.surface.blit(text, (x, y))
        if self.horizontal:
            self.x += text.get_width()
        else:
            self.y += text.get_height()

        return Position(x, y)

    def render_text(self, text: Text, x_margin, y_margin, antialias):
        return self.render(text.get_font(antialias), x_margin, y_margin)
