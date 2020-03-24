# Constants used by each solution
from math import sin, cos, pi, sqrt
from PIL import Image, ImageDraw
import noise
THETA = pi / 3.0 # Angle from one point to the next
HEXES_HIGH = 60 # How many rows of hexes
HEXES_WIDE = 16 # How many hexes in a row
RADIUS = 30 # Size of a hex
HALF_RADIUS = RADIUS / 2.0
HALF_HEX_HEIGHT = sqrt(RADIUS ** 2 - HALF_RADIUS ** 2)
IMAGE_WIDTH = int(RADIUS * (HEXES_WIDE * 3 + .5))
IMAGE_HEIGHT = int(HALF_HEX_HEIGHT * (HEXES_HIGH + 1))

HEXES_HIGH_BIG = 10 # How many rows of hexes
HEXES_WIDE_BIG = 7 # How many hexes in a row
RADIUS_BIG = 150 # Size of a hex
HALF_RADIUS_BIG = RADIUS_BIG / 2.0
HALF_HEX_HEIGHT_BIG = sqrt(RADIUS_BIG ** 2 - HALF_RADIUS_BIG ** 2)

scale = 10.0
octaves = 2
persistence = 12.0
lacunarity = 2.0

colors = {"water": (128,192,255), "plains": (128,255,128), "forest": (0,55,0), "hills":(128, 128, 64),
          "mountains": (200, 200, 200), "swamp": (128,128,92)}


# Functions (generators) used by each solution
def hex_points(x,y, radius):
    '''Given x and y of the origin, return the six points around the origin of RADIUS distance'''
    for i in range(6):
        yield cos(THETA * i) * radius + x, sin(THETA * i) * radius + y
def hex_centres(hexesWide, hexesHigh, radius, halfHexHeight):
    for x in range(hexesWide):
        for y in range(hexesHigh):
            yield ((x * 3 + 1) * radius + radius * 1.5 * (y % 2), (y + 1) * halfHexHeight), (x,y)


def colorsFunc(perlinNumber):
    global colors
    if perlinNumber < -0.2:
        return colors["water"]
    elif -0.2 <= perlinNumber < 0.1:
        return colors["plains"]
    elif 0.1 <= perlinNumber < 0.35:
        return colors["hills"]
    elif 0.35 <= perlinNumber <= 1.0:
        return colors["mountains"]
#pil_colours = pygame_colours  # same format works, so we'll re-use it
def pil_hex():
    #image = Image.new("RGBA", (IMAGE_WIDTH,IMAGE_HEIGHT), (0,0,0,0))
    image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), (0, 0, 0))
    #colours = pil_colours()
    draw = ImageDraw.Draw(image, "RGBA")
    for coords, num in hex_centres(HEXES_WIDE, HEXES_HIGH, RADIUS, HALF_HEX_HEIGHT):
        color = noise.pnoise2(num[0]/scale, num[1]/scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity, repeatx=IMAGE_WIDTH, repeaty=IMAGE_HEIGHT)
        draw.polygon(list(hex_points(coords[0],coords[1], RADIUS)), fill=colorsFunc(color))
    #image.save('pil_hexes.png', 'PNG')
    return image
def pil_big_hex(image):
    draw = ImageDraw.Draw(image, "RGBA")
    for coords, num in hex_centres(HEXES_WIDE_BIG, HEXES_HIGH_BIG, RADIUS_BIG, HALF_HEX_HEIGHT_BIG):
        x = coords[0]+15
        y = coords[1]+25
        draw.polygon(list(hex_points(x,y, RADIUS_BIG)), fill=(0,0,0,0), outline=(255,0,0, 255))
    #image.save('pil_hexes.png', 'PNG')
    return image

img = pil_big_hex(pil_hex())
img.save('pil_hexes.png', 'PNG')
