# this is a python dictionary holding box scores
j_allen = {
    'c/att': [32, 40],
    'yards': 375,
    'touchdowns': 4,
}
# you can get a value from the dictionary using bracket notation
# print(f" Josh Allen had {j_allen['yards']} yards last night")
# If I try to obtain a value for a key that doesn't exist, python throws a KeyError"
#print(j_allen['attempts'])
# dict.get() allows the code to keep running even if the key doesn't exist 
# print(f"Josh Allen had {j_allen.get('attempts', 'no')} attempts last night")

# you can use math operations to change values if they are numbers
j_allen['yards'] += 1
# print(f" UPDATE: Josh Allen had {j_allen['yards']} yards last night")
# you can add a new key, value pair to a dictionary using bracket notation
j_allen['interceptions'] = 0

# you can get all the key, value pairs as tuples from a dictionary
# for item in j_allen.items():
#     print(f"Josh allen had {item[1]} {item[0]}")



