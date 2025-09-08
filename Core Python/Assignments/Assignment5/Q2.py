num = int(input("Enter number of students:"))
total_percent = 0
student = 1
while(student <= num):
    marks = int(input(f'Enter the marks of student{student}:'))
    subject = 1
    total_marks = 0
    while(subject <= 5):
        mark_sub = int(input(f'Enter marks of subject{subject}:'))
        total_marks += mark_sub
        subject += 1
    
    percentage = total_marks / 5
    print(f'Percentage of student {student}:{percentage}')

    total_percent += percentage
    student += 1
average_percent = total_percent / num
print(f'Average percentage of all students:{average_percent}.')