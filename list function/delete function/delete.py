l = [3,45,63,76,11,90,0,32,8]

size = len(l)

print(l)
# del keyword work in index number
del l[1]
print(l)

#pop() function works on index and it also return popped value when we print it
l.pop(3)
print(l)
print(l.pop(4))
print(l)

#remove function works on value . when we want to delete a value from lint we simply pass that value
l.remove(76)
print(l)

#clear function :- this function clear whole list. this function does not workin on index nor value
l.clear()
print(l)