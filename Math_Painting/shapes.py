import numpy as np
from PIL import Image


class Square:

    """A square shape that can be drawn on a canvas object"""
    def __init__(self, x, y, side, color):
        self.x = int(x)
        self.y = int(y)
        self.side = int(side)
        self.color = color

    def draw(self, canvas):

        """Draws itself into the canvas object"""
        img = Image.open(canvas)
        img_data = np.array(img)

        # Changes a slice of the array with new values
        img_data[self.x: self.x + self.side, self.y: self.y + self.side, :] = \
                [self.color[0], self.color[1], self.color[2]]

        img = Image.fromarray(img_data, 'RGB')
        img.save('canvas.png')


class Rectangle:

    """A rectangle shape that can be drawn on a canvas object"""

    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):

        """Draws itself into the canvas object"""

        img = Image.open(canvas)
        img_data = np.array(img)

        img_data[self.x: self.x + self.width, self.y: self.y + self.height, :] = \
                [self.color[0], self.color[1], self.color[2]]
        img = Image.fromarray(img_data, 'RGB')
        img.save('canvas.png')
