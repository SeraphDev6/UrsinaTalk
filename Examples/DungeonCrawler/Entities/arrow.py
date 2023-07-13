from typing import List
from ursina import Entity, destroy, time, Vec3, scene


class Arrow(Entity):
    instances: List[Entity] = []
    max_arrows: int = 10

    def __init__(self, add_to_scene_entities=True, **kwargs):
        while len(Arrow.instances) >= Arrow.max_arrows:
            destroy(Arrow.instances.pop(0))
        kwargs = {
            "model": "arrow",
            "collider": "box",
            "speed": 10,
            "damage": 5,
            "fired": False,
            **kwargs,
        }
        super().__init__(add_to_scene_entities, **kwargs)
        self.momentum = 0.0
        Arrow.instances.append(self)

    def update(self):
        if self.fired:
            if self.momentum == 0:
                self.momentum = self.forward * self.speed
            if self.intersects(scene):
                self.fired = False
                self.collision = False
                if getattr(self.parent, "health", False):
                    self.parent.health -= self.damage
                    destroy(self)
            self.position += self.speed * time.dt * self.momentum
            self.momentum += Vec3(0, -scene.gravity, 0) * time.dt
            self.look_at(self.position + self.momentum)
