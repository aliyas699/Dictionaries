# Original nested dictionary
nested_dict = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}

# Initialize an empty dictionary to store the flattened result
flat_dict = {}

# Flatten the dictionary
for outer_key, inner_dict in nested_dict.items():
    for inner_key, value in inner_dict.items():
        flat_dict[f"{outer_key}_{inner_key}"] = value

# Print the flattened dictionary
print(flat_dict)
