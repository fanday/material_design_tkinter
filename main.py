from tkinter import *

root = Tk()

canvas = Canvas(root, width=500, height=500, bg='black', highlightthickness=0)
canvas.pack()

class CanvasButton(Canvas):

    def __doc__(self):
        # todo tag, binding, event handling/rules
        """
            This docstring mostly serves as a note for myself.
            Creates a shadowed button by nesting a canvas to hold a canvas.
            This is dependent on the parent being passed in to be a canvas.

            The layers are as follows (parents to children order):

                Parent canvas (not included in class)
                    shadow_window
                        shadow_canvas
                            window
                                canvas
                                    label

            # Parent for shadow_window = your outer canvas name
            # x, y for shadow_window position in parent canvas
            # size of canvas consider this as your button size
            # color of canvas consider this as your button color

            # text
            # text color
            # font style
            # font size

            # binding ?
            # tag ?
            # event ?
        """

    def __init__(self, parent=canvas, x=26, y=26, z=1, canvas_width=50, canvas_height=50,
                 canvas_color='white', text='PRESS ME!', text_color='black',
                 font_style="Verdana", font_size=10):

        # Call to super class __init__
        Canvas.__init__(self)

        # sets outermost canvas (not in class) as parent for shadow window and shadow canvas
        ''' Inner window/ inner canvas are grandchildren of this parent '''
        self.parent = parent

        # sets x and y position of outer window
        self.x = x
        self.y = y
        # todo will be used for drawing shadow size, consider it like material designs z level
        self.z = z

        # sets inner canvas width, height, and color
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.canvas_color = canvas_color

        # set shadow containing canvas width and height
        self.width_z = self.canvas_width + (self.z * 2) + 1
        self.height_z = self.canvas_height + (self.z * 2) + 1

        # sets inner canvas display text and color
        self.text = text
        self.text_color = text_color
        self.font_style = font_style
        self.font_size = font_size

        # *****************************************************
        # Outer for shadow

        # create canvas for the shadow
        self.shadow_canvas = Canvas(self.parent, width=self.width_z, height=self.height_z,
                                    bg='white', highlightthickness=0, bd=0)

        # create window that will hold the shadow canvas
        self.shadow_window = self.parent.create_window(self.x, self.y, window=self.shadow_canvas)

        # *****************************************************
        # Inner for button

        # Creates inner canvas
        self.canvas = Canvas(self.shadow_canvas, width=self.canvas_width, height=self.canvas_height,
                             bg=self.canvas_color, highlightthickness=0, bd=0)

        # creates window in outer canvas and sets inner canvas as child
        self.window = self.shadow_canvas.create_window(self.width_z / 2, self.height_z / 2 - (z/3), window=self.canvas)

        # creates label for inner canvas
        self.label = self.canvas.create_text(self.canvas_width/2, self.canvas_height/2, text=self.text,
                                             fill=self.text_color, font=(self.font_style, self.font_size),
                                             width=self.canvas_width)


test_1 = CanvasButton(canvas_color='red', text_color='yellow')
test_2 = CanvasButton(x=200, y=100, z=10, canvas_color='blue', text_color='yellow', canvas_width=100)
test_3 = CanvasButton(x = 100, y= 200, z=5, canvas_color='maroon', text_color='pink')
test_4 = CanvasButton(x=300, y=300, z=20, canvas_width=200, canvas_height=250, canvas_color='orange')


root.mainloop()