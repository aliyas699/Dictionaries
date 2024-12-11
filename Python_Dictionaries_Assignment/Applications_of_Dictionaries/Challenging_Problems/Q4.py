# Given dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Initialize two dictionaries for odd and even values
odd_dict = {}
even_dict = {}

# Split the dictionary into odd and even based on values
for key, value in my_dict.items():
    if value % 2 == 0:
        even_dict[key] = value
    else:
        odd_dict[key] = value

# Print the resulting dictionaries
print("Odd values dictionary:", odd_dict)
print("Even values dictionary:", even_dict)
