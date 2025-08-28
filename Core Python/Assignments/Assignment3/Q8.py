import random
user_id = input("Enter the User_ID:")
password = input("Enter password:")

uid = 'saurav'
pw = '12345'


if(user_id == uid and password == pw):
    print("The user_id and password are valid.")
    captcha = random.randint(1000,9999)
    print(f'captcha : {captcha}')
    captcha1 = int(input("Enter the given Captcha:"))
    if(captcha1 == captcha):
        print("Captcha is valid.")
    else:
        print("Captcha is invalid.")
else:
    print("The user_id and password is invalid.")
    
 