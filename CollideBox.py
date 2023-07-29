class CollideBox(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def check_if_collide(self, collide_boxes):
        for collide_box in collide_boxes:
            if (((collide_box.x < self.x < collide_box.x + collide_box.width)
                    or (collide_box.x + collide_box.width > self.x + self.width > collide_box.x))
                    and ((collide_box.y < self.y < collide_box.y + collide_box.height)
                    or (self.y + self.height > collide_box.y and self.y < collide_box.y + collide_box.height))):
                return True

    def get_rect(self):
        return (self.x, self.y, self.width, self.height)