#Write a program to store seven fruits in a list entered by the user.
fruits = []
for i in range(7):
    fruit = input(f"Enter fruit {i+1}: ")
    fruits.append(fruit)
# fruits.append(input("Enter fruit 1:    "))
# fruits.append(input("Enter fruit 2:    "))
# fruits.append(input("Enter fruit 3:    "))
# fruits.append(input("Enter fruit 4:    "))
print(fruits)