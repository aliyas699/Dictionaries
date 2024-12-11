# Original dictionary
my_dict = {'a': 10, 'b': 15, 'c': 10, 'd': 15}

# Create a new dictionary to store unique values
unique_values_dict = {}
for key, value in my_dict.items():
    if value not in unique_values_dict.values():
        unique_values_dict[key] = value

# Print the dictionary with unique values
print(unique_values_dict)
