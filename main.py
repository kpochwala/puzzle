import imageutils
import filterutils

import glob, os

import numpy as np

this_script_path = os.path.dirname(os.path.realpath(__file__))
path_to_images = os.path.join(this_script_path,'./puzzle_img')
window_name = "puzzle"


def find_image_paths(path):
    images = []
    os.chdir(path)
    for file in glob.glob("*.png"):
        images.append(file)
    
    return images



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


def main():
    filter = filterutils.create_rotation_filter(30, 128)
    # generate_curve()
    # marker = imageutils.generate_x_marker(20);

    # image = marker

    # img.append_image(imageutils.rotate_image(image, 30), "marker")
    

if __name__ == "__main__":
    main()     

