import numpy as np
import math
import random
import string
from Object import Object

class Sphere(Object):
    def __init__(self, center, radius, material, name=None):
        if name:
            self.name = name
        else:
            self.name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        self.center = center
        self.radius = radius
        self.material = material
    
    def hit(self, ray, t_min, t_max):
        oc = ray.origin - self.center
        a = np.dot(ray.direction, ray.direction)
        b = np.dot(oc, ray.direction)
        c = np.dot(oc, oc) - self.radius * self.radius
        discriminant = b * b - a * c

        if discriminant > 0:
            t = (-b - math.sqrt(discriminant)) / a
            if t < t_max and t > t_min:
                return self.populate_record(ray, t)
            t = (-b + math.sqrt(discriminant)) / a
            if t < t_max and t > t_min:
                return self.populate_record(ray, t)
        
        return False, {}
    
    def populate_record(self, ray, t):
        record = {}
        record["t"] = t
        record["p"] = ray.point_at_parameter(t)
        record["n"] = (record["p"] - self.center) / self.radius
        record["mat"] = self.material
        return True, record
