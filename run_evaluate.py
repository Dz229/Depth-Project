import torch
from zoedepth.utils.misc import get_image_from_url, colorize
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

#Load the model
zoe = torch.hub.load(".", "ZoeD_N", source="local", pretrained=True)

import os
input_folder_path = "input_images_2/"
output_folder_path = "output_images/"
output_txt_folder_path = "output_txt/"

for file in os.listdir(input_folder_path):
    file_path = os.path.join(input_folder_path, file) # get the file path
    image = Image.open(file_path).convert("RGB") # load
    depth_numpy = zoe.infer_pil(image)  # as numpy
    np.savetxt(output_txt_folder_path + file + ".txt", depth_numpy, fmt='%1.3f') # save as txt
    output_image = plt.imsave(output_folder_path + file, depth_numpy, cmap='gray') # save as image



