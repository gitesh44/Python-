f=open("poem.txt")
content=f.read()
if("twinkle" in content):
    print("yes,present")
else:
    print("no,not present")


print(content)
f.close()
