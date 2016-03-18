"""
quantic-bolt's Map TILER
@quantic_bolt
v1.0_alpha
Manual map tiler with built in tiles. Feel free to use your own tiles.
Part of an initiative to make a Pokemon style RPG.
Uses matrix tiling to generate map graphics.
"""

from PIL import Image # Imports image class.

tileMatrix = open("map.txt") # Opens tile matrix.
lst = []
while True:
    c = tileMatrix.read(1)
    lst.append(c)
    if not c:
      break

imageEx = ".bmp"
name = ""

myMap = Image.new("RGB", (54,54))

c=0
i=0
j=0
while c<len(lst)-1:
    if lst[c] != "\n":
        im = Image.open(lst[c]+imageEx)
        myMap.paste(im,(i,j))
        i = i + 18
        c = c + 1
    elif lst[c] == "\n":
        i = 0
        j = j + 18
        c = c + 1

myMap.show()
