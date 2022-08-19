import imageutils
import filterutils

import glob, os
from matplotlib import pyplot as plt

import numpy as np

this_script_path = os.path.dirname(os.path.realpath(__file__))
path_to_images = os.path.join(this_script_path,'./puzzle_img')
window_name = "puzzle"

# decorator to display mat->mat transform 
def display_transform(func):
    def wrapper(*args, **kwargs):
        input_mat = args[0]
        print("Display transform before: ")
        output_mat = func(*args, **kwargs)
        print("Display transform after: ")

        print(input_mat)
        print(output_mat)

        fig, axs = plt.subplots(1, 2, constrained_layout=True)        
        axs[0].imshow(input_mat, cmap='gray')
        axs[0].set_title("Input")
        axs[0].set_xlabel('x')
        axs[0].set_ylabel('y')

        axs[1].imshow(output_mat, cmap='gray')
        axs[1].set_title("Output")
        axs[1].set_xlabel('x')
        axs[1].set_ylabel('y')

        fig.suptitle(func.__name__)

        # plt.subplot(1, 2, 1), 
        # plt.title("Input")
        
        # plt.subplot(1, 2, 2), plt.imshow(output_mat, cmap='gray')
        
        # plt.savefig('final_image_name.extension') # To save figure
        plt.show()

        return output_mat
    return wrapper


def find_image_paths(path):
    images = []
    os.chdir(path)
    for file in glob.glob("*.png"):
        images.append(file)
    
    return images

@display_transform
def select_rectangle(mat):
    return mat
    pass

def generate_curve():
    image_paths = find_image_paths(path_to_images)

    img = imageutils.ImageShower()

    print(image_paths)

    for path in image_paths:

        image = imageutils.open_to_mat(path)

        mat = imageutils.detect_edges(image)

        poi = filterutils.pick_point_of_interest(mat)
        print("point of interest")
        print(poi)
        
        if poi is not None:
            mat = imageutils.put_marker(mat, poi)

        

        img.append_image(mat, path)

    img.show_blackwhite()


#
def score(mat, mask):
    if mat.shape != mask.shape:
        raise ValueError("image part must be the same size as filter kernel")

    return np.sum(mat*mask)

    


# return an array of filter matrices with the param generated by the range
# def arrange_filters(filter_function, size, range_generator):
#     filters = []
#     for value in range_generator:
#         filters.append(filter, ))
#     pass

def main():

    filter_angles = np.arange(-90, 90, 22.5)

    size = 5

    mat = filterutils.create_rotation_filter(30, size)
    mat = select_rectangle(mat)

    # filters = {}
    # for angle in filter_angles:
    #     filters[angle] = filterutils.create_rotation_filter(angle, size)

    # generate_curve()
    # marker = imageutils.generate_x_marker(20);

    # image = marker

    # img.append_image(imageutils.rotate_image(image, 30), "marker")
    

if __name__ == "__main__":
    main()     

