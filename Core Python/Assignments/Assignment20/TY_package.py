class TYmarks:
    def __init__(self,theory,practical):
        self.theory = theory
        self.practical = practical
        
    def __str__(self):
        return f"Theory:{self.theory}\nPractical:{self.practical}"