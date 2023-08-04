import numpy as np
import matplotlib.pyplot as plt
import os

# Settings
divider = 10 # Point cloud density divider (1 = no divider)
line_density = 150 # Line density for contour plot
number_to_import = 1 # Number of depth map in folder to import (0 = first depth map)
apply_texture = False # Apply texture from original image (True/False)

# Import specific depth map in folder output_txt
loop_number = 0
for filename in os.listdir('output_txt'):
    if loop_number == number_to_import:
        depth_map = np.loadtxt('output_txt/' + filename)
    loop_number += 1
    
# Import original image for texture
if apply_texture == True:
    loop_number = 0
    for filename in os.listdir('input_images'):
        if loop_number == number_to_import:
            img = plt.imread('input_images/' + filename)
            plt.imshow(img)
        loop_number += 1
    
# Resize depth map for visualization and create x, y, z
depth_map_resized = depth_map[::divider, ::divider]
y = np.arange(0, depth_map_resized.shape[0], 1)
x = np.arange(0, depth_map_resized.shape[1], 1)
X, Y = np.meshgrid(x, y)
Z = depth_map_resized

# Plot 3D meshgrid
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, line_density, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.view_init(-90, -90)


#####################################################
###TODO                                           ###
###Convert mesh to blender file using blender api ###
#####################################################


# Apply a photo texture on the 3D meshgrid from the original image
if apply_texture == True:
    # Resize original image to match depth map
    img_resized = img[::divider, ::divider]
    # Plot photo texture on 3D meshgrid
    ax.plot_surface(X, Y, Z, facecolors=img_resized)

plt.show()
