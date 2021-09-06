"""
Name: Caroline Perez
lab2.py
"""
import math


def sum_of_threes():
    x = eval(input('what is the upper bound?'))
    acc = 0
    for s in range(0, x+1, 3):
        acc = acc+s
    print(acc)



def multiplication_table():
    for h in range(1,11):
        for l in range(1,11):
            print(h * l, end=" ")
        print(' ')


def triangle_area():
    a = eval(input('what is the length of side a? '))
    b = eval(input('what is the length of side b? '))
    c = eval(input('what is the length of side a? '))
    s = (a + b + c) / 2
    start = s * (s - a) * (s - b) * (s - c)
    A = math.sqrt(start)
    print(A)


def sumSquares():
    starting_number = eval(input('what is the lower range? '))
    ending_number = eval(input('what is the upper range? '))
    m  = 0
    for l in range(starting_number, ending_number + 1):
        square = l ** 2
        m = m + square
    print(m)


def power():
    base = eval(input('what is the base? '))
    exponent = eval(input('what is the exponent? '))
    acc = 1
    for w in range(exponent):
        acc = acc * base
    print(  base, ' ^ ',exponent, '=', acc)



sum_of_threes()
multiplication_table()
triangle_area()
sumSquares()
power()

