# json to dictionary

import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}
personJSON=json.dumps(person,indent=4,sort_keys=True)

with open('person.json','r')as file:
    person=json.load(file)
    print(person)