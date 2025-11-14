from SY_package import SYmarks
from TY_package import TYmarks

class Student:
    def __init__(self,roll_no,name,SYmarks,TYmarks):
        self.roll_no = roll_no
        self.name = name
        self.sy_marks = SYmarks
        self.ty_marks = TYmarks
        
    def cal_result(self):
        total_comp_marks = self.sy_marks.comp_tot