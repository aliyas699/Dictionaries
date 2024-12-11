# Take input from the user
n = int(input("Enter a positive integer n: "))

# Create a dictionary with keys as integers and values as their cubes
cube_dict = {i: i**3 for i in range(1, n+1)}

# Print the dictionary
print(cube_dict)
