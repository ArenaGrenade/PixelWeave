from Material import Material
from Metal import Metal
from Ray import Ray
import numpy as np
import math
from utils import *
from random import random

class Dielectric(Material):
    def __init__(self, ri):
        self.ref_idx = ri
    
    def scatter(self, in_ray, record):
        reflected = Metal.reflect(in_ray.direction, record["n"])
        if np.dot(in_ray.direction, record["n"]) > 0:
            outward_normal = - record["n"]
            refraction_ratio = self.ref_idx
            cosine = self.ref_idx * np.dot(in_ray.direction, record["n"]) / np.linalg.norm(in_ray.direction - np.zeros(3))
        else:
            outward_normal = record["n"]
            refraction_ratio = 1 / self.ref_idx
            cosine = - np.dot(in_ray.direction, record["n"]) / np.linalg.norm(in_ray.direction - np.zeros(3))
        
        is_refracted, refracted = Dielectric.refract(in_ray.direction, outward_normal, refraction_ratio)
        reflect_prob = 1.0
        if is_refracted:
            reflect_prob = Dielectric.schlick(cosine, self.ref_idx)
        if random() < reflect_prob:
            scattered_ray = Ray(record["p"], reflected)
        else:
            scattered_ray = Ray(record["p"], refracted)
        return True, scattered_ray, np.array([1, 1, 1])
    
    def schlick(cosine, ref_idx):
        r0 = (1 - ref_idx) / (1 + ref_idx)
        r0 **= 2
        return r0 + (1 - r0) * math.pow(1 - cosine, 5)
    
    @staticmethod
    def refract(in_vector, normal, refraction_ratio):
        unit_vector = in_vector / np.linalg.norm(in_vector)
        dt = np.dot(unit_vector, normal)
        discriminant = 1 - (refraction_ratio ** 2) * (1 - dt * dt)
        if discriminant > 0:
            return True, refraction_ratio * (in_vector - normal * dt) - normal * math.sqrt(discriminant)
        else:
            return False, None
