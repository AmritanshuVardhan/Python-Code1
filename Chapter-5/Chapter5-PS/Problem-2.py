n = int(input("Enter term number:"))
s = set()
for i in range(1,n+1):
    val = input(f"Enter number {i}: ")
    s.add(int(val))
print(s)