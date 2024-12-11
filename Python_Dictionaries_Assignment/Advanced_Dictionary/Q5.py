def are_dicts_identical(dict1, dict2):
    return dict1 == dict2

# Example dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 1, 'b': 2, 'c': 3}
dict3 = {'a': 1, 'b': 2, 'd': 4}

# Check if dict1 and dict2 are identical
print(are_dicts_identical(dict1, dict2))  # True

# Check if dict1 and dict3 are identical
print(are_dicts_identical(dict1, dict3))  # False
