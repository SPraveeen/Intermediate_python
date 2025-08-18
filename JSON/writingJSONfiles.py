import json

# reading json
with open('data.json','r') as f:
    data=json.load(f)

# writing JSON
with open('data2.json','w') as c:
    json.dump(data,c,indent=3)