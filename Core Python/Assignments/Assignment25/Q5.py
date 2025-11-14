import re

def validate_email(email):
    
    pattern = r'\w+@\w+\.\w+'
    if(re.fullmatch(pattern,email)):
        print("Valid Email:",email)
    else:
        print("Invalid Email:",email)
        
emails = ["saurav@gmail.com","ankit@yahoo@.com","abc@xyz.com"]

for e in emails:
    validate_email(e)