from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

FIELD_DIMENSIONS = (100,1,100)

class WalkingApp(Ursina):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        window.fullscreen = True
        Entity(model = "plane", texture="grass", collider="mesh", scale=FIELD_DIMENSIONS)
        FirstPersonController()
        self.add_sample()

    def add_sample(self) -> None:
        Entity(model="assets/bench.obj", collider="mesh", collision=True, texture="vignette", scale=.02)


class Conroller:
    def __init__(self) -> None:
        pass


app = WalkingApp()
app.run()
