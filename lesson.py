from PIL import Image, ImageFilter


def f():
    outfile = 'thumbnail.png'
    im.thumbnail((100, 100))
    im.save(outfile, format='PNG')


def cropping():
    box = (100, 100, 400, 400)
    reg = im.crop(box)
    reg.save('cropping.png', 'PNG')


def rotating(x):
    im3 = im.rotate(x)
    im3.save('rotating.jpg')


def grey():
    pixels = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            gre = (r + g + b) // 3
            pixels[i, j] = gre, gre, gre
    im.save('grey.png')


if __name__ == '__main__':
    im = Image.open('vulkanturizmkamchatka.jpg')
    grey()
