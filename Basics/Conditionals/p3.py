# A spam comment is defined as a text containing the following keywords: "make a lot of money", 
# "buy now", "subscribe this", "click this". Write a program to check if the text entered 
# by the user is a spam or not. (The program should be case insensitive).

p1="MAKE A LOT OF MONEY"
p2="BUY Now"
p3="SUBSCRIBE THIS"  
p4="CLICK THIS"

message=input("Enter the message-")
if(p1 in message) or (p2 in message) or (p3 in message) or (p4 in message):
    print("This is a spam message")
else:   
    print("This is not a spam message")