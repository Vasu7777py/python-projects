import vectors

g = vectors.PredefinedVectors.AccDueToGravity()
F = vectors.Force([0.98, 876, 87])
'''
print(type(F))
print(f"Magnitude : {F.Force.Magnitude}")
print(f"Direction : {F.Force.Direction}")
print(f"Unit : {F.Unit}")
'''
print(F.Vector.Angles)