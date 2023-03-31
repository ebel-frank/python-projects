import turtle
import math

screen = turtle.Screen()
screen.bgcolor("skyblue")

george = turtle.Turtle()
george.color("black")
george.shape("turtle")
george.speed(1)


class MyHouse:
    # def a function to draw and fill a rectangle
    def drawRectangle(t, width, height, color):
        t.fillcolor(color)
        t.begin_fill()
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.end_fill()

    # def a function to draw and fill a triangle
    def drawTriangle(t, length, color):
        t.fillcolor(color)
        t.begin_fill()
        t.forward(length)
        t.left(135)
        t.forward(length / math.sqrt(2))
        t.left(90)
        t.forward(length / math.sqrt(2))
        t.left(135)
        t.end_fill()

    # def a function to draw and fill a parrallelogram
    def drawParralelogarm(t, width, height, color):
        t.fillcolor(color)
        t.begin_fill()
        t.left(30)
        t.forward(width)
        t.left(60)
        t.forward(height)
        t.left(120)
        t.forward(width)
        t.left(60)
        t.forward(height)
        t.left(90)
        t.end_fill()

    # draw and fill front of the house
    george.penup()
    george.goto(-150, -120)
    george.pendown()
    drawRectangle(george, 100, 110, "blue")
    # draw and fill the front door
    george.penup()
    george.goto(-120, -120)
    george.pendown()
    drawRectangle(george, 40, 60, "lightgreen")
    # Front roof
    george.penup()
    george.goto(-150, -10)
    george.pendown()
    drawTriangle(george, 100, "magenta")
    # Side of the house
    george.penup()
    george.goto(-50, -120)
    george.pendown()
    drawParralelogarm(george, 60, 110, "yellow")
    # Window
    george.penup()
    george.goto(-40, -70)
    george.pendown()
    drawParralelogarm(george, 30, 50, "red")
    # side roof
    george.penup()
    george.goto(-50, -10)
    george.pendown()
    george.fillcolor("orange")
    george.begin_fill()
    george.left(30)
    george.forward(60)
    george.left(105)
    george.forward(100 / math.sqrt(2))
    george.left(75)
    george.forward(60)
    george.left(105)
    george.forward(100 / math.sqrt(2))
    george.left(45)
    george.end_fill()

    # Bring the turtle down to the front door
    george.penup()
    george.goto(-100, -150)
    george.left(90)


ebel_frank = turtle.Turtle()


class MySquare:

    # my beautiful squares
    def Square():
        ebel_frank.forward(100)
        ebel_frank.right(90)
        ebel_frank.forward(100)
        ebel_frank.right(90)
        ebel_frank.forward(200)
        ebel_frank.right(90)
        ebel_frank.forward(200)
        ebel_frank.right(90)
        ebel_frank.forward(200)
        ebel_frank.right(90)
        ebel_frank.forward(100)
        ebel_frank.right(90)
        ebel_frank.forward(100)
        ebel_frank.left(90)
        ebel_frank.forward(100)
        ebel_frank.left(180)
        ebel_frank.forward(200)
        ebel_frank.left(153.43)
        ebel_frank.forward(223.6067977)
