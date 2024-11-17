l = ['Make a lot of money', 'Buy Now', 'Subscribe this', 'Click this']
p1 = 'Make a lot of money'
p2 = 'Buy Now'
p3 = 'Subscribe this'
p4 = 'Click this'
msg = (input("Enter your comment: "))
# if (p1 in msg or p2 in msg or p3 in msg or p4 in msg):
if(msg in l):
    print("This comment is a spam!")
else: 
    print("This comment is not a spam!") 