import ursina as ur
import random

ur.app = ur.Ursina()
class Plinko(ur.Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = 'quad'
        self.color = ur.color.orange
        self.scale = (0.1, 0.1)
        self.collider = 'box'
        self.velocity = ur.Vec3(0, -0.1, 0)

    def update(self):
        self.position += self.velocity
        if self.y < -5:
            self.disable()

def create_board():
    for x in range(-5, 6):
        for y in range(-5, 6):
            if (x + y) % 2 == 0:
                ur.Entity(model='sphere', color=ur.color.azure, scale=0.1, position=(x * 0.5, y * 0.5, 0))

def drop_ball():
    ball = Plinko(position=(random.uniform(-2, 2), 5, 0))

ur.window.color = ur.color.black
create_board()
ur.Button(text='Drop Ball', color=ur.color.green, position=(0.7, 0.45), scale=(0.2, 0.1), on_click=drop_ball)

ur.app.run()