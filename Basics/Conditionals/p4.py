# Write a program to check if the username contains less than 10 characters. 
# If it contains less than 10 characters, then the username is valid otherwise it is not valid 


username=input("Enter your username-")
if len(username)<10:
    print("Username is invalid less than 10 characters")
else:
    print("Username is valid more than 10 characters")
    
