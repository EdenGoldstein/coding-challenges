# AI:Bot Training Challenges - www.101computing.net/for-loops-challenges

# Writing Lines
for i in range(0,101):
   print("I will listen to my teacher and complete my work on time")
# counting in 5 from 0 to 500  
for i in range(0,501, 5):
   print(i)
   
# counting down

for i in range(100,-1, -1):
   print(i)

# times table

for i in range(1,11):
   print(12*i)
# times table given number

number = int(input("enter a number"))

for i in range(1,11):
   print(number*i)

# the alphabet
   
for i in range (65,91):
   print(chr(i))

# iterative sum

number = int(input("enter a number"))
sum =0

for i in range(0,number+1):
   sum += i
   
print("Iterative sum of", f"{number}", "=", f"{sum}")
   
# factorial

number = int(input("enter a number"))
sum =1

for i in range(1,number+1):
   sum = sum*i
   
print("factorial sum of", f"{number}", "=", f"{sum}")
