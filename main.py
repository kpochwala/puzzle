import imageutils

import glob, os

import numpy as np

path_to_images = '/home/kpo/git/puzzle/puzzle_img'
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
        img.append_image(mat, path)

    img.show_blackwhite()


def main():
    img = imageutils.ImageShower()

    marker = imageutils.generate_x_marker(20);

    image = marker

    img.append_image(imageutils.rotate_image(image, 30), "marker")
    img.show_blackwhite()
    

if __name__ == "__main__":
    main()     

