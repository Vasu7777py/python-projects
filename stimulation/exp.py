import numpy as np

PIE = (22/7)

angle = float(input("Enter an angle : "))

def rad(angle:float):
    angle_r = ((angle * PIE)/180)
    return angle_r

print(f"tan : {np.tan(rad(angle))}")