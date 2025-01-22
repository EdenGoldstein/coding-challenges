#Leap Year Algorithm - www.101computing.net/from-flowcharts-to-python-code/

year = int(input("enter a year"))
if year%4 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")