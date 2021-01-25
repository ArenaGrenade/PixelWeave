import numpy as np

class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction
    
    def point_at_parameter(self, t_param):
        return self.origin + t_param *  self.direction
