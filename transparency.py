import io
from PIL import Image
import pyglet
from PIL.PngImagePlugin import PngImageFile


def replace_content_with_transparency(img: PngImageFile, x, y, width, height):
    pixels = img.load()
    for i in range(x, width):
        for j in range(y, height):
            pixels[i, j] = (0, 0, 0, 0)


desert_png = Image.open('assets/desert.png')
replace_content_with_transparency(desert_png, 32, 32, 123, 123)

fake_file = io.BytesIO()
desert_png.save(fake_file, format='PNG')

desert_img = pyglet.image.load('img.png', file=fake_file)
desert = pyglet.sprite.Sprite(desert_img, x=50, y=50)

winter_img = pyglet.image.load('assets/winter.jpg')
winter = pyglet.sprite.Sprite(winter_img, x=0, y=0)

window = pyglet.window.Window()


@window.event
def on_draw():
    winter.draw()
    desert.draw()

pyglet.app.run()
