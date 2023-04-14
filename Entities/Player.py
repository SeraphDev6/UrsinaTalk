from ursina.prefabs.first_person_controller import FirstPersonController


class Player(FirstPersonController):
    def __init__(self, **kwargs):
        kwargs = {"paused": False, **kwargs}
        super().__init__(**kwargs)

    def update(self):
        if not self.paused:
            super().update()

    def input(self, key):
        super().input(key)
