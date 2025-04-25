def sum_of_digits(number):
    total = 0  # Initialize sum to 0
    
    # Loop until number becomes 0
    while number > 0:
        digit = number % 10  # Extract the last digit
        total += digit  # Add the digit to the total
        number = number // 10  # Remove the last digit
    
    return total  # Return the sum of digits

# Call the function and print the result
print("Sum of digits:", sum_of_digits(1234))  # Example: 1+2+3+4 = 10
