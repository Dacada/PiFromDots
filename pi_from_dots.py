#!/usr/bin/env python3

"""Approximate pi by randomly placing dots and seeing how many fall inside a
circle and how many do not.

A circle of radius 0.5 inscribed inside a square of side 1. The origin 0,0 is
in one of the corners of the square. Random points (x,y) with x,y in the
interval [0,1) are generated. Since the area of this square is (2r)²=4r² and
the area of a circle is πr² the division of the number of points in the circle
by the number of points in total will be π/4.

After approximating pi, show an image of how the circle looks like.

"""

import subprocess
import tempfile
import random
import math
import sys
from PIL import Image, ImageDraw


def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def print_usage(name):
    print("Usage:")
    print(f"  {name} [points]")
    print()
    print('Approximate pi by "throwing darts". Uses the given number of '
          'points ("darts").')
    exit(1)


def get_num_dots():
    name = ""
    args = sys.argv
    if len(args) == 0:
        print_usage("")
    name = args[0]

    if len(args) != 2:
        print_usage(name)

    try:
        return int(args[1])
    except ValueError:
        print_usage(name)


def image_init(size):
    white = (255, 255, 255)
    red = (255, 0, 0)
    im = Image.new('RGB', (size, size), color=white)
    draw = ImageDraw.Draw(im)
    draw.ellipse((0, 0, size-1, size-1), fill=white, outline=red)
    return im


def approximate_pi(ndots):
    side = 1024
    im = image_init(side)
    px = im.load()

    inside = 0
    center = (0.5, 0.5)
    for dot in range(ndots):
        x = random.random()
        y = random.random()

        dist = distance((x, y), center)
        if dist <= 0.5:
            inside += 1
            color = (0, 255, 0)
        else:
            color = (0, 0, 255)

        px[x*side, y*side] = color
    pi = inside / ndots * 4

    return inside, pi, im


def show_image(im):
    with tempfile.NamedTemporaryFile('wb') as f:
        im.save(f, "PNG")
        subprocess.run(('eog', f.name))


def main():
    num_dots = get_num_dots()
    dots_inside, pi, im = approximate_pi(num_dots)
    print(f"total dots: {num_dots}")
    print(f"dots inside the circle: {dots_inside}")
    print(f"pi = {pi}")
    show_image(im)


if __name__ == '__main__':
    exit(main())
