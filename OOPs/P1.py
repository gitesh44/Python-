#OOPs- Object Oriented Programming
#Class and Object
#Program to demonstrate class and object


class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,pincode,product):#constructor #It is a special function which is called automatically when an object is created
        self.name=name
        self.product=product
        self.salary=salary
        self.pincode=pincode
        print("Object is created")
    
p=Programmer("Ravi",100000,560037,"AI")
    
print(p.name) 
print(p.product) 
print(p.pincode)
print(p.salary) 