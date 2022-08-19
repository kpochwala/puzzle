import cv2, numpy as np
from matplotlib import pyplot as plt


# https://pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/
def detect_edges(mat, sigma = 0.33):
    v = np.median(mat)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(mat, lower, upper)

    return edged


# https://stackoverflow.com/questions/9041681/opencv-python-rotate-image-by-x-degrees-around-specific-point
def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

# just this
def open_to_mat(image_path):
    return cv2.imread(image_path)


# # show image from path using opencv stuff
# def display_image(path):
#     print(path)
#     mat = cv2.imread(path)
#     cv2.imshow(window_name, mat)



class ImageShower():

    images = []

    def __init__(self):
        pass

    def append_image(self, mat, image_name):
        self.images.append((mat, image_name))       

    def show_color(self):
        for mat, image_name  in self.images:
            plt.imshow(mat, cmap="brg")
            self.show()

    def show_blackwhite(self):
        for mat, image_name  in self.images:
            print("Runniong show on image name: {}".format(image_name))
            plt.imshow(mat, cmap="gray")
            self.show()

    def show(self):
        plt.show()


def generate_x_marker(size):
    diagonal = np.identity(size)
    
    print(diagonal)
    other_diagonal = np.rot90(diagonal, k=1, axes=(1,0))
    print(other_diagonal)
    out = diagonal + other_diagonal

    return out