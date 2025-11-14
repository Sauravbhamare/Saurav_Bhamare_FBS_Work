def calculator():
    try:
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter Second number:"))
        
        operator = input("Enter Operator(+,-,*,/):")
        
        if(operator == '+'):
            result = num1 + num2
        elif(operator == '-'):
            result = num1 - num2
        elif(operator == '*'):
            result = num1 * num2
        elif(operator == '/'):
            result = num1 / num2
        else:
            print("Invalid Input...")
        print(f"result:{result}")
    
    except ValueError as e:
        print("Invalid number entered:", e)
    except Exception as e:
        print("An unexpected error occured:",e)
        

if __name__ == "__main__":
    calculator()
        