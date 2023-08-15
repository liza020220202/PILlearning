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


if __name__ == '__main__':
    im = Image.open('vulkanturizmkamchatka.jpg')
    x = int(input())
    rotating(x)
