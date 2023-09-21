import json

dis = {
    "course":"Python course",
    "fees":1200,
    "discriptionn":"this is python course"
}

f = json.dumps(dis)

print(f)
print(type(f))##it will give string type of f variable because it will return json type data