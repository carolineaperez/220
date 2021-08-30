"""
Name: <Caroline Perez>
lab1.py

Problem: This function calculates the area of a rectangle
"""
def calc_rec_area():
    length= eval(input('Enter the length: '))
    width = eval(input('Enter the width: '))
    area = length * width
    print ("Area =", area )


def calc_volume():
    length = eval(input('Enter the length: '))
    width = eval(input('Enter the width: '))
    height = eval(input('Enter the height: '))
    volume = length * width * height
    print('Volume= ', volume)


def shooting_percentage():
    shotsmade = eval(input('Enter the shotsmade: '))
    shotsattempted = eval(input('Enter the shots attempted: '))
    shootingpercentage = shotsmade/shotsattempted * 100
    print ("Shooting percentage = ",shootingpercentage)


def coffee():
    numberofpounds = eval(input('Enter the number of pounds of coffee purchases:'))
    costs= 10.5 * numberofpounds
    shipping= .86 * numberofpounds
    fixed= 1.5
    totalcost= costs + shipping + fixed
    print ('Total cost= ', totalcost)


def kilometers_to_miles():
    numberofkilometerstraveled = eval(input('Enter the distance traveled in kilometers:'))
    miles = numberofkilometerstraveled/1.61
    print (miles)


calc_rec_area()
calc_volume()
shooting_percentage()
coffee()
kilometers_to_miles()