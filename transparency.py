import pyglet


desert_img = pyglet.image.load('assets/desert.jpg')
desert = pyglet.sprite.Sprite(desert_img, x=50, y=50)

winter_img = pyglet.image.load('assets/winter.jpg')
winter = pyglet.sprite.Sprite(winter_img, x=0, y=0)

window = pyglet.window.Window()


@window.event
def on_draw():
    winter.draw()
    desert.draw()

pyglet.app.run()
