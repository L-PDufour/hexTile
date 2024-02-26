from __future__ import division
from __future__ import print_function
import collections
import math
from tkinter import Tk, BOTH, Canvas

def hex_corner(center, size, i):
    angle_deg = 60 * i
    angle_rad = math.radians(angle_deg)
    x = center[0] + size * math.cos(angle_rad)
    y = center[1] + size * math.sin(angle_rad)
    return x, y


def draw_hexagon(canvas, center, size, color="green"):
    hexagon_coords = []
    for i in range(6):
        corner = hex_corner(center, size, i)
        hexagon_coords.extend(corner)
    hexagon_id = canvas.create_polygon(hexagon_coords, fill=color, outline="black")
    return hexagon_id


def main():
    root = Tk()
    root.title("Hexagon Drawing")

    canvas = Canvas(root, width=400, height=400)
    canvas.pack()

    draw_hexagon(canvas, (200, 200), 30, color="green")

    root.mainloop()

if __name__ == "__main__":
    main()
