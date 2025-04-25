def reverse_string(s):
    reversed_str = ""  # Initialize an empty string to build the reversed version
    
    # Loop through each character in the original string
    for char in s:
        # Prepend the current character to reversed_str
        reversed_str = char + reversed_str
    
    return reversed_str  # Return the fully reversed string
# Calling the function with different strings
print(reverse_string("hello"))    # Output: olleh
print(reverse_string("12345"))    # Output: 54321
print(reverse_string(""))         # Output: "" (empty string)
