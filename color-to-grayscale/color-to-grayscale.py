import numpy as np
def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    res = []
    for row in image:
        gray = []
        for pixl in row:
            gray.append(np.dot(pixl, [0.299, 0.587, 0.114]))
        res.append(gray)
    return res