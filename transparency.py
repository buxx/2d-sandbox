import pyglet

window = pyglet.window.Window()
desert = pyglet.resource.image('assets/desert.jpg')
winter = pyglet.resource.image('assets/winter.jpg')


@window.event
def on_draw():
    window.clear()
    desert.blit(0, 0)
    winter.blit(64, 64)

pyglet.app.run()
