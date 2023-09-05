l = [1,23,87,48,0,24,71]

size = len(l)

print(" ")
for i in range(size):
    print(l[i])

print(" ")
for i in range(1,size,2):
    print(l[i])

print(" ")
for a in l:
    print(a)

# print in reverse order
print(" ")
for x in range(size-1,-1,-1):
    print(l[x])