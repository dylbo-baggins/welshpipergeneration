import math
from PIL import Image, ImageDraw
import noise
class Hex:
    q = 0
    r = 0
    s = 0
    def __init__(self, q,r,s):
        if (q+r+s == 0):
            self.q = q
            self.r = r
            self.s = s
    def setCoordinatesQRS(self, q,r,s):
        if (q+r+s == 0):
            self.q = q
            self.r = r
            self.s = s
        else:
            return False

    def getCubicCoordnates(self):
        return (self.q,self.r,self.s)

    def getAxialCoordinates(self):
        return(self.q, self.r)

    def __eq__(self, other):
        return self.q == other.q and self.r == other.r and self.s == other.s

    def __add__(self, other):
        self.setCoordinatesQRS(self.q+other.q, self.r+other.r, self.s+other.s)
        return self

    def __sub__(self, other):
        self.setCoordinatesQRS(self.q - other.q, self.r - other.r, self.s - other.s)
        return self

    def __mul__(self, other):
        self.setCoordinatesQRS(self.q * other, self.r *other, self.s * other)
        return self
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Orientation:
    def __init__(self, f0, f1, f2, f3, b0, b1, b2, b3, start_angle):
        self.f0 = f0
        self.f1 = f1
        self.f2 = f2
        self.f3 = f3
        self.b0 = b0
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.start_angle = start_angle # in multiples of 60 degrees

orientation_pointy = Orientation(math.sqrt(3.0), math.sqrt(3.0) / 2.0, 0.0, 3.0 / 2.0,
                math.sqrt(3.0) / 3.0, -1.0 / 3.0, 0.0, 2.0 / 3.0,
                0.5)
orientation_flat = Orientation(3.0 / 2.0, 0.0, math.sqrt(3.0) / 2.0, math.sqrt(3.0),
                2.0 / 3.0, 0.0, -1.0 / 3.0, math.sqrt(3.0) / 3.0,
                0.0)
class Layout:
    def __init__(self, orientation, pointsize, pointorigin):
        self.orientation = orientation
        self.pointsize = pointsize
        self.pointorigin = pointorigin


# q,r,s = x,z,y
#flat top orientation
hex_directions = {"north" : Hex(0,-1,1), "northeast": Hex(1,-1,0), "southeast": Hex(1,0,-1), "south": Hex(0,1,-1),
                  "southwest": Hex(-1,1,0), "northwest": Hex(-1,0,1)}


def hex_length(hex):
    return int((abs(hex.q) + abs(hex.r) + abs(hex.s))/2)

def hex_distance(hexa,hexb):
    return hex_length(hexa-hexb)

def hex_neighbor(hex, direction):
    return hex + hex_directions[direction]

def hex_to_pixel(layout, hex):
    M = layout.orientation
    x = (M.f0*hex.q + M.f1 * hex.r) * layout.pointsize.x
    y = (M.f2 * hex.q + M.f3 * hex.r) * layout.pointsize.y
    return Point(x + layout.pointorigin.x, y + layout.pointorigin.y)

def pixel_to_hex(layout, pointp):
    M = layout.orientation
    pt = Point((pointp.x - layout.origin.x) / layout.pointsize.x, (pointp.y - layout.pointorigin.y) / layout.pointsize.y)
    q = M.b0 * pt.x + M.b1 * pt.y
    r = M.b2 * pt.x + M.b3 * pt.y
    return Hex(q,r, -q-r)

def hex_corner_offset(layout, corner):
    size = layout.pointsize
    angle = 2.0 * math.pi * (layout.orientation.start_angle + corner) / 6
    return Point(size.x * math.cos(angle), size.y * math.sin(angle))

def polygon_corners(layout, hex):
    corners = []
    center = hex_to_pixel(layout, hex)
    for i in range(6):
        offset = hex_corner_offset(layout, i)
        corners.append(Point(center.x + offset.x, center.y + offset.y))
    return corners

def testHexEquals():
    hex1 = Hex(0,0,0)
    hex2 = Hex(0,-1,1)
    if hex1 == hex2:
        print("Equal Test 1 Failed!")
    else:
        print("Equal Test 1 Passed!")
    hex3 = Hex(0,0,0)
    hex4 = Hex(0,0,0)
    if hex3 == hex4:
        print("Equal Test 2 Passed!")
    else:
        print("Equal Test 2 Failed!")
    hex5 = Hex(-1,0,1)
    hex6= Hex(-1,-1,2)
    if hex5 != hex6:
        print("Equal Test 2 Passed!")
    else:
        print("Equal Test 2 Failed!")

def testArithmetic():
    hex1 = Hex(0,0,0)
    hex2 = Hex(0,-1,1)
    hex3 = hex1 + hex2
    if hex3 == hex2:
        print("Addition Test Passed!")
    else:
        print("Addition Test Failed!")
    hex3 = hex3 - hex2
    if hex3 == hex1:
        print("Subtraction Test Passed!")
    else:
        print("Subtraction Test Failed!")
    hex4 = Hex(-1,0,1)
    hex4 = hex4 * 2
    if hex4 == Hex(-2,0,2):
        print("Mult Test Passed!")
    else:
        print("Mult Test Failed!")

HEXES_HIGH = 30 # How many rows of hexes
HEXES_WIDE = 16 # How many hexes in a row
RADIUS = 30 # Size of a hex
HALF_RADIUS = RADIUS / 2.0
HALF_HEX_HEIGHT = math.sqrt(RADIUS ** 2 - HALF_RADIUS ** 2)
IMAGE_WIDTH =  int(HALF_HEX_HEIGHT * (HEXES_HIGH + 1))
IMAGE_HEIGHT = int(RADIUS * (HEXES_WIDE * 3 + .5))

map = [[None for i in range(HEXES_HIGH)] for j in range(HEXES_WIDE)]
a = 0
b = 0
for q in range(HEXES_WIDE):
    q_offset = math.floor(q/2)
    for r in range(-q_offset, HEXES_HIGH-q_offset):
        hex = Hex(q, r, -q-r)
        map[a][b] = hex
        b = b+1
    b = 0
    a = a+1

layout = Layout(orientation_flat, Point(30,30), Point(0,0))
image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), (0, 0, 0))
for q in range(HEXES_WIDE):
    for r in range(HEXES_HIGH):

        #colours = pil_colours()
        draw = ImageDraw.Draw(image, "RGBA")
        hex = map[q][r]
        tupleList = []
        for pt in polygon_corners(layout, hex):
            tupleList.append((pt.x, pt.y))
        draw.polygon(tupleList, fill=(255,255,255,255), outline=(0,0,0,255))

image.save('coordhex.png', 'PNG')
testHexEquals()
testArithmetic()

