from Object import Object

class Scene(Object):
    def __init__(self, objects):
        self.objects = objects
        self.size = len(objects)
    
    def hit(self, ray, t_min, t_max):
        record = {}
        hit_anything = False
        closest_hit = t_max
        for object in self.objects:
            cast_hit, hit_rec = object.hit(ray, t_min, closest_hit)
            if cast_hit:
                hit_anything = True
                closest_hit = hit_rec["t"]
                record = hit_rec
        
        return hit_anything, record
