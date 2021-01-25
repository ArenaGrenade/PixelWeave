from displayImage import color, displayImage
from Scene import Scene
from Sphere import Sphere
from Camera import Camera
import numpy as np
from random import random
from progress.bar import Bar
import math
from Lambert import Lambert
from Metal import Metal
from Dielectric import Dielectric
from generateScene import random_scene

def main():
    aspect_ratio = 16 / 9
    nx = 180
    ny = int(nx / aspect_ratio)
    ns = 3
    print("Size: ", nx, ny)

    image = np.zeros((nx, ny, 3))
    scene = random_scene()

    # Normal (0, 0, 0), (0, 0, -1), (0, 1, 0), 90, nx / ny
    lookfrom = np.array([13, 2, 3])
    lookat = np.array([0, 0, 0])
    focus_dist = 10.0
    camera = Camera(lookfrom, lookat, np.array([0, 1, 0]), 20, nx / ny, 0, focus_dist)

    bar = Bar("Processing", max = nx * ny * ns, fill="-", suffix='%(percent)d%%    %(index)d / %(max)d  [%(elapsed_td)s : %(eta_td)s]')
    for j in range(ny - 1, -1, -1):
        for i in range(nx):
            col = np.zeros(3)
            for s in range(ns):
                u = (i + random()) / nx
                v = (j + random()) / ny
                ray = camera.get_ray(u, v)
                col += color(ray, scene, 0, 1)
                bar.next()
            
            col /= ns
            col = np.vectorize(math.sqrt)(col)
            image[i][j] = col
    
    bar.finish()
    displayImage(image)

if __name__ == '__main__':
    main()
