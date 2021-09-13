"""
Name: <Caroline Perez>
lab3.py
"""


def average():
    x = eval(input('# of grades to input:'))
    acc = 0
    for i in range(1, x+1):
        grade = eval(input('Enter your grade for HW' + str(i) + ':'))
        acc += grade
        average_grade = acc/x
    print(average_grade)


def tip_jar():
    acc = 0
    for i in range(5):
        amount = eval(input('Enter the amount you want to donate:'))
        acc += amount
    print(acc)


def newton():
    x = eval(input('What is the number you want to square root:'))
    refine = eval(input('how many times do you want to refine it: '))
    approx = x/2
    for i in range(refine):
        approx = ((approx + (x / approx))/2)
    print(approx)


def sequence():
    x = eval(input('what is the number of terms in a series:'))
    for i in range(1, x + 1):
        seq = 1 + (i//2) * 2
        print(seq, end=' ')
        print()


def pi():
    n = eval(input(' Number of terms in a series:'))
    acc = 1
    for i in range(n+1):
        num = 2 + ((i//2) * 2)
        den = 1 + ((i+1)//2) * 2
        fraction = num / den
        acc = acc * fraction
    print(acc)


average()
tip_jar()
newton()
sequence()
pi()
