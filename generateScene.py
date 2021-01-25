from Sphere import Sphere
from Scene import Scene
from Dielectric import Dielectric
from Metal import Metal
from Lambert import Lambert
from utils import *

import numpy as np
from random import random

def random_scene():
    scene_objects = [Sphere(np.array([0, -1000, 0]), 1000, Lambert(np.array([0.5, 0.5, 0.5])))]
    for i in range(-11, 11):
        for j in range(-11, 11):
            center = np.array([i + 0.9 * random(), 0.2, j + 0.9 * random()])
            if np.linalg.norm(center - np.array([4, 0.2, 0])) > 0.9:
                choose_mat = random()
                if choose_mat < 0.6:
                    material = Lambert(np.random.random(3))
                elif choose_mat < 0.85:
                    material = Metal(np.random.random(3), 0.5 * random())
                else:
                    material = Dielectric(1.5)
                scene_objects.append(Sphere(center, 0.2, material))
    
    scene_objects.append(Sphere(np.array([0, 1, 0]), 1, Dielectric(1.5)))
    scene_objects.append(Sphere(np.array([-4, 1, 0]), 1, Lambert(np.array([0.4, 0.2, 0.1]))))
    scene_objects.append(Sphere(np.array([4, 1, 0]), 1, Metal(np.array([0.7, 0.6, 0.5]), 0.0)))
    return Scene(scene_objects)
