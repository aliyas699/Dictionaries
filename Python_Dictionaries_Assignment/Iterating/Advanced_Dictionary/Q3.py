# Original dictionary
my_dict = {'z': 1, 'a': 2, 'c': 3}

# Sort the dictionary by keys in ascending order
sorted_dict = {key: my_dict[key] for key in sorted(my_dict)}

# Print the sorted dictionary
print(sorted_dict)
