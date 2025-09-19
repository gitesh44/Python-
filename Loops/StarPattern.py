# Star Pattern using for loop

n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(" "* (n-i),end="")  #end="" is used to avoid new line after print statement
    print("*"* (2*i-1),end="")
    print("")