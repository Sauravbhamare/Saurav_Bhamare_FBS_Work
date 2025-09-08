User_id = 'admin'
password = 12345
count = 0

while(count<3):
    uid = input("Enter the username:")
    pw = int(input("Enter the password:"))
    if(User_id == uid and password == pw):
        print("Username and password is valid.")
        break
    else:
        print("Username and password is invalid.")
    count +=1
if(count == 3):
    print("Too many Attempts.Access Denied.")