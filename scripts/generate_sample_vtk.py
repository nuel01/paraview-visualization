#!/usr/bin/env python3
import numpy as np

nx, ny, nz = 20, 20, 20
x = np.linspace(-1, 1, nx)
y = np.linspace(-1, 1, ny)
z = np.linspace(-1, 1, nz)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
# synthetic scalar: spherical + sinusoidal variation
T = 300 + 50 * np.exp(-5*(X**2+Y**2+Z**2)) + 20*np.sin(3*X)*np.cos(3*Y)

with open('data/sample.vtk', 'w') as f:
    f.write("# vtk DataFile Version 2.0\n")
    f.write("Simple scalar field\n")
    f.write("ASCII\n")
    f.write("DATASET STRUCTURED_POINTS\n")
    f.write(f"DIMENSIONS {nx} {ny} {nz}\n")
    f.write("ORIGIN 0 0 0\n")
    f.write("SPACING 1 1 1\n")
    f.write(f"POINT_DATA {nx*ny*nz}\n")
    f.write("SCALARS Temperature float 1\n")
    f.write("LOOKUP_TABLE default\n")
    flat = T.ravel()
    for i, val in enumerate(flat):
        f.write(f"{val:.6f} ")
        if (i+1) % 10 == 0:
            f.write("\n")
