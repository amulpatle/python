str = "Learn Python"

n = str.lower()
print(n)
n = str.upper()
print(n)
n = str.title()
print(n)
n = str.capitalize()
print(n)

# __________________________

# Use find fucntion

print("Use find fucntion")
print(str.find('n'))
print(str.find('n',5))

#use index function
print("use index function")
print(str.index('a'))
print(str.find('m'))

# chr function use 
x = chr(66)
print(type(x),x)

#ord function use --- it simply take an charater and return assci value of that character 

y = ord('A')
print(type(y),y)

# Use formate function -- it uses to formate string at rumtime

str = input("Enter you name :- ")
str1 = int(input("Enter an interger :- "))

str3 = "My name is {} and my age is {}".format(str,str1)
print(str3)