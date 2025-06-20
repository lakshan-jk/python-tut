
import json

# Original Python dictionary
data = {"name": "lux", "age": 25, "city": "San Francisco"}

# Convert Python dictionary to JSON string
json_str = json.dumps(data)
print("JSON String:", json_str)

# Convert JSON string back to Python dictionary
data_back = json.loads(json_str)
print("Converted Dictionary:", data_back)

# Verify the original and converted dictionaries are equal
print("Are original and converted dictionaries equal?", data == data_back)
