l = [12,68,91,20,3,46,0,29,33]

print(l)
l[0] = 9
print(l)

#insert functionn :- this function uses to insert element at given index
# this functionn require two arguments first is index and second one is value
# edge case :- if we pass outof size index we will get error

l.insert(0,99)
print(l)

# append function :- this function add element at last  position of list
#  we can also append new list in existing list 
l.append(59)
print(l)
li = [0,8]
l.append(li)
print(l)

# extend function :-

lis = [24,53]
l.extend(lis)
print(l)