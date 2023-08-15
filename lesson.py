from PIL import Image, ImageFilter


def f():
    im = Image.open('vulkanturizmkamchatka.jpg')
    print(im.format, im.size, im.mode)

    outfile = 'thumbnail.png'
    im.thumbnail((100, 100))
    im.save(outfile, format='PNG')


if __name__ == '__main__':
    f()