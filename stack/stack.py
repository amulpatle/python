l = []
while True:
    c = int(input('''
            1 = push the value
            2 = pop 
            3 = peek element
            4 = print the list
            5 = exit    
            '''))
    
    if c == 1:
            x = int(input("enter the vlaue :-"))
            l.append(x)
            print(l)
    elif c == 2:
            if len(l) == 0:
                   print("stack is empty")
            else:
                   a = l.pop()
                   print(a)
                   print(l)
    elif c== 3:
           if len(l) == 0:
                  print("Stack is Empty")
           else:
                  print(l[-1])
    elif c == 4:
           print(l)
    elif c == 5:
           break

            