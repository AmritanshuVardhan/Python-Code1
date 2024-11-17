s = {}
for i in range(4):
    name = input('Enter friends name: ')
    lang = input('Enter language name: ')
    s.update({name:lang})
print(s)