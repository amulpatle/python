import json

j = '{"cName":"python", "duration":"2 Months", "discription":"this is python course"}'

x = json.loads(j)

print(x)