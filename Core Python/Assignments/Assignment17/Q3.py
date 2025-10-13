from Q1 import Student

class MedicalStudent(Student):
    def __init__(self,StudentId,Name,Age,percentage,Specialization,marksofInternship):
        super().__init__(StudentId,Name,Age,percentage)
        self.specialization = Specialization
        self.internmarks = marksofInternship
        
        
    def Enter(self):
        super().accept()
        self.specialization = input("Enter Specialization:")
        self.internmarks = int(input("Enter Marks of internship:"))
    
    def displayData(self):
        super().display()
        print(f"Specialization:{self.specialization}")
        print(f"Internship marks:{self.internmarks}")
    def cal_rank(self):
        total = self.percentage + (self.internmarks * 3)
        if(total >= 90):
            return 'A'
        elif(total >= 75):
            return 'B'
        elif(total >= 60):
            return 'C'
        elif(total >= 50):
            return 'D'
        else:
            return 'Fail'
    
    def __str__(self):
        return f'{self.StudentId}\n{self.Name}\n{self.Age}\n{self.percentage}\n{self.specialization}\n{self.internmarks}'
        
m1 = MedicalStudent(102,'sb',23,90.0,'Surgeon',350)        
m1.displayData()