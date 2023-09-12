d = {
    'Name':'Python',
    'Fees': 8000,
    'Duration':'2 Months'
}

print(d)

print(d.get('Name'))

for a in d.keys():
    print(a)

for a,b in d.items():
    print(a,b)

for a in d.values():
    print(a)

# deletion  in dectionary
del d['Duration']
print(d)

# pop fucntion return a value which we want to delete
print(d.pop('Name'))
print(d)

d['desc'] = 'this is python course'
print(d)

d['Fees'] = 1000
print(d)