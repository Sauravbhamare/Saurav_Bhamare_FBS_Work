gender = input("Enter the Gender(M/F):")
age = int(input("Enter Age:"))

if(gender == 'M'):
    if(age >= 21):
        print("Eligible for Marriage.")
    else:
        print("Not Eligible for Marriage.")
else:
    if(gender == 'F'):
        if(age > 17):
            print("Eligible for Marriage.")
        else:
            print("Not Eligible for Marriage")
        