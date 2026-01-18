# serialization and deserialization
# serialization is the process of converting the objects into bite or JSON for streaming 
# deserialization is the reverse process.

# binary serialization --> pickle module
# JSOn serialization --> json module

import pickle
import json

data = {"name": "Kari", "skills": ["python", "SQL", "Azure"]}

# serializing with files
with open('data.pkl', "wb") as file:
    pickle.dump(data, file)
# deserializing with files
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)
print(loaded_data)

# serializing without files
byte_data = pickle.dumps(data)

# deserializing without files
loaded = pickle.loads(byte_data)

print(loaded)

# serialization using json without files
json_data = json.dumps(data)

# deserializing without files
loaded_json = json.loads(json_data)

print(json_data)
print(loaded_json)

# with files

with open("data.json", "w") as file:
    json.dump(data, file)
with open("data.json", "r") as file:
    new_data = json.load(file)
print(new_data)

print(byte_data)