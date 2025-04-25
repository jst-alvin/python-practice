def check_even_odd(num):
    # If number is divisible by 2 with no remainder, it's even
    if num % 2 == 0:
        return "Even"
    else:  # Otherwise, it's odd
        return "Odd"
        # Calling the function with different numbers
print(check_even_odd(4))     # Output: Even (4 % 2 == 0)
print(check_even_odd(7))     # Output: Odd (7 % 2 != 0)
print(check_even_odd(0))     # Output: Even (0 % 2 == 0)

