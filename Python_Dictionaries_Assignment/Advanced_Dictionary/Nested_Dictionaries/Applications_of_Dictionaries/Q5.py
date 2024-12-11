def get_value(dictionary, key):
    # Check if the key exists in the dictionary
    if key in dictionary:
        return dictionary[key]
    else:
        return "Key not found"

# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Test with an existing key
print(get_value(my_dict, 'b'))  # Output: 2

# Test with a non-existing key
print(get_value(my_dict, 'd'))  # Output: Key not found
