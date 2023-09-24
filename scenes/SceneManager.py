import pygame


class SceneManager(object):
    def __init__(self, scenes, current_scene_index):
        self.scenes = scenes
        self.currentSceneIndex = current_scene_index

    def get_current_scene(self):
        return self.scenes[self.currentSceneIndex]

    def check_to_change_scene(self):
        if self.get_current_scene().name != self.get_current_scene().scene_to_change:
            current_scene_index = self.currentSceneIndex
            self.currentSceneIndex = self.scenes.index(list(
                filter(lambda x: x.name == self.get_current_scene().scene_to_change,
                       self.scenes))[0])
            self.scenes[current_scene_index].scene_to_change = self.scenes[current_scene_index].name
            self.scenes[self.currentSceneIndex].init()

