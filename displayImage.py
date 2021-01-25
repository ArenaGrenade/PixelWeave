import matplotlib.pyplot as plt
import numpy as np
import sys
from Ray import Ray
from utils import *
import time
import os

def color(ray, scene, depth, max_depth):
    cast_hit, hit_record = scene.hit(ray, 0, sys.float_info.max)
    if cast_hit:
        is_scatter, scattered_ray, attenuation = hit_record["mat"].scatter(ray, hit_record)
        if depth < max_depth and is_scatter:
            col = attenuation * color(scattered_ray, scene, depth + 1, max_depth)
            return col
        else:
            return np.zeros(3)
    else:
        unit_direction = ray.direction / np.linalg.norm(ray.direction)
        t = 0.5 * (unit_direction[1] + 1)
        col = (1 - t) * np.array([1.0, 1.0, 1.0]) + t * np.array([0.5, 0.7, 1.0])
        return col

def displayImage(image):
    oriented_image = np.flip(np.transpose(image, (1, 0, 2)), (0))
    final_image = oriented_image
    plt.imshow(final_image)
    plt.imsave(os.path.join("renders", "render-{timestamp}.png".format(timestamp=time.strftime("%d%m%Y-%H%M%S"))), final_image)
    plt.show()
