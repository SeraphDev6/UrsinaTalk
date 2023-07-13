from ursina import *

app = Ursina()

testing = application.development_mode
window.title = "Terrain Generation"
window.borderless = not testing
window.fullscreen = not testing
window.exit_button.visible = not testing
window.fps_counter.enabled = testing

aliases = {
    "up arrow": "w",
    "left arrow": "a",
    "down arrow": "s",
    "right arrow": "d",
}

for a in aliases:
    input_handler.bind(a, aliases[a])

"""Terrain using an RGB texture as input"""
terrain_from_heightmap_texture = Entity(
    model=Terrain("heightmap_1", skip=8), scale=(40, 5, 20), texture="heightmap_1"
)

"""
I'm just getting the height values from the previous terrain as an example, but you can provide your own.
It should be a list of lists, where each value is between 0 and 255.
"""
hv = terrain_from_heightmap_texture.model.height_values.tolist()
terrain_from_list = Entity(
    model=Terrain(height_values=hv), scale=(40, 5, 20), texture="heightmap_1", x=40
)


def input(key):
    if key == "space":  # randomize the terrain
        terrain_from_list.model.height_values = [
            [random.uniform(0, 255) for a in column]
            for column in terrain_from_list.model.height_values
        ]
        terrain_from_list.model.generate()


EditorCamera()
Sky()

player = Entity(model="sphere", color=color.azure, scale=0.2, origin_y=-0.5)
hv = terrain_from_list.model.height_values


def update():
    direction = Vec3(
        held_keys["d"] - held_keys["a"], 0, held_keys["w"] - held_keys["s"]
    ).normalized()
    player.position += direction * time.dt * 8
    player.y = terraincast(player.world_position, terrain_from_list, hv)


if __name__ == "__main__":
    app.run()
