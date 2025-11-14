import pickle
from emp import Emp



def add_record():
    eid = input("Enter Employee ID: ")
    ename = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))

    e = Emp(eid, ename, basic)
    with open('employee.txt', "ab") as fp:
        pickle.dump(e, fp)
    print("Record Added Successfully!\n")
    
def search_record():
    eid = input("Enter Employee ID to search:")
    found = 0
    try:
        with open('employee.txt','rb') as fp:
            e = pickle.load(fp)
            if(e.eid == eid):
                print("Record Found:",e)
                found = 1
            
    except FileNotFoundError as e:
        print("File not found!",e)
        return
    if(found == 0):
        print("Record not found!")
        
def display_all():
    try:
        with open('employee.txt','rb') as fp:
            e = pickle.load(fp)
            print(e)
            
    except FileNotFoundError as e:
        print("No Records Found!", e)
        
def delete_record():
    eid = input("Enter Employee id to delete:")
    found = 0
    records = []
    
    try:
        with open('employee.txt','rb') as fp:
            e = pickle.load(fp)
            if(e.eid != eid):
                records.append(e)
                
    except FileNotFoundError as e:
        print("File Not found!",e)
        return
    
    with open('employee.txt','wb'):
        for e in records:
            pickle.dump(e,fp)
            
    if(found == 1):
        print("Record Deleted Successfully!")
    else:
        print("Record not found!")
        
def edit_record():
    eid = input("Enter Employee ID to Edit:")
    found = 0
    records = []
    
    try:
        with open('employee.txt','rb') as fp:
            e = pickle.load(fp)
            if(e.eid == eid):
                print("Record found", e)
                e.ename = input("Enter New Name:")
                e.basic = input("Enter New Basic Salary:")
                found = 1
            records.append(e)
    except FileNotFoundError as e:
        print("File Not found!", e)
        return
    
    with open('employee.txt','wb') as fp:
        for e in records:
            pickle.dump(e,fp)
            
    if(found == 1):
        print("Record Updated Successfully!")
    else:
        print("Record Not Found!")
        