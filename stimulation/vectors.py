import numpy as np

class _1D_vector_:
    def __init__(self, magnitude:float, position:tuple):
        self.magnitude = magnitude
        self.position = position

    def reverse_vector(self):
        self.magnitude *= -1

class _2D_vector_:
    def __init__(self, magnitude:float, angle:float, position:tuple):
        self.magnitude = magnitude
        self.angle = angle
        self.position = position

    def reverse_vector(self):
        self.magnitude *= -1
        self.angle = self.angle