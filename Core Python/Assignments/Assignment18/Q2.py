class Distance:
    def __init__(self,km,m,cm):
        self.km = km
        self.m = m
        self.cm = cm
        
    def __add__(self,other):
        cm = self.cm + other.cm
        m = cm // 100
        self.cm = cm % 100
        m = self.m + other.m + m
        km = m // 1000
        self.m = m % 1000
        self.km = self.km + other.km + km
        return self
    
    def __sub__(self,other):
        cm = self.cm - other.cm
        m = cm // 100
        self.m = m % 100
        m = self.m - other.m - m
        km = m // 1000
        self.m = m % 1000
        self.km = self.km - other.km - km
        return self
        
    def __str__(self):
        return f'{self.km}:{self.m}:{self.cm}'
        
d1 = Distance(1,2,23)
d2 = Distance(1,2,23)

print(d1+d2)
print(d1-d2)