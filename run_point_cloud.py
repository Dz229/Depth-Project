import numpy as np
import matplotlib.pyplot as plt
import os

# Settings
divider = 1 # Point cloud density divider (1 = no divider)
number_to_import = 3 # Number of depth map in folder to import (0 = first depth map)
connect_points = False # Connect points with lines (True/False)

# Import specific depth map in folder output_txt
loop_number = 0
for filename in os.listdir('output_txt'):
    if loop_number == number_to_import:
        depth_map = np.loadtxt('output_txt/' + filename)
    loop_number += 1

# Resize depth map for visualization
depth_map_resized = depth_map[::divider, ::divider]

# Plot depth map on 3D meshgrid
x = np.arange(0, depth_map_resized.shape[0], 1)
y = np.arange(0, depth_map_resized.shape[1], 1)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

for xx in x:
    #print % done
    if xx % 10 == 0:
        print("Progress: " + str(int(xx/depth_map_resized.shape[0]*100)) + "%")
    for yy in y:
        ax.scatter(xx, yy, depth_map_resized[xx, yy], c='black', marker='o')

# Connect points with lines if connect_points = True
if connect_points == True:
    for xx in x:
        for yy in y:
            if xx < depth_map_resized.shape[0]-1:
                ax.plot([xx, xx+1], [yy, yy], [depth_map_resized[xx, yy], depth_map_resized[xx+1, yy]], c='black')
            if yy < depth_map_resized.shape[1]-1:
                ax.plot([xx, xx], [yy, yy+1], [depth_map_resized[xx, yy], depth_map_resized[xx, yy+1]], c='black')

plt.show()
