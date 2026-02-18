# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 07:04:48 2019

@author: JOHNJAIRO
"""

import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import warnings
import cv2

warnings.filterwarnings("ignore")
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)
# Using an existing stl file:
mesh = mesh.Mesh.from_file('E:\dicom dentista\paciente zero\Dentes\30986617_shell_occlusion_l.stl')
print("abertura mesh")
# Or creating a new mesh:
VERTICE_COUNT = 100
#data = np.zeros(VERTICE_COUNT, dtype=Mesh.dtype)
#mesh = mesh.Mesh(data, remove_empty_areas=False)

# The mesh normals (calculated automatically)
mesh.normals
# The mesh vectors
mesh.v0, mesh.v1, mesh.v2
# Accessing individual points (concatenation of v0, v1 and v2 in triplets)
mesh.points[0] == mesh.v0[0]
mesh.points[1] == mesh.v1[0]
mesh.points[2] == mesh.v2[0]
mesh.points[3] == mesh.v0[1]

print("m plot  ")
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(mesh.vectors))

# Auto scale to the mesh size
scale = mesh.points.flatten(-1)
axes.auto_scale_xyz(scale, scale, scale)
print("figuras  ")
# Show the plot to the screen
pyplot.show()
print("tipo variable ",type(mesh))
mesh.save('new_stl_file.stl')
print("figura final")

#cv2.imshow('sample image dicom',mesh)
