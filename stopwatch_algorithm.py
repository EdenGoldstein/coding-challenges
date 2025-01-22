#Stopwatch Algorithm - www.101computing.net/from-flowcharts-to-python-code/

number = 45015
hours = number/3600
remainder = number % 3600
minutes = remainder/60
seconds = remainder%60

print(number, "seconds = ", hours, "hours", minutes, "minutes and", seconds, "seconds")