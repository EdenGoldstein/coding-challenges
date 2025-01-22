
  #Python Slicing in Python - www.101computing.net/python-slicing-in-python/


username = input("enter a username that include your year group, first letter of your first name, last name, _ and S for student/T for teachers/A for admin. example: 07jFox_S")
if len(username)<6 or username.find("_") == (-1):
  username = input("enter a valid username")

else:
  status = username.find("S" or "T" or "A")
  if username[status] == "S":
    print("the year group is", username[0:2])
    print("the student name initial is", username[2:3], "and his last name is", username[3:-2])
 
print("the user is a/an: ", f"{username[status]},", ("  S = student, T = teacher, A = admin"))
  