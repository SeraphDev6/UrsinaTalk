from ursina import Entity, time
from spaceship import Spaceship

class Wallpart(Entity):
  def __init__(self, add_to_scene_entities=True, **kwargs):
    kwargs = {"model": "cube",
              "texture": "white_cube",
              "scale": 3,
              "collider":"box",
              **kwargs}
    super().__init__(add_to_scene_entities, **kwargs)

  def update(self):
    if self.intersects(Spaceship.instance):
      Spaceship.instance.dead = True
