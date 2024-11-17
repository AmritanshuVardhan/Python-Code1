# Break
for i in range(1,80):
    if i == 21:
        break #Exit the loop right now
    print(i)


#Continue
for i in range(0, 100, 2):
    if i == 18:
        continue #Skip this iteration
    print(i)



#Pass
for i in range(45):
    pass #pass is a null statement in python
         #It instruct to "do nothing"
         #Without pass, the program will throw an error


i=1
while(i<45):
    print(i)
    i+=1