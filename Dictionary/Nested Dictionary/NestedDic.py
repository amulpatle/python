course ={
    'Java':{'duration':'2 Months', 'fees': 3000, 'Decs':'core java course'},
    'python':{'duration':'2 Months','fees':7999, 'Desc' : 'core Python course'},
    'c++':{'Duration':'3 Months','fees':5999, 'desc':'Advance c++ course'}
}

print(course)

for k,v in course.items():
    print(k,v)

for k,v in course.items():
    print(k,v['duration'],v['fees'])