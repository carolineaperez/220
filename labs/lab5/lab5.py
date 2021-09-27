"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

from graphics import *

import math


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target


    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    point_a = win.getMouse()
    point_b = win.getMouse()
    point_c = win.getMouse()

    point_b.draw(win)
    point_a.draw(win)
    point_c.draw(win)

    # distance formula
    tri = Polygon(point_a, point_b, point_c)
    tri.draw(win)

    # Add code here to accept the mouse clicks, draw the triangle.

    # distance formula
    tri = Polygon(point_a, point_b, point_c)
    tri.draw(win)

    win.getMouse()

    pAx = point_a.getX()
    pAy = point_a.getY()
    pBx = point_b.getX()
    pBy = point_b.getY()
    pCx = point_c.getX()
    pCy = point_c.getY()
    side_1 = math.sqrt((pBx- pAx)**2 + (pBy- pAy)**2)
    side_2 = math.sqrt((pCx - pBx) ** 2 + (pCy - pBy) ** 2)
    side_3 = math.sqrt((pAx - pCx) ** 2 + (pAy - pCy) ** 2)
    perimeter = side_1 + side_2 + side_3
    s = perimeter / 2
    area = math.sqrt((s)*(s-side_1)*(s-side_2)*(s-side_3))
    # and display its area in the graphics window.
    p = Text(Point(300, 200), perimeter)
    p.draw(win)
    answer_area = Text(Point(300, 250), area)
    answer_area.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")


    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    get_red_box = Entry(Point(win_width / 2 - 20, win_height / 2 + 40), 5)
    get_green_box = Entry(Point(win_width / 2 - 20, win_height / 2 + 70), 5)
    get_blue_box = Entry(Point(win_width / 2 - 20, win_height / 2 + 100), 5)

    get_red_box.draw(win)
    get_green_box.draw(win)
    get_blue_box.draw(win)
    win.getMouse()
    for i in range(5):
        r = int(get_red_box.getText())
        g = int(get_green_box.getText())
        b = int(get_blue_box.getText())
        color = color_rgb(r, g, b)
        shape.setFill(color)
        win.getMouse()

    # Wait for another click to exit
    win.getMouse()
    win.close()

def process_string():
    input_string = (input('Input String:'))
    # 1
    first_character = input_string[0]
    print(first_character)

    length= len(input_string)
    # 2
    last_character = input_string[length-1]
    print(last_character)
    # 3
    print(input_string[2:6])
    #4
    print(first_character + last_character)
    #5
    number_five = input_string[0:3] * 10
    print(number_five)
    #6
    for i in input_string:
        print(i)
    #7
    print(length)


def process_list():
    pt = Point(5, 10)
    values = [5,'hi',2.5,'there',pt,'7.2']
    x = values[1] + values[3]
    print(x)
    a = values[0]
    b= values[2]
    x = a + b
    print(x)
    x = values[1]*5
    print(x)
    x = [values[2], values[3], values[4]]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    c = values[0]
    d = values[2]
    e = float(values[5])
    x = c + d + e
    print(x)
    x = len(values)
    print(x)


def another_series():
    n = eval(input("How many inputs?"))
    acc = 0
    for i in range(n):
        y = 2 + (2 * (i % 3))
        acc += y
        print(y, end="")
    print()
    print(acc)


def main():
    # target()
    triangle()
    color_shape()
    another_series()
    process_string()
    process_list()
    pass


main()
