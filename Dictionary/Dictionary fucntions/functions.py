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