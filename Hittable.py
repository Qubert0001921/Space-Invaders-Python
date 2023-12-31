from CollideBox import CollideBox


class Hittable(object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.collide_boxes = []
        self.hittable = True

    def add_collide_box(self, collide_box: CollideBox):
        self.collide_boxes.append(collide_box)

    def check_collision(self, hittable):
        for collide_box in self.collide_boxes:
            if collide_box.check_if_collide(hittable.collide_boxes):
                return True
