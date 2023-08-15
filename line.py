from PIL import Image, ImageDraw
im = Image.new('RGB', (100, 200), (0, 0, 0))
draw = ImageDraw.Draw(im)
draw.line((0, 0, 100, 200), fill=(255, 0, 0), width=1)
im.save('image.png')
