num = int(input("Enter the three digit Number:"))

A = num % 10
num = num // 10

B = num % 10
num = num // 10

C = num % 10
num = num // 10

addition = A + B + C 

print(f'Addition of given three digit number: {addition}.')