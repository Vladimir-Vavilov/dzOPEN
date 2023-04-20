with open('reception.txt') as f:
    cockbook1 = f.read()
cockbook = {}
for cock in cockbook:
    key, value = cockbook.split(': ')
    cockbook.update({key: value})
print(cockbook1)