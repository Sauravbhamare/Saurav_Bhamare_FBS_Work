class Television:
    def __init__(self):
        self.model_no = 0
        self.screen_size = 0
        self.price = 0
        
    def get_data(self):
        try:
            self.model_no = int(input("Enter Model Number:"))
            self.screen_size = float(input("Enter Screeen size:"))
            self.price = float(input("Enter price:"))
            
            if(self.model_no > 9999 or self.model_no < 0):
                print("Error: Model number must have at most 4 digits.")
                self.model_no = 0
                self.screen_size = 0
                self.price = 0
            elif(self.screen_size < 12 or self.screen_size > 70):
                print("Error: Screen size must be between 12 and 70 inches.")
                self.model_no = 0
                self.screen_size = 0
                self.price = 0
            elif(self.price < 0 or self.price > 5000):
                print("Error: Price must be between 0 and 5000 Rs.")
                self.model_no = 0
                self.screen_size = 0
                self.price = 0
        
        except ValueError as e:
            print("Error: Invalid Input! Please enter numbers only.",e)
            self.model_no = 0
            self.screen_size = 0
            self.price = 0
    
    def display_data(self):
        print("Model Number:",self.model_no)
        print("Screen Size:",self.screen_size)
        print("Price:",self.price)
        
tv = Television()
tv.get_data()
tv.display_data()
                