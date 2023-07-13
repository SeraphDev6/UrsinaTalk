from ursina import application, window, input_handler

testing = application.development_mode
window.title = "Space Avoider"
window.borderless = not testing
window.fullscreen = not testing
window.fps_counter.enabled = testing

aliases = {
    "up arrow": "w",
    "left arrow": "a",
    "down arrow": "s",
    "right arrow": "d",
}

for a in aliases:
    input_handler.bind(a, aliases[a])
