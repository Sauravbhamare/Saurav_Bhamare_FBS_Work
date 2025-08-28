age1 = int(input("Enter the age of person1:"))
age2 = int(input("Enter the age of person2:"))
age3 = int(input("Enter the age of person3:"))
age4 = int(input("Enter the age of person4:"))
age5 = int(input("Enter the age of person5:"))
ticket_amount = int(input("Enter the ticket amount:"))
if(age1 < 12):
    ticket = ticket_amount * 0.3
    print(f'Ticket amount:{ticket}.')
elif(age1 > 59):
    ticket = ticket_amount * 0.5
    print(f'Ticket amount: {ticket}.')
else:
    print(f'Ticket amount: {ticket_amount}.')
    
    
            
if(age2 < 12):
    ticket = ticket_amount * 0.3
    print(f'Ticket amount : {ticket}.')
elif(age2 > 59):
    ticket = ticket_amount * 0.5
    print(f'Ticket amount:{ticket}.')
else:
    print(f'ticket amount: {ticket_amount}.')  
    
    

if(age3 < 12):
    ticket = ticket_amount * 0.3
    print(f'Ticket amount: {ticket}')
elif(age3 > 59):
    ticket = ticket_amount * 0.5
    print(f'Ticket amount: {ticket}') 
else:
    print(f'Ticket amount: {ticket_amount}.')
    
    
    
if(age4 < 12):
    ticket = ticket_amount * 0.3
    print(f'Ticket amount: {ticket}.')
elif(age4 > 59):
    ticket = ticket_amount * 0.5
    print(f'Ticket amount: {ticket}.')
else:
    print(f'Ticket amount: {ticket_amount}.')    
    
    
    
if(age5 < 12):
    ticket = ticket_amount * 0.3
    print(f'Ticket amount: {ticket}.')
elif(age5 > 59):
    ticket = ticket_amount * 0.5
    print(f'Ticket amount: {ticket}.')
else:
    print(f'Ticket amount: {ticket_amount}.')

