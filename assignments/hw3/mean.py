"""
Name : Caroline Perez
mean.py

Problem : calculating the different types of mean

Certification of Authenticity
I certify that this assignment is entirely my own work

"""
# The program will solve for the RMs Average, the Harmonic Mean, and a set of numbers
# the inputs will be hpw many numbers they want to put into the program, and what those numbers are
# the outputs will be the RMS Average, Harmonic Mean, and the Geometric Mean
# 1. ask for the input
# 2. loop through the amount of inputs and the inputs themself
# 3. compute the RMS Average, Compute the Harmonic mean , Compute the geometric mean
# 4. prints and around the answers
import math


def main():
    amount_of_values = eval(input('# of values to be entered:'))
    acc = 0
    acc1 = 0
    acc2 = 1
    for i in range(1, amount_of_values +1):
        #RMSAverage
        value = eval(input('Enter value ' + str(i) + ' :'))
        acc += value**2
        average_arithmetic = acc/amount_of_values
        rms_average = math.sqrt(average_arithmetic)
        #Harmonic Mean
        denom = 1/value
        acc1 += denom
        harmonic_mean = amount_of_values / acc1
        #Geometric Mean
        acc2 *= value
        geometric_mean = acc2 ** (1/amount_of_values)
    print(round(rms_average, 3))
    print(round(harmonic_mean,3))
    print(round(geometric_mean, 3))


if __name__ == "__main__":
    main()
