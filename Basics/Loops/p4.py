# Check if a number is prime or not using for-else loop

m=int(input("Enter the number "))
for i in range(2,m):
    if(m%i==0):
        print("Not a prime number")
        break
else:
    print("Prime number")   