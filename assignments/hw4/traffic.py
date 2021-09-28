"""
Name: Caroline Perez
traffic.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    roads = eval(input("How many roads were surveyed?"))
    acc = 0
    for i in range(1, roads + 1):
        days = eval(input("How many days was road " + str(i) + " surveyed?"))
        average = 0
        for day in range(1, days + 1):
            traveled = eval(input(      'How many cars traveled on day ' + str(day) + '?'))
            acc += traveled
            average += traveled
        print("Road", str(i), "average vehicles per day:", round(average/days, 2))
    print("total number of vehicles traveled on all roads:", acc)
    print('Average number of vehicles per road:', round(acc/roads, 2))


if __name__ == '__main__':
    main()
