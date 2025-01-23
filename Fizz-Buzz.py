#Fizz - Buzz Challenge - 101Computing.net

for i in range(1,101):
  
 
  num1= i%3
  num2= i%5
  
  if num1 != 0 and num2 != 0:
    print(i)
  
  elif num1 == 0:
    
    if num2 == 0:
      print("fizz-buzz")
    else:
      print("fizz")
      
  else:
    print("buzz")

  # challenge 2

print("enter numbers 1-100 in order. number divided by 3 enter the word `fizz`, divided by 5 enter the word `fuzz`, divided by both numbers enter `fizz-buzz`")
  
for i in range(1,101):

    number = input("enter a number: ")
    if number.isnumeric():
      number = int(number)
    else:
      number = str(number)
      
    if i%3 != 0 and i%5 != 0 and number != i:
      print("you loose, try again")
      break
    elif i%3 == 0 and i%5 == 0 and number != "fizz-buzz":
      print("you loose, try again")
      break
    elif i%3 == 0 and i%5 != 0 and number != "fizz":
      print("you loose, try again")
      break
    elif i%3 != 0 and i%5 == 0 and number != "buzz":
      print("you loose, try again")
      break
    
    # challenge 3
    
    
print("enter numbers 1-100 in order. number divided by 3 enter the word `fizz`, divided by 5 enter the word `fuzz`, divided by both numbers enter `fizz-buzz`")
  
live_count = 0
  
for i in range(1,101):
  
    number = input("enter a number: ")
    if number.isnumeric():
      number = int(number)
    else:
      number = str(number)
      
    if i%3 != 0 and i%5 != 0 and number != i:
      live_count += 1
      print("you left", 3-live_count, "tries until you loose")
      
      if live_count == 3:
        print("you loose, try again")
        break
      else: 
        continue
      
    elif i%3 == 0 and i%5 == 0 and number != "fizz-buzz":
      
      live_count += 1
      print("you left", 3-live_count, "tries until you loose")
      if live_count == 3:
        print("you loose, try again")
        break
      else: 
        continue
    
    elif i%3 == 0 and i%5 != 0 and number != "fizz":
      
      live_count += 1
      print("you left", 3-live_count, "tries until you loose")
      if live_count == 3:
        print("you loose, try again")
        break
      else: 
        continue
    
    elif i%3 != 0 and i%5 == 0 and number != "buzz":
      live_count += 1
      print("you left", 3-live_count, "tries until you loose")
      if live_count == 3:
        print("you loose, try again")
        break
      else: 
        continue
      
    
    
  