class SYmarks:
    def __init__(self,computer_total,maths_total,electronics_total):
        self.computer_tot = computer_total
        self.maths_tot = maths_total
        self.electronics_tot = electronics_total
        
    def __str__(self):
        return (f'Computer:{self.computer_tot}\nMaths:{self.maths_tot}\nElectronics:{self.electronics_tot}')
        