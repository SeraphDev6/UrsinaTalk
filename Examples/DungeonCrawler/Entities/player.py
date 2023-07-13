from ursina import camera, scene, mouse
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar
from Entities import Bow


class Player(FirstPersonController):
    def __init__(self, **kwargs):
        self.max_health = 100
        self.health = self.max_health
        self.bow_available = False
        self.health_bar = HealthBar(max_value=self.max_health)
        self.health_bar.value = self.health
        super().__init__(**kwargs)
        self.bow = Bow(parent=camera, position=(0.75, 0, 1.25))
        self.bow.enabled = self.bow_available
        self.gravity = scene.gravity

    def update(self):
        super().update()
        self.health_bar.value = self.health

    def input(self, key):
        super().input(key)
        if key == "escape":
            mouse.locked = False
            self.cursor.enabled = False
        if not mouse.locked and key == "left mouse down":
            mouse._locked = True
            self.cursor.enabled = True
