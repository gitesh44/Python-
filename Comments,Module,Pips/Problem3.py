# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that.

#Taken from ChatGPT for reference and learning about os module in Python and its functions


import os

# specify the path ('.' means current directory)
path = '/'

# list all files and directories in the given path
contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)
