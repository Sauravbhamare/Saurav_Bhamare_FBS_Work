m1 = int(input("Enter the marks of Subject1:"))
m2 = int(input("Enter the marks of Subject2:"))
m3 = int(input("Enter the marks of Subject3:"))
m4 = int(input("Enter the marks of Subject4:"))
m5 = int(input("Enter the marks of Subject5:"))

sum = m1 + m2 + m3 + m4 + m5

percent= sum / 500 * 100

if(percent >= 80):
    print("The result is First class.")
elif(percent >= 60):
    print("The result is second class.")
elif(percent >= 35):
    print("The result is pass.")
else:
    print("The result is fail.")