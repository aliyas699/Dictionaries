# Given dictionaries
dict1 = {'a': 5, 'b': 10}
dict2 = {'a': 3, 'b': 7}

# Create a new dictionary to store the result
result = {}

# Iterate through the keys of dict1 (or dict2 since they have the same keys)
for key in dict1:
    if key in dict2:
        result[key] = dict1[key] + dict2[key]

# Print the result
print(result)
