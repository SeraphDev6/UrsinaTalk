from ursina import Entity, held_keys, time, clamp, destroy

class Spaceship(Entity):
  instance = None
  def __init__(self, add_to_scene_entities=True, **kwargs):
    if Spaceship.instance:
      destroy(Spaceship.instance)
    kwargs = {"model": "spaceship", "rotation_z": 180, "scale": 0.5, "collider":"mesh", **kwargs}
    super().__init__(add_to_scene_entities, **kwargs)
    self.target_rot = [0,180]
    self.dead = False
    Spaceship.instance = self

  def lerp_torwards_target(self):
    if self.rotation_x < self.target_rot[0]:
      self.rotation_x = min(self.rotation_x + 80 * time.dt, self.target_rot[0])
    elif self.rotation_x > self.target_rot[0]:
      self.rotation_x = max(self.rotation_x - 80 * time.dt, self.target_rot[0])
    if self.rotation_z < self.target_rot[1]:
      self.rotation_z = min(self.rotation_z + 80 * time.dt, self.target_rot[1])
    elif self.rotation_z > self.target_rot[1]:
      self.rotation_z = max(self.rotation_z - 80 * time.dt, self.target_rot[1])
    self.rotation_y = (self.rotation_z - 180) / 2

  def clamp_position(self):
    self.x = clamp(self.x,-6.75,6.75)
    self.y = clamp(self.y,-4,4)

  def update(self):
    if not self.dead:
      if held_keys["w"]:
        self.y += 5 * time.dt
        self.target_rot[0] = -20
      elif held_keys["s"]:
        self.y -= 5 * time.dt
        self.target_rot[0] = 20
      else:
        self.target_rot[0] = 0
      if held_keys["d"]:
        self.x += 5 * time.dt
        self.target_rot[1] = 200
      elif held_keys["a"]:
        self.x -= 5 * time.dt
        self.target_rot[1] = 160
      else:
        self.target_rot[1] = 180
      self.lerp_torwards_target()
      self.clamp_position()

