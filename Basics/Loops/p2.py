# Program to print the multiplication table of a given number




# using for loop
m=int(input("Enter the number : "))
for i in range(1,11):
    i=i*m
    print(f"{m}*{i} ={m*i} ")
    
    
#while loop
a=1
while(a<=10):
    print(a*m)
    a=a+1