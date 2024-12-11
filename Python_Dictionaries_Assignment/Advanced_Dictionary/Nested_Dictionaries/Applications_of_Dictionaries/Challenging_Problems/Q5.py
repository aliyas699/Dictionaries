# Given dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Dictionary comprehension to filter out keys where value is less than 3
filtered_dict = {key: value for key, value in my_dict.items() if value >= 3}

# Print the filtered dictionary
print(filtered_dict)
