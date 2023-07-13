from ursina import *
from wall import Wall
from spaceship import Spaceship

app = Ursina()

testing = application.development_mode
window.title = "Space Avoider"
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


sky = Sky(color="000000")
ship = Spaceship()

spawn_timer = 0
score = 0
high_score = 0
Text.size = 0.1
Text.default_resolution = 1080 * Text.size
score_text = Text(text="0", x=0, y=0.48)
score_text.color = color.green
game_over_screen = None


def add_score():
    global score, score_text
    application.time_scale += 0.05
    score += 1
    score_text.text = f"{score}"


def reset():
    global score, spawn_timer, game_over_screen, score_text
    application.time_scale = 1
    score = 0
    score_text.text = f"{score}"

    spawn_timer = 0
    destroy(game_over_screen)
    Wall.destroy_all()
    ship = Spaceship()


def update():
    global spawn_timer, game_over_screen, high_score
    if not Spaceship.instance.dead:
        spawn_timer -= time.dt
        if spawn_timer < 0:
            Wall(score_func=add_score)
            spawn_timer = 3
    elif not game_over_screen:
        game_over_screen = Text(
            text="Game Over", x=-0.25, y=-0.05, current_color="FF0000"
        )
        game_over_screen.color = color.red
        invoke(reset, delay=3)


app.run()
