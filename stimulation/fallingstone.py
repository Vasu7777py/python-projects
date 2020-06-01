import time
import matplotlib.pyplot as plt
#import numpy as np

g = -9.80665

class falling_obj:
    def __init__(self, h_:float, u:float, mass:float, t_:float):
        self.h_ = h_
        self.u = u
        self.v = self.u
        self.mass = mass
        self.t = t_
        self.position = (0.0, self.h_, self.t)
        self.path = []
        self.path.append(self.position)
        self.bounce_count = 0

    def path_of_motion(self, acc:float):
        time.sleep(0.25)
        t = time.time()
        dt = t - self.t
        self.v += (self.u + (acc * dt))
        y = (self.v * dt)
        if (y < 0):
            print(y)
            y *= -1
            self.v *= -1
            self.bounce_count += 1
        self.position = (0.0, y, dt)
        self.path.append(self.position)

h = float(input("Enter the initial height : "))
u = float(input("Enter the initial velocity : "))
mass = float(input("Enter mass of the body : "))
t_ = time.time()
obj1 = falling_obj(h, u, mass, t_)

while (obj1.bounce_count <= 10):
    obj1.path_of_motion(g)

t_path = []
y_path = []
for move in obj1.path:
    t_path.append(move[2])
    y_path.append(move[1])
plt.plot(t_path, y_path)
plt.show()
