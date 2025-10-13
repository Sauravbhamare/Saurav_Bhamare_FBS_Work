def notes(Data,amount):
    note_count = {}
    for note in Data:
        if(amount >= note):
            note_count[note] = amount // note
            amount = amount % note
            
            
    print("Minimum number of notes required:")
    for note , count in note_count.items():
        print(f"{note}:{count}")
        
Data = [2000,500,200,100,50,20,10,5]
amount = int(input("Enter amount:"))
notes(Data,amount)
