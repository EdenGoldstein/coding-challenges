#Login Form Algorithm - www.101computing.net/from-flowcharts-to-python-code/

username = input("enter a user name")
password = input("enter a password")

if username == "admin" and password == "1234":
    print("you are logged in")
else:
    print("incorrect username or password")