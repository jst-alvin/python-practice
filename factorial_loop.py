def factorial_loop(n):
    result = 1  # Initialize result to 1 (since 0! and 1! are 1)
    
    # Multiply result by each integer from 1 to n
    for i in range(1, n + 1):
        result *= i
    
    return result  # Return the computed factorial
    # Calling the function with different numbers
print(factorial_loop(3))     # Output: 6 (1*2*3)
print(factorial_loop(5))     # Output: 120 (1*2*3*4*5)
print(factorial_loop(0))     # Output: 1 (0! = 1 by definition)

