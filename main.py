with open('reception.txt') as f:
    cockbook1 = f.read().splitlines()
cockbook = {}
for cock in cockbook:
    key, value = cockbook1.split(': ')
    cockbook.update({key: value})
print(cockbook1)