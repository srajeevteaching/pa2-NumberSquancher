# Programmer: Aidan Shaughnessy
# Course: CS701/GB-731, Dr. Rajeev
# Date: 10/5/21
# Programming Assignment: 2
# Program Inputs: month and year
# Program Outputs: leap year and days in month

# Problem Write a program that asks the user to enter the month (represented as a number in the range 1 through 12)
# and the year. The program should then display the number of days in that month.
# Use the following criteria to identifyleap years:

# Determine whether the year is divisible by 100. If it is, then it is a leap year if and only if it is
# divisible by 400. For example, 2000 is a leap year but 2100 is not. If the year is not divisible by 100, then it
# is a leap year if and if only it is divisible by 4. For example, 2008 is a leap year but 2009 is not.
# Example: if the user enters 2 for the month and 2008 for the year, the program should say that month has 29 days.

# input/variable
month = float(input("Input month's number: "))
year = int(input("Input year: "))
days = 0

# if statements
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            leapYear = True
            print(year, "is a leap year")
        else:
            leapYear = False
            print(year, "isn't a leap year")
    else:
        leapYear = True
        print(year, "is a leap year")
else:
    leapYear = False
    print(year, "isn't a leap year")

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 \
        or month == 10 or month == 12:
    days = 31
    print(days, "days in the month", month)
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30
    print(days, "days in the month", month)
elif (leapYear == True) and month == 2:
    days = 29
    print(days, "days in the month", month)
elif (leapYear == False) and month == 2:
    days = 28
    print(days, "days in the month", month)
else:
    print("This number isn't connected to a month.")

