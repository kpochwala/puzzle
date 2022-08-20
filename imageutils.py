import cv2, numpy as np
from matplotlib import pyplot as plt

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

        plt.show()

        return output_mat
    return wrapper


# https://pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/
@display_transform
def detect_edges(mat, sigma = 0.33):
    v = np.median(mat)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(mat, lower, upper)

    return edged


# https://stackoverflow.com/questions/9041681/opencv-python-rotate-image-by-x-degrees-around-specific-point
@display_transform
def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

@display_transform
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


def generate_x_marker(size):
    diagonal = np.identity(size)
    
    other_diagonal = np.rot90(diagonal, k=1, axes=(1,0))
    out = diagonal + other_diagonal

    return out

# https://stackoverflow.com/questions/40833073/insert-matrix-into-the-center-of-another-matrix-in-python
@display_transform
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


    return mat
