num = int(input("Enter a number: "))
product = 1
for i in range(1, num+1):
    product = product*i

print(f"The factorial of {num} is {product}")