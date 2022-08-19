

import itertools
import imageutils
import os

def validate_inputs(mat, filtermatrix) -> bool:

    # could functionally-lambdaly iterate over sizes and copare them
    x_shape_ok = mat.shape[0] > filtermatrix.shape[0];
    y_shape_ok = mat.shape[1] > filtermatrix.shape[1];

    return x_shape_ok and y_shape_ok

# def quick_binary_filter(mat, filtermatrix, break_decision) -> tuple:

#     valid = validate_inputs(mat, filtermatrix);
#     if not valid:
#         raise ValueError("filter is bigger than image");

#     x_iterations = mat.shape[0] - filtermatrix.shape[0] + 1
#     y_iterations = mat.shape[1] - filtermatrix.shape[1] + 1

#     for x, y in zip(x_iterations, y_iterations):
#         filter_value = filtermatrix[x,y]
#         mat_value = mat[]
#         if break_decision(x,y, filter_value):
#             return x, y

def create_rotation_filter(angle, size):

    this_script_path = os.path.dirname(os.path.realpath(__file__))
    filter_path = os.path.join(this_script_path, 'filter_img/direction_filter.png')

    direction_filter = imageutils.open_to_mat(filter_path)
    direction_filter = imageutils.rotate_image(direction_filter, angle)
    direction_filter = imageutils.resize_image(direction_filter, (size, size))

    img = imageutils.ImageShower()
    img.append_image(direction_filter, "direction filter")
    img.show_blackwhite()

    pass

def quick_binary_filter(mat, threshold) -> tuple:

    rows, cols = mat.shape

    for i in range(rows):
        for j in range(cols):
            if mat[i, j] > threshold:
                return i, j
      

def pick_point_of_interest(mat):
    return  quick_binary_filter(mat, 10)



    
    # would use fewer iterations if matrix was scanned n-th line
