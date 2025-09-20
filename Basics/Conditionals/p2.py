
# A student will not be allowed to sit in exam if his/her attendance is less than 75%.
# Take following input from user       

marks1=int("Enter the marks of subject 1-")
marks2=int("Enter the marks of subject 2-")
marks3=int("Enter the marks of subject 3-")

total_percentage=(100*(marks1+marks2+marks3))/300
if total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33:
    print("The student has passed the exam",total_percentage)
else:
    print("The student has failed the exam",total_percentage)