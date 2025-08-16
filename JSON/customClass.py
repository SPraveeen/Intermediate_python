import json

class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age

user=User('Max',27)

def encode_user(o):
    if isinstance(o,User):
        return {'name':o.name,'age':o.age,o.__class__.__name__:True}
    else:
        raise TypeError('object of type user is not json serializable')

from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o,User):
            return {'name':o.name,'age':o.age,o.__class__.__name__:True}        
        return JSONEncoder.default(self,o)

userJSON=json.dumps(user,cls=UserEncoder)
userJSON1=UserEncoder().encode(user)
print(userJSON)
print(userJSON1)

user1=json.loads(userJSON)
print(user1)
print(type(user1))