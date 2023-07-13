from random import randint
from ursina import Entity, time, destroy
from spaceship import Spaceship
from wallpart import Wallpart

class Wall(Entity):
  instances = []
  def __init__(self, add_to_scene_entities=True, num_holes = 5,**kwargs):
    self.score = kwargs["score_func"]
    grid = [[1 for _ in range(7)] for _ in range(4)]
    for _ in  range(num_holes):
      grid[randint(0,3)][randint(0,6)] = 0
    kwargs = {"z":27,**kwargs}
    super().__init__(add_to_scene_entities, **kwargs)
    for y, row in enumerate(grid):
      for x, box in enumerate(row):
        if box:
          part = Wallpart(parent = self, origin_x = x-3, origin_y = y-1.5 )
    Wall.instances.append(self)

  def update(self):
    if not Spaceship.instance.dead:
      self.z -= 10 * time.dt
      if self.z < -5:
        self.score()
        destroy(self)
  @classmethod
  def destroy_all(cls):
    for i in cls.instances:
      destroy(i)