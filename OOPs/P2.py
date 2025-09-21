class Calculator:
    
    def __init__(self,a):
        self.a=a;
    
    def sqr(self,a):
        return a*a;
    
    def cube(self,a):
        return a*a*a;
    
    def sqrr(self,a):
        return a**1/2;
    
    
o=Calculator(10);
print(o.sqr(2));
print(o.cube(10));
print(o.sqrr(16));
    
    
    
        
        