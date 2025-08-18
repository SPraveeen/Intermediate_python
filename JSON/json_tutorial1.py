import json

json_string='''
{
    "students":[
    {
        "id":1,
        "name":"Tim",
        "age":21,
        "full-time":true
    },
    {
        "id":2,
        "name":"Joe",
        "age":33,
        "full-time":false
    }
    ]
}
'''

data=json.loads(json_string)

# json to dictionary

# print(data)
# print(data['students'][0])

# adding new key to that json/dictionary 
data['test']=True

new_json=json.dumps(data,indent=2,sort_keys=True)
print(new_json)
