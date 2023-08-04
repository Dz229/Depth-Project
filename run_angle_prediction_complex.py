import numpy as np
import os

input_folder_path = "output_txt/"
output_folder_path = "output_angle/"
pixels_range_tab = [15,50,100,150,200] # the range of pixels to calculate the average difference

for pixels_range in pixels_range_tab:
    print(f"Pixels range: {pixels_range}")
    
    output_txt_1 = []
    output_txt_2 = []
    output_txt_3 = []
    
    for file in os.listdir(input_folder_path):
        print(f"File: {file}")
        file_path = os.path.join(input_folder_path, file) # get the file path
        depth_numpy = np.loadtxt(file_path) # load the txt file
        mean_values = np.mean(depth_numpy[:,:pixels_range], axis=1) # calculate the mean of the values
        
        #First approach - polynomial fit and math formula between two points (first and last)
        line_function = np.polyfit(np.arange(0, len(mean_values)), mean_values, 1) # calculate the line function
        first_point = np.array([0, line_function[1]]) # get the first point
        last_point_x = len(mean_values) # get the last point x
        last_point = np.array([last_point_x, line_function[0]*last_point_x + line_function[1]]) # get the last point
        tng_alpha_angle = (last_point[1]-first_point[1])/(last_point[0]-first_point[0]) # calculate the tng alpha
        degrees_alpha_angle_left = np.degrees(np.arctan(tng_alpha_angle)) # calculate the angle in degrees
        output_txt_1.append(degrees_alpha_angle_left) # append to the output list
        
        #Second approach - math formula between two points (min and max)
        min_point = np.array([np.argmin(mean_values), np.min(mean_values)]) # get the min point
        max_point = np.array([np.argmax(mean_values), np.max(mean_values)]) # get the max point
        #Tng alpha = a/b where a is height and b is width
        tng_alpha_angle = (max_point[1]-min_point[1])/(max_point[0]-min_point[0]) # calculate the tng alpha
        degrees_alpha_angle = np.degrees(np.arctan(tng_alpha_angle)) # calculate the angle in degrees
        output_txt_2.append(degrees_alpha_angle) # append to the output list
        
        #Third approach - polynomial fit and math formula between two points (first and last) + calculating mean between pixels from the left and right side
        right_side_limit = depth_numpy.shape[1] - pixels_range # calculate the right side limit
        mean_values_right = np.mean(depth_numpy[:,right_side_limit:], axis=1) # calculate the mean of the values from the right side
        line_function_right = np.polyfit(np.arange(0, len(mean_values_right)), mean_values_right, 1) # calculate the line function
        first_point_right = np.array([0, line_function_right[1]]) # get the first point
        last_point_x_right = len(mean_values_right) # get the last point x
        last_point_right = np.array([last_point_x_right, line_function_right[0]*last_point_x_right + line_function_right[1]]) # get the last point
        tng_alpha_angle_right = (last_point_right[1]-first_point_right[1])/(last_point_right[0]-first_point_right[0]) # calculate the tng alpha
        degrees_alpha_angle_right = np.degrees(np.arctan(tng_alpha_angle_right)) # calculate the angle in degrees
        two_sides_mean = (degrees_alpha_angle_left + degrees_alpha_angle_right)/2 # calculate the mean of the angles
        output_txt_3.append(two_sides_mean) # append to the output list
        
        #TODO: Fourth approach - not counting the wall background, then polynomial fit and math formula between two points (first and last) + calculating mean between pixels from the left and right side
        #WIll be implemented in another file - run_angle_prediction_complex_half.py
        
    np.savetxt(output_folder_path + "complex_angle_1_range_" + str(pixels_range) + ".txt", output_txt_1, fmt='%1.3f') # save as txt
    np.savetxt(output_folder_path + "complex_angle_2_range_" + str(pixels_range) + ".txt", output_txt_2, fmt='%1.3f') # save as txt
    np.savetxt(output_folder_path + "complex_angle_3_range_" + str(pixels_range) + ".txt", output_txt_3, fmt='%1.3f') # save as txt
