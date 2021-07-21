# 2. Create a program for drawing graphical objects as pixel, line, triangle, rectangle, circle.
# Using object-oriented programming class declaration, inheritance, polymorphism, etc. elements.
# For graphical drawing in Python ‘turtle’ library should be used.
import turtle
wn = turtle.Screen()


class MyTurtle(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("blue")
        self.shape("turtle")

    def rectangle(self):
        for i in range(4):
            self.forward(100)
            self.right(90)
        wn.mainloop()

    # I don't know is this correct as it is in Java to overload method?
    def rectangle(self, size):
        for i in range(4):
            self.forward(size)
            self.right(90)
        wn.mainloop()

    def triangle(self):
        for i in range(3):
            self.forward(100)
            self.right(120)
        wn.mainloop()

    def circleT(self):
        self.circle(100)
        wn.mainloop(3)

alex = MyTurtle()
alex.rectangle(200)
# alex.rectangle()
# alex.triangle()
# alex.circleT()

