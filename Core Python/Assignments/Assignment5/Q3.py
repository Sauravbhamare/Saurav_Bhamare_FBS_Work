num = int(input("Enter the number of passengers:"))
ticket_cost = float(input("Enter the ticket amount:"))
total_cost = 0
passenger = 1
while(passenger<=num):
    age = int(input(f'Enter age of passenger{passenger}:'))
    if(age<12):
        amount = ticket_cost * 0.7
    elif(age>59):
        amount = ticket_cost * 0.5
    else:
        amount = ticket_cost
    
    print(f'Ticket amount of passenger{passenger}:{amount}.')
    total_cost += amount
    passenger += 1

print(f'Total amount of ticket for all passengers:{total_cost}.')