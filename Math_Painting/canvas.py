import numpy as np
from PIL import Image


class Canvas:

    """Object where all shapes are going to be drawn"""
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

    def make(self, image_path):

        """Create a numpy array of zeros"""
        canvas = np.zeros((self.height, self.width, 3), np.uint8)

        if self.color == 'black':
            canvas[:] = [0, 0, 0]

        if self.color == 'white':
            canvas[:] = [255, 255, 255]

        """Convert the array of zeros into an image file"""
        img = Image.fromarray(canvas, 'RGB')
        img.save(f'{image_path}/canvas.png')
