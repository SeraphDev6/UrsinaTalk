from ursina import *
from Entities import Player

app = Ursina()
scene.gravity = 1

player = Player(bow_available=True)
cube = Entity(
    position=(0, -5, 0),
    **{
        "model": "cube",
        "texture": "white_cube",
        "scale": (100, 10, 100),
        "collider": "box",
    }
)
if application.development_mode:
    from ursina.scripts.noclip_mode import NoclipMode

    player.add_script(NoclipMode(speed=32))

camera.clip_plane_far = 500
Sky(texture="sky_sunset", scale=camera.clip_plane_far - 1)

app.run()
