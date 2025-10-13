from Q1 import Student

class EnggStudent(Student):
    def __init__(self,StudentId,Name,Age,percentage,branch,InternalMarks):
        super().__init__(StudentId,Name,Age,percentage)
        self.branch = branch
        self.internalmarks = InternalMarks
        
    def Enterdata(self):
        super().accept()
        self.branch = input("Enter branch:")
        self.internalmarks = int(input("Enter Internal Marks obtained:"))
        
    def showData(self):
        super().display()
        print(f"Branch of Student:{self.branch}")
        print(f"Internal Marks of student:{self.internalmarks}")
        
    def cal_rank(self):
        total = self.percentage + (self.internalmarks * 3)
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
        return f'{self.StudentId}\n{self.Name}\n{self.Age}\n{self.percentage}\n{self.branch}\n{self.internalmarks}'
    

e1 = EnggStudent(101,'sb',22,97,'Computer',350)
e1.showData()