age = int(input("Enter your age: "))

if(age%2 ==0):
    print("Even!")
else:
    print("Odd!")


if(age>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(age<=0):
    print("You are entering an invalid age: ")

else:
    print("You are below the age of consent")

print("End of Program.")

# Quick Ouiz
# age = int(input("Enter Age: "))
# if(age>=18):
#     print("YES!")
# else:
#     print("NO!")