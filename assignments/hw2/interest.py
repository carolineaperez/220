def main():
    annualinterestrate= eval(input('Enter the annual interest rate:'))
    numberofdaysinabillingcycle = eval(input('Enter the number of days in a billing cycle:'))
    netbalanceshown = eval(input('Enter the net balance shown:'))
    paymentamount = eval(input('Enter the payment amount:'))
    daythepaymentwasmade = eval(input('Enter the day of the billing cycle in which the payment was made:'))
    step1= netbalanceshown * numberofdaysinabillingcycle
    step2= paymentamount * (numberofdaysinabillingcycle - daythepaymentwasmade)
    step3= step1 - step2
    step4= step3 / numberofdaysinabillingcycle
    monthlyinterestrate = (annualinterestrate/ 12) /100
    answer= monthlyinterestrate * step4
    print(answer)
main()

'''read about -s on stack over flow'''
