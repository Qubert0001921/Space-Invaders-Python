import math
import pygame


class Animationable(object):
    def __init__(self,
                 animation_speed,
                 frame_idle,
                 frame_idle_size=(0, 0),
                 animate=False,
                 show=True,
                 current_frame=0,
                 current_animation=0,
                 **kwargs
                 ):
        super().__init__(**kwargs)
        self.animate = animate
        self.show = show

        self.animations = []
        self.current_animation = current_animation

        self.current_frame_index = current_frame
        self.animation_speed = animation_speed

        self.frame_idle = frame_idle
        if not Animationable.check_if_size_is_default(frame_idle_size):
            self.frame_idle = pygame.transform.scale(self.frame_idle, frame_idle_size)

    def on_animation_end(self):
        self.current_frame_index = 0

    def on_frame_change(self, new_frame):
        return

    @staticmethod
    def check_if_size_is_default(size):
        return size[0] == 0 and size[1] == 0

    def get_current_frame(self):
        return self.animations[self.current_animation][math.floor(self.current_frame_index)]

    def load_animation(self, frames, size=(0, 0)):
        if not Animationable.check_if_size_is_default(size):
            frames = [pygame.transform.scale(x, size) for x in frames]
        self.animations.append(frames)

    def animation(self):
        result = None

        if self.show:
            if self.animate:
                result = self.get_current_frame()

                self.current_frame_index += self.animation_speed
                self.on_frame_change(self.current_frame_index)

                if self.current_frame_index > len(self.animations[self.current_animation]) - 1:
                    self.on_animation_end()
            else:
                result = self.frame_idle

        return result
