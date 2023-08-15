from PIL import Image, ImageFilter


def f():
    im = Image.open('vulkanturizmkamchatka.jpg')
    print(im.format, im.size, im.mode)
    im.thumbnail((100, 100))
    im.save('thumbnail.jpg')
    im.show()


if __name__ == '__main__':
    f()