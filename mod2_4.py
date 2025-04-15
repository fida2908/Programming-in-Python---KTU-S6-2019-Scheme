# Write a Python program to count how many times each character appears in a given string and store the count in a dictionary with key as the character.

# Input string
input_string = input("Enter a string: ")

# Dictionary to store character counts
char_count = {}

# Loop through each character in the string
for char in input_string:
    if char in char_count:
        char_count[char] += 1  # Increment count if already in dictionary
    else:
        char_count[char] = 1   # Initialize count to 1

# Display the result
print("Character frequencies:")
for char, count in char_count.items():
    print(f"'{char}': {count}")

