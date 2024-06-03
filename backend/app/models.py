class Material:
    def __init__(self, id, name, transparency, density, stiffness):
        self.id = id
        self.name = name
        self.transparency = transparency
        self.density = density
        self.stiffness = stiffness

class Object:
    def __init__(self, id, name, min_transparency, max_density, min_stiffness):
        self.id = id
        self.name = name
        self.min_transparency = min_transparency
        self.max_density = max_density
        self.min_stiffness = min_stiffness
