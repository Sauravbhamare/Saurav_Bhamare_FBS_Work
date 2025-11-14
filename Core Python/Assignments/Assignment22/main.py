import empmanage as em

def main():
    ch = 0
    while(ch != '6'):
        print('''
            1.Add Record
            2.Display All Records
            3.Search Record by ID
            4.Delete Record by ID
            5.Edit Record by ID
            6.Exit''')
        ch = input("Enter Choice:")
        if(ch == '1'):
            em.add_record()
        elif(ch == '2'):
            em.display_all()
        elif(ch == '3'):
            em.search_record()
        elif(ch == '4'):
            em.delete_record()
        elif(ch == '5'):
            em.edit_record()
        elif(ch == '6'):
            print("Program Exited Successfully!")
        else:
            print("Invalid Choice...")
            
if(__name__ == "__main__"):
    main()