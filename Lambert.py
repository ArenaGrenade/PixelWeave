from Material import Material
from Ray import Ray
from utils import *

class Lambert(Material):
    def __init__(self, a):
        self.albedo = a
    
    def scatter(self, in_ray, record):
        target = record["p"] + record["n"] + random_in_unit_sphere()
        scattered_ray = Ray(record["p"], target - record["p"])
        return True, scattered_ray, self.albedo
