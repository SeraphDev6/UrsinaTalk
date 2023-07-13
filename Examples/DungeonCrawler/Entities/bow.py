from typing import List
from ursina import Entity, destroy, time, Vec3, scene, mouse
from Entities.arrow import Arrow


class Bow(Entity):
    def __init__(self, add_to_scene_entities=True, **kwargs):
        kwargs = {
            "model": "bow",
            "projectile": Arrow,
            "speed": 20,
            "damage": 5,
            "draw_speed": 1.5,
            "drawn": 0.0,
            "texture": "perlin_noise",
            "color": "#34301D",
            **kwargs,
        }
        super().__init__(add_to_scene_entities, **kwargs)
        self.proj = None

    def update(self):
        self.scale = Vec3(1, 1, 1 + 2 * self.drawn)
        if self.proj:
            self.proj.scale = Vec3(1, 1, 1 / (1 + 1 * self.drawn))
            if self.drawn < 1:
                self.drawn += time.dt / self.draw_speed
                self.proj.position = Vec3(0, 0, 0.4 - 0.4 * self.drawn)
                if self.drawn > 1:
                    self.drawn = 1

    def input(self, key):
        if self.enabled:
            if key == "left mouse down":
                if self.drawn == 0:
                    self.proj = self.projectile(parent=self, color="#ff0000")
            if self.drawn > 0 and key == "left mouse up":
                self.fire_proj()
                self.drawn = 0

    def fire_proj(self):
        if not self.proj:
            return
        rotation = self.proj.world_rotation
        self.proj.parent = scene
        self.proj.world_position = self.world_position
        self.proj.world_rotation = self.world_rotation
        self.proj.fired = True
        self.proj.speed = self.speed * self.drawn
        self.proj.damage = (self.proj.damage + self.damage) * self.drawn
        self.proj = None
