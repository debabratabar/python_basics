import json

# some JSON:
x = { "name":"John", "age":30, "city":"New York"}



# parse x:
#y = json.loads(z)

for ( id , userDetails ) in enumerate(x , start=1):
            print(f"{id}. Video Name : {type(userDetails)}")

# the result is a Python dictionary:
# print(y)
