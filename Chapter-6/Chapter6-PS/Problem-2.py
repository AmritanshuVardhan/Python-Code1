marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

total_percent = (marks1+marks2+marks3)/300*100
print("Total Percentage: ",total_percent)

if(total_percent>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are pass.")
else:
    print("You failed, try again next year!")