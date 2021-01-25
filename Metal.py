from Material import Material
from Ray import Ray
import numpy as np
from utils import *

class Metal(Material):
    def __init__(self, a, f):
        self.albedo = a
        self.fuzz = min(f, 1)
    
    def scatter(self, in_ray, record):
        unit_vector = in_ray.direction / np.linalg.norm(in_ray.direction)
        reflected = Metal.reflect(unit_vector, record["n"])
        scattered_ray = Ray(record["p"], reflected + self.fuzz * random_in_unit_sphere())
        return np.dot(scattered_ray.direction, record["n"]) > 0, scattered_ray, self.albedo

    @staticmethod
    def reflect(v, n):
        return v - 2 * np.dot(v, n) * n
