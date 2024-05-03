from canvas import Canvas
from shapes import Square, Rectangle

# Ask for the canvas size and color
width = int(input('Enter Canvas width '))
height = int(input('Enter Canvas height '))
canvas_color = input('Enter canvas color (white or black) ')

# Create a canvas object
canvas = Canvas(width, height, canvas_color)
canvas.make('C:/Users/sebas/OneDrive/Escritorio/Cursos/Udemy/10 OOP Projects/MyOwnProjects/Math_Painting')

while True:
    shape = input('What do you like to draw? (rectangle, square) Enter quit to quit. ')

    # If the user entered rectangle. The program will ask for the rectangle data and will create it and draw it.
    if shape == 'rectangle':
        x_rectangle = int(input('Enter x of the rectangle: '))
        y_rectangle = int(input('Enter y of the rectangle '))
        w_rectangle = int(input('Enter the width of the rectangle '))
        h_rectangle = int(input('Enter the  height of the rectangle '))
        r = int(input('How much red should the rectangle have? '))
        g = int(input('How much green should the rectangle have? '))
        b = int(input('How much blue should the rectangle have? '))

        rectangle = Rectangle(x_rectangle, y_rectangle, w_rectangle, h_rectangle, (r, g, b))
        rectangle.draw('C:/Users/sebas/OneDrive/Escritorio/Cursos/Udemy/10 OOP Projects'
                       '/MyOwnProjects/Math_Painting/canvas.png')

    # If the user entered square. The program will ask for the square data and will create it and draw it.
    if shape == 'square':
        x_square = int(input('Enter x of the square: '))
        y_square = int(input('Enter y of the square '))
        side_rectangle = int(input('Enter the side length of the square '))
        r = int(input('How much red should the rectangle have? '))
        g = int(input('How much green should the rectangle have? '))
        b = int(input('How much blue should the rectangle have? '))

        square = Square(x_square, y_square, side_rectangle, (r, g, b))
        square.draw('C:/Users/sebas/OneDrive/Escritorio/Cursos/Udemy/10 OOP Projects'
                    '/MyOwnProjects/Math_Painting/canvas.png')

    # Break the loop if user entered 'quit'
    if shape == 'quit':
        break

