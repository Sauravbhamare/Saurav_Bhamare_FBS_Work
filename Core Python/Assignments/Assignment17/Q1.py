class Student:
    def __init__(self,StudentId,nm,age,Percent):
        self.StudentId = StudentId
        self.Name = nm
        self.Age = age
        self.percentage = Percent
        
        
    def accept(self):
        self.StudentId = input("Enter Student ID:")
        self.Name = input("Enter Name:")
        self.Age = int(input("Enter age:"))
        self.percentage = float(input("Enter Percentage:"))
        
        
    def display(self):
        print(f"Student Id:{self.StudentId}")
        print(f"Name:{self.Name}")
        print(f"Age: {self.Age}")
        print(f"Percentage: {self.percentage}")
        print(f"Rank: {self.cal_rank()}")
    def cal_rank(self):
        if(self.percentage >= 90):
            return 'A'
        elif(self.percentage >= 75):
            return 'B'
        elif(self.percentage >= 60):
            return 'C'
        elif(self.percentage >= 50):
            return 'D'
        else:
            return 'Fail'
        
    def __str__(self):
        return f"Student({self.StudentId},{self.Name},{self.Age},{self.percentage})"
    
    
# s1 = Student("S1","Saurav",22,90.0)
# s1.display()

# s2= Student("S2","Ankit",22,91.2)
# s1.display()