from Position import Position


class ObjectRenderer(object):
    def __init__(self, x, y, surface, horizontal=True):
        self.x = x
        self.y = y
        self.horizontal = horizontal
        self.surface = surface

    def render(self, obj, x_margin, y_margin):
        if not self.horizontal:
            x = self.x + x_margin
        else:
            self.x += x_margin
            x = self.x
        y = self.y + y_margin

        obj.pos = Position(x, y)
        obj.draw(self.surface)

        if self.horizontal:
            self.x += obj.width
        else:
            self.y += obj.height

        return Position(x, y)

    # def render_text(self, text: Text, x_margin, y_margin, antialias):
    #     return self.render(text.get_font(antialias), x_margin, y_margin)
