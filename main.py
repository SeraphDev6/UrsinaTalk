from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from Entities import Player

app = Ursina()


# testing = application.development_mode
# window.title = "FPS Demo"
# window.borderless = not testing
# window.fullscreen = not testing
# window.exit_button.visible = not testing
# window.fps_counter.enabled = testing

# Entity.default_shader = lit_with_shadows_shader

aliases = {
    "up arrow": "w",
    "left arrow": "a",
    "down arrow": "s",
    "right arrow": "d",
}


for a in aliases:
    input_handler.bind(a, aliases[a])

ground = Entity(model="plane", collider="box", scale=64)
player = Player()
sky = Sky(color="87CEEB")

app.run()
