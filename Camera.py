from Ray import Ray
import numpy as np
import math
from utils import *

class Camera:
    def __init__(self, lookfrom, lookat, vup, fov, aspect, aperture, focus_distance):
        theta = math.radians(fov)
        h = math.tan(theta / 2)
        viewport_height = 2 * h
        viewport_width = aspect * viewport_height

        self.w = unit_vector(lookfrom - lookat)
        self.u = unit_vector(np.cross(vup, self.w))
        self.v = np.cross(self.w, self.u)

        self.origin = lookfrom
        self.horizontal = viewport_width * focus_distance * self.u
        self.vertical = viewport_height * focus_distance * self.v
        self.lower_left_corner = self.origin - self.horizontal / 2 - self.vertical / 2 - focus_distance * self.w

        self.lens_radius = aperture / 2
        """
        print(self.origin)
        print(self.horizontal)
        print(self.vertical)
        print(self.lower_left_corner)
        print(viewport_height)
        print(viewport_width)
        """
    
    def get_ray(self, s, t):
        rd = self.lens_radius * random_in_unit_disk()
        offset = self.u * rd[0] + self.v * rd[1]
        return Ray(
            self.origin + offset,
            self.lower_left_corner + 
            s * self.horizontal + 
            t * self.vertical -
            self.origin -
            offset
        )
