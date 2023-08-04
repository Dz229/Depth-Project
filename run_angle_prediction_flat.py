import numpy as np
import os 

input_folder_path = "output_txt/"
output_folder_path = "output_angle/"
pixels_range = 15 # the range of pixels to calculate the average difference

output_txt_1 = []
output_txt_2 = []
output_txt_3 = []

for file in os.listdir(input_folder_path):
    file_path = os.path.join(input_folder_path, file) # get the file path
    depth_numpy = np.loadtxt(file_path) # load
    
    #First approach
    avg_diff = np.mean(np.diff(depth_numpy[:,:pixels_range])) # calculate the average difference
    output_txt_1.append(avg_diff) # append to the output list
    
    #Second approach
    mean = np.mean(depth_numpy[:,:pixels_range]) # calculate the mean
    reduced_values_sum = np.sum(depth_numpy[:,:pixels_range] - mean) # calculate the sum of the reduced values
    output_txt_2.append(reduced_values_sum) # append to the output list
    
    #Third approach
    std = np.std(depth_numpy[:,:pixels_range]) # calculate the standard deviation
    output_txt_3.append(std) # append to the output list
    
np.savetxt(output_folder_path + "avg_diff_1.txt", output_txt_1, fmt='%1.3f') # save as txt
np.savetxt(output_folder_path + "avg_diff_2.txt", output_txt_2, fmt='%1.3f') # save as txt
np.savetxt(output_folder_path + "avg_diff_3.txt", output_txt_3, fmt='%1.3f') # save as txt


#Testing the treshold
treshold = 0.250
cnt = 0
for i in output_txt_3:
    if i > treshold:
        print(f"Image {cnt}: True")
        cnt += 1
    else:
        print(f"Image {cnt}: False")
        cnt += 1