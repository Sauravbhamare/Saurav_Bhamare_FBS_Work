P = int(input("Enter the Principle Amount:"))
R = int(input("Enter the Rate of interest:"))
T = int(input("Enter the Time of Interest:"))

CI = P * (1 + R / 100)**T  - P
print(f"The Compound Interest is {CI}.")