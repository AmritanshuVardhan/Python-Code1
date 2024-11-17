# for i in range(1,5):
#     num = int(input(f"Enter number {i}: "))
# print(type(num))

num1 = int(input("Enter 1st no.:"))
num2 = int(input("Enter 2nd no.:"))
num3 = int(input("Enter 3rd no.:"))
num4 = int(input("Enter 4th no.:"))

if(num1 > num2 and num1>num3 and num1>num4):
    print(f'Num1 {num1} is greatest.')
elif(num2 > num3 and num1>num4):
    print(f'Num2 {num2} is greatest')
elif(num3 > num4):
    print(f'Num3 {num3} is greatest')
else:
    print(f'Num4 {num4} is greatest')
