basic = int(input("Enter the Basic salary of Employee:"))

da = (10 / 100) * basic
ta = (12 / 100) * basic
hra = (15 / 100) * basic

tot_salary = basic + da + ta + hra

print(f'The total salary of Employee: {tot_salary}')