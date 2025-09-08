num = int(input("Enter number of employees:"))
employee = 1
total_salary_employees = 1
for i in range(1,num+1):
    basic = int(input(f"Enter basic salary of employee{employee}:"))
    if(basic < 20000):
        da = 10/100 * basic
        ta = 12/100 * basic
        hra = 15/100 * basic
        total_salary = basic + da + ta + hra
        print(f'Total salary of employee{employee}:{total_salary}.')
    else:
        da = 15/100 * basic
        ta = 18/100 * basic
        hra = 20/100 * basic
        total_salary = basic + da + ta + hra
        print(f'Total salary of employee{employee}:{total_salary}')
    
    total_salary_employees += total_salary   
    employee += 1
    
print(f'Total salary of all employees:{total_salary_employees}.') 