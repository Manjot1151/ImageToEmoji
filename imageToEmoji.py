from PIL import Image
import requests
from io import BytesIO
import math


def distance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2


colors = {
    (0, 0, 0): '⬛',
    (255, 255, 255): '⬜',
    (255, 0, 0): '🟥',
    (255, 127, 0): '🟧',
    (255, 255, 0): '🟨',
    (0, 255, 0): '🟩',
    (0, 0, 255): '🟦',
    (75, 0, 130): '🟪',
    (139, 69, 19): '🟫'
}


def findNearestEmoji(pixel):
    minDist = 1000000
    nearestEmoji = ''
    for color in colors:
        dist = distance(pixel, color)
        if dist < minDist:
            minDist = dist
            nearestEmoji = colors[color]
    return nearestEmoji


url = input('Enter image url: ')
response = requests.get(url)
img = Image.open(BytesIO(response.content))
pixels = int(input('Enter number of pixels: '))
downscale_factor = int(math.sqrt(img.height * img.width / pixels))
if downscale_factor == 0:
    downscale_factor = 1
img = img.resize((img.width // downscale_factor, img.height //
                 downscale_factor), Image.NEAREST)
for i in range(img.height):
    for j in range(img.width):
        print(findNearestEmoji(img.getpixel((j, i))), end='')
    print()
