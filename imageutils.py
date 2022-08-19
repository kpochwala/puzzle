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

def resize_image(mat, shape):
    return cv2.resize(mat, shape)


# just this
def open_to_mat(image_path):
    return cv2.imread(image_path).astype(np.float32)/256


# # show image from path using opencv stuff
# def display_image(path):
#     print(path)
#     mat = cv2.imread(path)
#     cv2.imshow(window_name, mat)



class ImageShower():

    images = []
    fig = None
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
    
    other_diagonal = np.rot90(diagonal, k=1, axes=(1,0))
    out = diagonal + other_diagonal

    return out

# https://stackoverflow.com/questions/40833073/insert-matrix-into-the-center-of-another-matrix-in-python
def put_marker(mat, position, marker_size = 10):

    marker = generate_x_marker(marker_size)

    marker = np.ones(marker_size**2).reshape(marker_size, marker_size)

    # nb = mat.shape[0]
    # na = marker.shape[0]
    


    # lower = nb - position
    # upper = nb - position + na

    # lower = (nb) // 2 - (na // 2)
    # upper = (nb // 2) + (na // 2)
    
    # print("matrix size: ({}, {})".format(mat.shape))

    lower = position
    upper = position + marker.shape

    print(marker)
    print(mat.shape)



    print(mat[position[0]: position[0] + marker.shape[0], position[1]:position[1]+marker.shape[1]])


    mat[position[0]: position[0] + marker.shape[0], position[1]:position[1]+marker.shape[1]] = marker*100


    show = ImageShower()
    print(mat)
    show.append_image(mat, "debug")
    show.show()

    return mat
