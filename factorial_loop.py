def factorial_loop(n):
    result = 1  # Initialize result to 1 (since 0! and 1! are 1)
    
    # Multiply result by each integer from 1 to n
    for i in range(1, n + 1):
        result *= i
    
    return result  # Return the computed factorial
