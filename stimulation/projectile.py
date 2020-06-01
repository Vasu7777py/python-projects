import matplotlib.pyplot as plt
import numpy as np
import time

import utility.Math as math

#   G = (6.67/np.power(10, 11))
g = -9.80665

I_angle = float(input("Enter the initial angle : "))
I_velocity = float(input("Enter the initial velocity : "))
v0_x = I_velocity * np.cos(math.angles.rad(I_angle))
v0_y = I_velocity * np.sin(math.angles.rad(I_angle))
v0 = (v0_x, v0_y)
x0, y0 = 0, 0
position = (x0, y0, 0.0)
path = []
path.append(position)
t0 = 0

def path_of_projectile(curr_position:tuple, acc:float, dt:float):
    x, y = curr_position[0], curr_position[1]
    vy = (v0_y + (acc*dt))
    vx = v0_x
    x = (vx * dt)
    y = (vy * dt)
    path.append((x, y, dt))
    return (x, y)

t = t0
while position[1] >= 0:
    dt = t - t0
    position = path_of_projectile(position, g, dt)
    t += 1

x_path = []
y_path = []
for move in path:
    x_path.append(move[2])
    y_path.append(move[1])

print(max(y_path), x_path[-1])

plt.plot(x_path, y_path)
plt.show()